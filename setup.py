#!/usr/bin/env python3

"""Setup script."""

from setuptools import setup

setup(
    name="hangman",
    version="1.0",
    author="Roman Proskin",
    author_email="opomuc@gmail.com",
    url="https://github.com/opomuc/tinkoff-hangman",
    license="MIT",
    packages=[
        "game",
    ],
    install_requires=[
    ],
    setup_requires=[
        "pytest-runner",
        "pytest-pylint",
        "pytest-pycodestyle",
        "pytest-pep257",
        "pytest-cov",
    ],
    tests_require=[
        "pytest",
        "pylint",
        "pycodestyle",
        "pep257",
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ]
)
