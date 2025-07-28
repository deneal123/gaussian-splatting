from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
import os
import subprocess
import sys


SUBMODULES = [
    # 'submodules/diff-gaussian-rasterization',
    # 'submodules/simple-knn',
    # 'submodules/fused-ssim'
]


class CustomInstall(install):
    def run(self):
        for submodule in SUBMODULES:
            print(f"Installing {submodule}...")
            subprocess.check_call([sys.executable, 'setup.py', 'install'], cwd=submodule)
        install.run(self)


class CustomDevelop(develop):
    def run(self):
        for submodule in SUBMODULES:
            print(f"Installing {submodule} in develop mode...")
            subprocess.check_call([sys.executable, 'setup.py', 'develop'], cwd=submodule)
        develop.run(self)


setup(
    name="gaussian_splatting",
    version="0.1.0",
    description="Gaussian Splatting implementation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/graphdeco-inria/gaussian-splatting",
    packages=find_packages(),
    install_requires=[
        'plyfile',
        'tqdm',
        'opencv-python',
        'joblib',
        'torch>=1.13.1',
        'torchvision>=0.14.1',
    ],
    cmdclass={
        'install': CustomInstall,
        'develop': CustomDevelop,
    },
    python_requires='>=3.10',
)
