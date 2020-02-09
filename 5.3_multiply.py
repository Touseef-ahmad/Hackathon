#!/usr/bin/python
def miltiply_int_with_list(A,num):
	"""this function takes an array and a number and 
	multiplys the number with array in-place"""
	carry = 0
	for i in reversed(range(len(A))):
		temp = (A[i]*num) + carry
		if temp>9:
			carry , temp = temp//10 , temp%10
		A[i] = temp

def multiply_lists(A,B):
	pass

def main():
	A = [1,9,3,7,0,7,7,2,1]
	B = [1,1,1,1,1,1,1,1,1,1,1,1]
	num = 3
	miltiply_int_with_list(A,num)
	print(A)
	

if __name__ == "__main__":
	main()
