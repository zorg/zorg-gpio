#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

req = open("requirements.txt")
requirements = req.readlines()

# Dynamically retrieve the version from the module
version_string = __import__('zorg_gpio').__version__

setup(
    name="zorg-gpio",
    version=version_string,
    url="https://github.com/zorg/zorg-gpio",
    description="GPIO drivers for Zorg robots.",
    setup_requires=['setuptools-markdown'],
    long_description_markdown_filename='README.md',
    author="Zorg Group",
    author_email="gunthercx@gmail.com",
    packages=find_packages(),
    package_dir={"zorg_gpio": "zorg_gpio"},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=True,
    platforms=["any"],
    keywords=["zorg", "gpio"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    test_suite="tests",
    tests_require=[]
)
