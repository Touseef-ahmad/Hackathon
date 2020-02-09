#!/usr/bin/python
from argparse import ArgumentParser
def main():
	arg_parser = ArgumentParser()
	arg_parser.add_argument("-n","--name",
		required=True,help="name of the user")
	args = vars(arg_parser.parse_args())
	print("Hi there {}, it's nice to meet you!".format(args["name"]))

if __name__ == "__main__":
	main()
