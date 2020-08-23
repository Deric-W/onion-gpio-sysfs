#!/usr/bin/python3

import onionGpio
import setuptools

with open("README.md", "r") as fd:
    long_description = fd.read()

setuptools.setup(
    name="onion_gpio_sysfs",
    version=onionGpio.__version__,
    author=onionGpio.__author__,
    author_email=onionGpio.__email__,
    description=onionGpio.__doc__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=onionGpio.__contact__,
    py_modules=["onionGpio"],
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Topic :: System :: Hardware :: Hardware Drivers",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming language :: Python :: 3.9"
    ],
    keywords="onion omega IoT gpio",
    python_requires=">=3.5",
)
