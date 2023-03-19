#! /usr/bin/env bash

# TODO: Improve this setup script a lot. See the project README.md for better info.

# Prior to this:
# Install the latest Python into your Pyenv: pyenv install 3.11.2
# pyenv virtualenv 3.11.2 ve.ansimynet
# NOTE: The .python-version included in the project contains: ve.ansimynet
# This is how Pyenv automatically activates the correct VE, for any
# location in any subdirectory underneath a .python-version file.
# How marvelous is that! lol. The wonders of Pyenv abound.

pip install --upgrade pip
pip install --upgrade setuptools
pip install --upgrade wheel

