# -*- coding: utf-8 -*-

from setuptools import setup

execfile("bootstrappercli/version.py")
version = __version__

setup(
    name='bootstrappercli',
    version=version,
    url='http://github.com/sentinelleader/bootstrappercli',
    author='Deepak Mohandas',
    author_email='deepakmdass88@gmail.com',
    packages=['bootstrappercli'],
    scripts=['bin/bootstrappercli'],
    description='Boootstrapper client script',
    install_requires=[
          'requests',
    ],
    long_description=open('README.md').read(),
)
