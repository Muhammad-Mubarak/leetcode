# reverse string using stack
from Stack import Stack
def reverse_string(stack, param_string):
	# s = stack()
	for i in range(len(param_string)):
		stack.push(param_string[i])
	rev_str = ""
	while not stack.is_empty():
		rev_str += stack.pop()

	return rev_str


stack = Stack()
input_str = 'Hello'
print(reverse_string(stack, input_str))

		