SHELL := /bin/bash

release:
	python setup.py register sdist bdist_wheel upload

test:
	nosetests

