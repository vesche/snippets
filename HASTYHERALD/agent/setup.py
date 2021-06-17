#!/usr/bin/env python

from setuptools import setup
from hhagent.meta import VERSION

setup(
    name='hhagent',
    packages=[
        'hhagent',
    ],
    version=VERSION,
    description='HASTYHERALD agent',
    license='MIT',
    url='https://github.com/CyborgSecurity/HASTYHERALD',
    author='Austin Jackson',
    author_email='vesche@protonmail.com',
    entry_points={
        'console_scripts': [
            'hhagent = hhagent.cli:main',
        ]
    },
    install_requires=[
        'pyautogui',
        'sanic'
    ],
    classifiers=[
        'License :: Public Domain',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8'
    ]
)