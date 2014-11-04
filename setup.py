from setuptools import setup

setup(
    name = "pycanlii",
    description = "A python wrapper for the CanLII API",
    packages = ["pycanlii"],
    version = "1.0.1b1",
    author = "Jonathan Webb",
    home_page = "http://sherlocke.me/developers/",
    install_requires=["requests"]
    )