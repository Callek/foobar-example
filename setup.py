#!/usr/bin/env python3
from typing import List

from setuptools import setup

# Any annotated var fails, if before the used requirements var
foobar: List[str] = []

# packages to setup
requirements = []

setup(
    name="foobar-example",
    version="0.0.1",
    description="foobar-example",
    url="https://github.com/Callek/foobar-example",
    license="Unlicense",
    install_requires=requirements,
)
