# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name="linked_list",
    description="Demonstration of a linked list",
    version=0.1,
    author="Crystal Lessor and Mike Harrison",
    license='MIT',
    py_modules=['linked_list'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch']}
    )