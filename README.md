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
gantry run --timeout -1 -- python src/main.py
```