import matplotlib.pyplot as plt
from packaging import version

# Data pulled from Beaker
data = [
    {"model": "Qwen/Qwen1.5-14B-Chat", "score": 0.226, "vllm_version": "0.8.3"},
    {"model": "Qwen/Qwen1.5-14B-Chat", "score": 0.224, "vllm_version": "0.8.0"},
    {"model": "Qwen/Qwen1.5-14B-Chat", "score": 0.22, "vllm_version": "0.6.6.post1"},
    {"model": "Qwen/Qwen1.5-14B-Chat", "score": 0.228, "vllm_version": "0.8.4"},
    {"model": "Qwen/Qwen1.5-14B-Chat", "score": 0.228, "vllm_version": "0.8.5.post1"},
    {"model": "Qwen/Qwen1.5-14B-Chat", "score": 0.238, "vllm_version": "0.9.1"},
    {"model": "Qwen/Qwen1.5-14B-Chat", "score": 0.222, "vllm_version": "0.8.2"},
    {"model": "Qwen/Qwen1.5-14B-Chat", "score": 0.22, "vllm_version": "0.6.6"},
    {"model": "Qwen/Qwen1.5-14B-Chat", "score": 0.224, "vllm_version": "0.8.1"},
    {"model": "Qwen/Qwen1.5-14B-Chat", "score": 0.224, "vllm_version": "0.6.4.post1"},
    {"model": "Qwen/Qwen1.5-14B-Chat", "score": 0.22, "vllm_version": "0.6.5"},
    {"model": "Qwen/Qwen1.5-14B-Chat", "score": 0.23, "vllm_version": "0.9.0"},
    {"model": "Qwen/Qwen1.5-14B-Chat", "score": 0.234, "vllm_version": "0.9.0.1"},
    {"model": "Qwen/Qwen1.5-14B-Chat", "score": 0.234, "vllm_version": "0.8.5"},
    {"model": "Qwen/Qwen1.5-14B-Chat", "score": 0.218, "vllm_version": "0.7.2"},
    {"model": "Qwen/Qwen1.5-14B-Chat", "score": 0.218, "vllm_version": "0.7.3"},
    {"model": "Qwen/Qwen1.5-14B-Chat", "score": 0.218, "vllm_version": "0.5.5"},
    {"model": "Qwen/Qwen1.5-14B-Chat", "score": 0.218, "vllm_version": "0.7.0"},
    {"model": "Qwen/Qwen1.5-14B-Chat", "score": 0.218, "vllm_version": "0.6.2"},
    {"model": "Qwen/Qwen1.5-14B-Chat", "score": 0.218, "vllm_version": "0.7.1"},
    {"model": "Qwen/Qwen1.5-14B-Chat", "score": 0.224, "vllm_version": "0.6.4"},
    {"model": "Qwen/Qwen1.5-14B-Chat", "score": 0.218, "vllm_version": "0.6.1.post1"},
    {"model": "Qwen/Qwen1.5-14B-Chat", "score": 0.218, "vllm_version": "0.6.3.post1"},
    {"model": "Qwen/Qwen1.5-14B-Chat", "score": 0.218, "vllm_version": "0.6.1"},
    {"model": "Qwen/Qwen1.5-14B-Chat", "score": 0.218, "vllm_version": "0.6.3"},
    {"model": "Qwen/Qwen1.5-14B-Chat", "score": 0.218, "vllm_version": "0.6.1.post2"},
    {"model": "Qwen/Qwen1.5-14B-Chat", "score": 0.232, "vllm_version": "0.5.4"},
]

# Sort by version number
data.sort(key=lambda x: version.parse(x["vllm_version"]))

versions = [d["vllm_version"] for d in data]
scores = [d["score"]*100 for d in data]

plt.figure(figsize=(8, 4))
plt.plot(versions, scores, marker='o')
plt.xticks(rotation=45, ha='right')
plt.xlabel('vLLM Version')
plt.ylabel('Exact Match')
plt.title('Minerva 500 for Qwen1.5-14B-Chat (temp=0)')
plt.grid(True)
plt.tight_layout()
plt.savefig('minerva_scores.png')
