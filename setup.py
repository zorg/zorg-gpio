#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from setuptools.command.install import install
from distutils.core import Command
import os


class MakeReadme(Command):
    description = 'Generates a README.rst version of README.md'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            from pypandoc import convert
            rst = convert('README.md', 'rst')
            readme = open('README.rst', 'w+')
            readme.write(rst)
            readme.close()
        except ImportError:
            raise ImportWarning('Module pypandoc not found, could not convert Markdown to RST')


req = open('requirements.txt')
REQUIREMENTS = req.readlines()
req.close()

if os.path.isfile('README.rst') :
    rm = open('README.rst')
    README = rm.readlines()
    rm.close()
else:
    README = ''

# Dynamically retrieve the version from the module
version_string = __import__('zorg_gpio').__version__

setup(
    name='zorg-gpio',
    version=version_string,
    url='https://github.com/zorg/zorg-gpio',
    description='GPIO drivers for Zorg robots.',
    long_description=README,
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
    test_suite='tests',
    tests_require=['mock'],
    cmdclass={
        'make_readme': MakeReadme,
    }
)
