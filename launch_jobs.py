import subprocess


COMMAND = """\
gantry run \
    --name vllm-debug \
    --cluster ai2/augusta-google-1 \
    --budget ai2/oe-eval \
    --workspace ai2/olmo-3-evals \
    --priority high \
    --timeout 0 \
    --gpus 1 \
    --allow-dirty \
    -- \
python src/main.py \
    --package=vllm=={version}
"""

with open("versions.txt") as f:
    versions = [line.strip() for line in f]

for version in versions:
    version = version.split("==")[1]  # Extract just the version number
    cmd = COMMAND.format(version=version)
    print(f"Running command for version {version}")
    subprocess.run(cmd, shell=True)