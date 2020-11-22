#! /bin/sh
# -- entry point of the CLI
# -- will be indicated by setup configuration/ setup.py

import sys
from .class_module import My_Class
from .func_module import my_function

def main():
	print("in main")
	args = sys.argv[1:]
	print("count args :: {} ".format(len(args)))
	for arg in args:
		print("passed argument:: {}".format(arg))


	my_function("hello world")

	my_object = My_Class("James")
	my_object.say_name()


if __name__ == "__main__":
	main()