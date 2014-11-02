from setuptools import setup

setup(
    name = "pycanlii",
    description = "A python wrapper for the CanLII API",
    packages = ["pycanlii"],
    version = "1.0.0",
    author = "Jonathan Webb",
    install_requires=["requests"]
    )