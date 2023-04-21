from setuptools import setup, find_packages

setup(
    name="TPL-package",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "firebase-admin",
        "google",
        "pydantic",
    ]
)