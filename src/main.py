import subprocess
import sys
import argparse


def install_package(package="vllm==0.9.1"):
    print(f"Installing {package}...")
    subprocess.run([sys.executable, "-m", "pip", "install", package])


def run_eval():
    subprocess.run(["python3", "src/eval.py"], check=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", default="vllm==0.9.1", help="Package to install")
    args = parser.parse_args()
    
    install_package(args.package)
    run_eval()