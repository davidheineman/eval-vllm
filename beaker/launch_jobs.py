import subprocess
from concurrent.futures import ThreadPoolExecutor

COMMAND = """\
gantry run \
    --name vllm-debug-{version}-{model_tag} \
    --cluster ai2/augusta-google-1 \
    --beaker-image ai2/cuda12.8-dev-ubuntu22.04-notorch \
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

# MODEL = "Qwen/Qwen3-8B"
MODEL = "Qwen/Qwen1.5-14B-Chat"


with open("versions.txt") as f:
    versions = [line.strip() for line in f]

def run_command(version):
    cmd = COMMAND.format(
        version=version, 
        model=MODEL,
        model_tag=MODEL.split('/')[1]
    )
    print(f"Running command for version {version}")
    subprocess.run(cmd, shell=True)

with ThreadPoolExecutor() as executor:
    executor.map(run_command, versions)