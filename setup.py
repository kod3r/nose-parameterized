#!/usr/bin/env python

import os
import sys

from setuptools import setup, find_packages

os.chdir(os.path.dirname(sys.argv[0]) or ".")

try:
    long_description = open("README.rst", "U").read()
except IOError:
    long_description = "See https://github.com/wolever/nose-parameterized"

setup(
    name="nose-parameterized",
    version="0.5.0",
    url="https://github.com/wolever/nose-parameterized",
    author="David Wolever",
    author_email="david@wolever.net",
    description="Parameterized testing with any Python test framework",
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
    ],
    packages=find_packages(),
    long_description=long_description,
)
