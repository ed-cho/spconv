import json
from pathlib import Path
from setuptools import setup
import platform

CUDA_VERSION_JSON = Path("/usr/local/cuda/version.json")

if CUDA_VERSION_JSON.is_file():
    # Read cuda version as integer (11.7.1 --> 117, 12.1.1 --> 121, etc.)
    with open(CUDA_VERSION_JSON, "r") as file:
        data = json.load(file)
    cuda_version = int("".join(data["cuda"]["version"].split('.')[:2]))
    
    # Assign correct spconv 
    if cuda_version < 113:
        raise ValueError("Please install CUDA >= 11.3. It is recommended to use >= 11.4 if possible")
    elif cuda_version == 115:
        spconv_version = f"spconv-cu114"
    elif cuda_version >= 120:
        spconv_version = f"spconv-cu120"
    else:
        spconv_version = f"spconv-cu{cuda_version}"
else:
    if platform.system() == 'Linux':
        spconv_version = "spconv"
    else:
        raise ValueError(f"CPU version of spconv is only available in LINUX. Please install CUDA toolkit >= 11.3")

setup(
    install_requires=[
        spconv_version
    ],
)
