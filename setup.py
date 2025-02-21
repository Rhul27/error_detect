# setup.py
from setuptools import setup, find_packages

setup(
    name="error_detect",
    version="0.1.0",
    author="Rahul Gond",
    author_email="27rg2000@gmail.com",
    description="A package for detecting errors and generating solutions using an LLM API.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Rhul27/error_detect",  # Update with your repository URL
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # or another license if applicable
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
