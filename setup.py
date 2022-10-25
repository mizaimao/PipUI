#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="pipui",
    version="0.1",
    description="PipUI toy project.",
    author="Mizaimao",
    packages=find_packages(include=["pipui", "pipui.*"]),
)
