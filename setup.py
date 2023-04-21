from setuptools import setup, find_packages

setup(
    name="TPL_package",
    version="0.0.1a",
    packages=find_packages(exclude=['tests*']),
    description='An package used for the TPL project',
    license='MIT',
    install_requires=[
        "fastapi",
        "firebase-admin",
        "google",
        "pydantic",
    ],
    url="https://github.com/The-Programming-Lab/TPL_package",
    author="The Programming Lab",
    author_email="braeden.norman6@gmail.com"
)