#!/usr/bin/env python

from distutils.core import setup

setup(name='car',
      version='0.0.1',
      description='Fun with the Tesla API',
      packages=['car'],
      install_requires=['pyyaml', 'requests'])
