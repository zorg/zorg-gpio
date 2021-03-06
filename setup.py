#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os


def read(fname):
    open_file = open(os.path.join(os.path.dirname(__file__), fname))
    file_content = open_file.read()
    open_file.close()
    return file_content

with open('requirements.txt') as req:
    REQUIREMENTS = req.readlines()

# Dynamically retrieve the version from the module
version_string = __import__('zorg_gpio').__version__

setup(
    name='zorg-gpio',
    version=version_string,
    url='https://github.com/zorg/zorg-gpio',
    description='GPIO drivers for Zorg robots.',
    long_description=read('README.rst'),
    maintainer='Zorg Group',
    maintainer_email='gunthercx@gmail.com',
    packages=find_packages(),
    package_dir={'zorg_gpio': 'zorg_gpio'},
    install_requires=REQUIREMENTS,
    license='BSD',
    zip_safe=True,
    platforms=['any'],
    keywords=['zorg', 'gpio'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests'
)
