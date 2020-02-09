#!/usr/bin/python

def main():

	try:
		input_file = open('input.xml','r')
	except IOError:
		print("the file you're trying to read does not exist.")

if __name__ == "__main__":
	main()
