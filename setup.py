#!/usr/bin/env python
"""
setup.py
"""

import setuptools

setuptools.setup(
      name='car',
      version='0.0.1',
      description='Fun with the Tesla API',
      packages=['car'],
      install_requires=['pyyaml', 'requests'],
      scripts=['bin/vehicle.py', 'bin/vehicles.py', 'bin/get_info.py'])
