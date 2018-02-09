#!/usr/bin/env python
install_requires = ['numpy','scipy']
# %%
from setuptools import setup,find_packages

setup(name='rmwutils',
      packages=find_packages(),
      version = '1.0.0',
      description='Support utilities for Radio Mobile Deluxe progation predication.',
      long_description=open('README.rst').read(),
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
      extras_require={'plot':['matplotlib','seaborn']},
      python_requires='>=3.5',
	  )

