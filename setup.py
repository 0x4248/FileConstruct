# FileConstruct
# Construct custom files with ease.
# 
# Setup.py
# 
# COPYRIGHT NOTICE
# Copyright (C) 2024 0x4248 and contributors
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the license is not changed.
# 
# This software is free and open source. Licensed under the GNU general
# public license version 3.0 as published by the Free Software Foundation.

from setuptools import setup, find_packages

setup(
	name='FileConstruct',
	version='1.0',
	packages=find_packages(where='src/python'),
	package_dir={'': 'src/python'},
	include_package_data=True,
	install_requires=[],
	python_requires='>=3.6',
	author='0x4248',
)