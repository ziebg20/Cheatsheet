import os
import subprocess
import sys

def install_pip():
    """Ensures pip is installed and up to date."""
    try:
        subprocess.run([sys.executable, "-m", "ensurepip", "--default-pip"], check=True)
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
    except subprocess.CalledProcessError:
        print("Failed to install or upgrade pip. Check your Python installation.")

def install_requirements():
    """Installs the necessary Python packages."""
    required_packages = ["pillow"]
    
    try:
        subprocess.run([sys.executable, "-m", "pip", "install"] + required_packages, check=True)
        print("All dependencies installed successfully.")
    except subprocess.CalledProcessError:
        print("Failed to install required packages.")

if __name__ == "__main__":
    install_pip()
    install_requirements()
