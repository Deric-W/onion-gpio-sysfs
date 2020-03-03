#!/usr/bin/python3

import setuptools
import os
os.chdir("python")
import onionGpio
os.chdir("../")

with open("README.md", "r") as fd:
    long_description = fd.read()

setuptools.setup(
    name="onion-gpio-sysfs++",   # original name onion-gpio-sysfs was already taken
    license="LICENSE.md",
    version=onionGpio.__version__,
    author=onionGpio.__author__,
    author_email=onionGpio.__email__,
    description="module to control the GPIO of onion chips via the sysfs interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=onionGpio.__contact__,
    py_modules=["onionGpio"],
    packages=setuptools.find_packages(where="python"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    keywords="onion omega IoT",
)
