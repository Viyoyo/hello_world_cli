#! /bin/sh
# -- ties it all together
# -- tells python how to handle it

from setuptools import
setup(
	name = "hello_cli"),
	version = "0.1.0"
	packages = ["hello_cli"],
	entry_points = {
		"console_scripts" : [
			"hello_cli = hello_cli.__main__:main"

		]
	})