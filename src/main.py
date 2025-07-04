import subprocess
import sys
import argparse

RUN_CMD = """
python src/eval.py --model {model}
"""

INSTALL_CMD = """
pip install {package}
"""


def install_package(package="vllm==0.9.1"):
    cmd = INSTALL_CMD.format(package=package)
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True)


def run_eval(model):
    cmd = RUN_CMD.format(model=model)
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", default="vllm==0.9.1", help="Package to install")
    parser.add_argument("--model", required=True, help="Model name/path to evaluate")
    args = parser.parse_args()
    
    install_package(args.package)
    run_eval(args.model)