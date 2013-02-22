#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

version = '0.1'
ROOT = os.path.dirname(__file__)


def read(fname):
    return open(os.path.join(ROOT, fname)).read()


setup(name='woods',
      version=version,
      description="The MapReduce Panels",
      long_description=read('README.md'),
      keywords='OpenStack',
      author='atomd',
      author_email='dwb319@gmail.com',
      url='https://github.com/atomd/woods.git',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
            #'horizon'
      ],
      classifiers=[
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Internet :: WWW/HTTP',
            'Environment :: OpenStack'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
