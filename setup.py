import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()


PATH = os.path.dirname(__file__)

def get_version():
    with open(os.path.join(PATH, "natsbehave", "VERSION")) as version_file:
        version = version_file.read().strip()
    return version


setuptools.setup(
    name="natsbehave",
    version=get_version(),
    author="Roman Kosobrodov",
    author_email="roman@kosobrodov.net",
    description="Behaviour Tests for NATS applications",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RomanKosobrodov/natsbehave",
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.12',
    install_requires=[
        "nats-py>=2.10.0"
    ]
)
