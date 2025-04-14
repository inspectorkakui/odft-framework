from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="odft-framework",
    version="0.1.0",
    author="Inspector Kakui",
    author_email="inspectorsurefooted@proton.me",
    description="Outcome-Driven Fine-Tuning for LLM Agents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/inspectorkakui/odft-framework",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    include_package_data=True,
)