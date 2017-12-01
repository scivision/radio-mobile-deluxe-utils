#!/usr/bin/env python
install_requires = ['numpy','scipy','matplotlib','seaborn']
# %%
from setuptools import setup,find_packages,

setup(name='rmwutils',
      packages=find_packages(),
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
      install_requires=install_requires,
      python_requires='>=3.5',
	  )

