### Quick start

```sh
# Get all vLLM packages
curl -s https://pypi.org/pypi/vllm/json | jq -r '.releases | keys[]'

pip install -e .
```

```sh
python src/main.py
```

### On Beaker

```sh
gantry run \
    --name vllm-debug \
    --cluster ai2/augusta-google-1 \
    --budget ai2/oe-eval \
    --workspace ai2/olmo-3-evals \
    --priority high \
    --timeout -1 \
    --gpus 1 \
    --allow-dirty \
    -- \
python src/main.py \
    --package=vllm==0.8.2
```