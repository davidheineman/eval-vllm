import subprocess
from concurrent.futures import ThreadPoolExecutor

COMMAND = """\
gantry run \
    --name vllm-debug-{version}-{model_tag} \
    --cluster ai2/augusta-google-1 \
    --beaker-image ai2/cuda12.4-dev-ubuntu20.04 \
    --budget ai2/oe-eval \
    --workspace ai2/olmo-3-evals \
    --priority high \
    --timeout 0 \
    --gpus 1 \
    -- \
python src/main.py \
    --package=vllm=={version} \
    --model={model}
"""

# ai2/cuda11.3-devel-ubuntu20.04
# ai2/cuda11.8-dev-ubuntu20.04
# ai2/cuda12.4-dev-ubuntu20.04
# ai2/cuda12.8-dev-ubuntu22.04-notorch


def run_command(version, model):
    cmd = COMMAND.format(
        version=version,
        model=model,
        model_tag=model.split('/')[1]
    )
    print(f"Running command for version {version}")
    subprocess.run(cmd, shell=True)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str, required=True,
                       help='Model to evaluate (e.g. Qwen/Qwen-14B-Chat)')
    args = parser.parse_args()

    with open("versions.txt") as f:
        versions = [line.strip() for line in f]

    with ThreadPoolExecutor() as executor:
        executor.map(lambda v: run_command(v, args.model), versions)

if __name__ == '__main__':
    main()