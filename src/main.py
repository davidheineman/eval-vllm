import subprocess
import sys
import argparse

COMMAND = """
python src/eval.py --model {model}
"""


def install_package(package="vllm==0.9.1"):
    print(f"Installing {package}...")
    subprocess.run([sys.executable, "-m", "pip", "install", package])


def run_eval(model):
    cmd = COMMAND.format(model=model)
    print(f"Running command for model {model}")
    subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", default="vllm==0.9.1", help="Package to install")
    parser.add_argument("--model", required=True, help="Model name/path to evaluate")
    args = parser.parse_args()
    
    install_package(args.package)
    run_eval(args.model)