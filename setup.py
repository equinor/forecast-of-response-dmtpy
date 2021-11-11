import shutil
from setuptools import setup, find_packages
from pathlib import Path

here = Path(__file__).parent.resolve()

# Remove build and dist folders
shutil.rmtree(Path("build"), ignore_errors=True)
shutil.rmtree(Path("dist"), ignore_errors=True)

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

with open('requirements.txt',encoding='utf8') as f:
    required = f.read().splitlines()

setup(
    name='ForApp-dmt-gen',
    version='0.1.0',
    author="UNKNOWN",
    description="Model accessor package for ForApp",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=['tests']),  # Required
    install_requires=required,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: UNKNOWN",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)