Eval on multiple versions of vLLM

![scores](minerva_scores.png)

### Quick start

```sh
pip install -e .
```

```sh
python src/main.py \
    --package=vllm==0.8.2 \
    --model=Qwen/Qwen1.5-14B-Chat
```

```sh
# See available vLLM packages
curl -s https://pypi.org/pypi/vllm/json | jq -r '.releases | keys[]'
```

### On Beaker

```sh
# Launch a single job
gantry run \
    --name vllm-debug \
    --cluster ai2/augusta-google-1 \
    --beaker-image ai2/cuda12.4-dev-ubuntu20.04 \
    --budget ai2/oe-eval \
    --workspace ai2/olmo-3-evals \
    --priority high \
    --timeout -1 \
    --gpus 1 \
    --allow-dirty \
    -- \
python src/main.py \
    --package=vllm==0.0.1 \
    --model=Qwen/Qwen1.5-14B-Chat
```

```sh
# Launch jobs on the cluster!
python beaker/launch_jobs.py --model Qwen/Qwen-14B-Chat
python beaker/launch_jobs.py --model Qwen/Qwen1.5-14B-Chat
python beaker/launch_jobs.py --model Qwen/Qwen2.5-14B-Instruct
python beaker/launch_jobs.py --model Qwen/Qwen3-14B

# Gather results
pip install beaker-py==1.36.2 # need to update script
python beaker/pull_results.py
pip install -U beaker-py

# Render figure
python beaker/render_results.py
```

### Known Issues
- (Fixed) vLLM 0.2.1 was yanked -- https://pypi.org/project/vllm/0.2.1/
- (Fixed) Some vLLM releases rely on `pip install vllm-flash-attn==2.5.8.post3` -- which was yanked for PyPi. https://pypi.org/project/vllm-flash-attn/2.5.8.post3/
- (Fixed) vLLM 0.2.4 requires strict CUDA verisoning -- https://beaker.allen.ai/orgs/ai2/workspaces/olmo-3-evals/work/01JZBJK2J3QH4G5AZW2VKZVSXV/logs?jobId=01JZBJK3418ZG8Z6RRXYV298DR
- Seeing failures for v0.5.xx due to requirement failures -- https://beaker.allen.ai/orgs/ai2/workspaces/olmo-3-evals/work/01JZBJK2PYC39EFBQ9AKFZQVJC/logs?jobId=01JZBJK3409HHFG5JXF649PQRF
- Geneartion is broken on v0.6.0 -- https://beaker.allen.ai/orgs/ai2/workspaces/olmo-3-evals/work/01JZBJK5QMFBR1PHDFP08J93SD