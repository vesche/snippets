#!/usr/bin/env python

from setuptools import setup

setup(
    name='pyfreebloks',
    packages=['pyfreebloks'],
    version='0.1.0',
    description='pyfreebloks - Python clone of the Android game, Freebloks 3D.',
    license='MIT',
    url='https://github.com/vesche/pyfreebloks',
    author='Austin Jackson',
    author_email='vesche@protonmail.com',
    install_requires=[
        'blessed',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console :: Curses',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Topic :: Games/Entertainment',
    ]
)