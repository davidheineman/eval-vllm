import subprocess
import sys

def install_package(package):
    print(f"Installing {package}...")
    subprocess.run([sys.executable, "-m", "pip", "install", package])
    subprocess.run(["python3", "src/eval.py"], check=True)
    
install_package('vllm==0.9.1')