

'''reads specified number of lines from file and returns a list of strings'''
def read_n_lines(size , input_file):

	list = []
	for i in range(size):
		list.append(input_file.readline().strip())
	
	return list

	


'''takes list of names as input and returns army size as a dictionary'''
def count_soldiers(list_of_names):
	
	armies = {}
	for name in list_of_names:
		name = name.split(' ')[0]
		if name not in armies:
			armies[name] = 1
		else:
			armies[name] += 1
	return armies

def write_outputs(outputs):
	output_file = open('output.txt' , 'w+')
	for i in range(len(outputs)):
		output_file.write("Case: {}\n".format(i+1))
		for key , value in outputs[i].items():
			output_file.write("{} {}\n".format(key,value))
		output_file.write('\n')
	output_file.close()
				
	
def main():
	input_file = open('input.txt')

	# first line is the number of test cases
	num_of_test_cases = int(input_file.readline())

	# to store the output of each case
	outputs = [None] * num_of_test_cases 

	for i in range(num_of_test_cases):
		num_of_inputs = int(input_file.readline()) # get number of inputs in each test case
		list_of_names = read_n_lines(num_of_inputs , input_file) # get list of name in each test case
		armies = count_soldiers(list_of_names) # count the names
		outputs[i] = armies 

	write_outputs(outputs)

main()
