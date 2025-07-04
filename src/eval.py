from dataclasses import dataclass, field
from typing import List, Optional

import huggingface_hub
import torch
from vllm import LLM, CompletionOutput, RequestOutput, SamplingParams
from datasets import load_dataset

from math_extract import extract_answer, is_equiv


@dataclass
class Instance:
    request: str
    gold_completion: Optional[str] = None
    solution: Optional[str] = None
    metadata: dict = field(default_factory=dict)


@dataclass
class Response:
    input: Instance
    output: str


class MathMetric:
    def __init__(self, responses: List[Response]):
        self.responses = responses

    def grade_responses(self):
        self.scores = list(map(self._grade_response, self.responses))

    def compute_metric(self) -> float:
        return sum(self.scores) / len(self.scores) if self.scores else 0.0

    def _grade_response(self, response: Response) -> bool:
        generated = response.output
        correct = response.input.solution

        assert correct is not None

        gen_answers: List[str] = extract_answer(generated)  # extracts many possible answers

        # "math flex" will allow any extracted answer to be correct
        for gen in gen_answers:
            if is_equiv(gen, correct):
                return True

        return False


class MinervaMath:
    SUBSETS = [
        "algebra",
        "counting_and_probability",
        "geometry",
        "intermediate_algebra",
        "number_theory",
        "prealgebra",
        "precalculus",
    ]

    def __init__(self, subset):
        self.dataset = load_dataset(path="EleutherAI/hendrycks_math", name=subset, split="test")
        self.build_requests()

    def build_requests(self):
        self.requests = list(map(self._process_instance, self.dataset))

    def _process_instance(self, doc) -> Instance:
        solution = extract_answer(doc["solution"])[0]  # get primary extracted answer

        # query = "Problem:\n" + doc["problem"] + "\n\nSolution:"
        query = doc["problem"]

        return Instance(
            request=query,
            gold_completion=doc["solution"],
            solution=solution,
            metadata={"level": doc.get("level"), "type": doc.get("type")},
        )


def main():
    model_name = "Qwen/Qwen1.5-14B-Chat"
    # model_name = "Qwen/Qwen3-8B"
    model_path = huggingface_hub.snapshot_download(model_name)

    llm = LLM(model_path, enforce_eager=True, tensor_parallel_size=torch.cuda.device_count())
    sampling_params = SamplingParams(
        temperature=0, 
        max_tokens=1024,
        # stop=["Problem:", "\n\n"]
    )

    scores = {}

    for subset in MinervaMath.SUBSETS:
        print(f"Evaluating {subset}...")

        dataset = MinervaMath(subset)

        instances: List[Instance] = dataset.requests
        queries: List[str] = [instance.request for instance in instances]

        outputs: List[RequestOutput] = llm.generate(queries, sampling_params)

        responses = []
        for input, output in zip(instances, outputs):
            completions: List[CompletionOutput] = output.outputs
            completion = completions[0].text # only sampling 1 output
            responses += [Response(input=input, output=completion)]

        metric = MathMetric(responses)
        metric.grade_responses()
        score = metric.compute_metric()

        print(score)

        scores[subset] = score

    mean_score = sum(scores.values()) / len(scores)
    print(f"Overall mean score: {mean_score:.2%}")

    # Save to job output
    import json
    import os
    os.makedirs("/results", exist_ok=True)
    with open("/results/metrics.json", "w") as f:
        json.dump({"score": mean_score}, f)


if __name__ == "__main__":
    main()
