
# this code is for  converting interger to binary 
from Stack import Stack
def intToBinary(input):
	s = Stack()
	while input > 0:
		reminder = input%2
		s.push(reminder)
		input = input // 2

	bn = ""
	while not s.is_empty():
		bn += str(s.pop())

	return bn






input_str = 56
print(intToBinary(input_str))


	