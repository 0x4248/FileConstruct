# FileConstruct
# Construct custom files with ease.
# 
# Makefile
# 
# COPYRIGHT NOTICE
# Copyright (C) 2024 0x4248 and contributors
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the license is not changed.
# 
# This software is free and open source. Licensed under the GNU general
# public license version 3.0 as published by the Free Software Foundation.


MAVEN = mvn
PYTHON = python3
PIP = pip3

include tools/clean.mk

all: java-build java-run python-build


java-build:
	$(MAVEN) clean install

java-run:
	$(MAVEN) exec:java -Dexec.mainClass="com.github._0x4248.Examples.HelloWorld"

python-build:
	$(PIP) install .

clean:
	$(MAVEN) clean
	$(PYTHON) setup.py clean
	rm -rf $(CLEAN_TARGETS)