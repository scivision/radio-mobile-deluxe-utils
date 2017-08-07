#!/usr/bin/env python
req = ['nose','numpy']
# %%
import pip
try:
    import conda.cli
    conda.cli.main('install',*req)
except Exception as e:
    pip.main(['install'] + req)
# %%
from setuptools import setup

setup(name='rmwutils',
      packages=['rmwutils'],
      version = '1.0.0',
      description='Support utilities for Radio Mobile Deluxe progation predication.',
      author = 'Michael Hirsch, Ph.D.',
      url = 'https://github.com/scivision/radio-mobile-deluxe-utils',
      classifiers=[
      'Intended Audience :: Science/Research',
      'Development Status :: 5 - Production/Stable',
      'License :: OSI Approved :: BSD License',
      'Topic :: Scientific/Engineering :: GIS',
      'Programming Language :: Python :: 3',
      ],
      install_requires=req,
	  )

