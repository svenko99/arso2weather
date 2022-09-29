from setuptools import setup, find_packages
import codecs
import os
from pathlib import Path

this_directory = Path(__file__).parent

VERSION = "0.1.4"
DESCRIPTION = "Basic package to get the current temperature of Slovenians cities."
LONG_DESCRIPTION = (this_directory / "README.md").read_text()

# Setting up
setup(
    name="arso2weather",
    version=VERSION,
    author="Sven Ulcar",
    author_email="<sven.ulcar@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["requests"],
    keywords=["python", "weather", "slovenia", "arso", "vreme"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
    ],
)
