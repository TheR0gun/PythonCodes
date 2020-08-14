def calculator(input_str2):
	symbols=['+','-','/','*','%']
	input_str = input_str2.replace(" ", "")

	index= 0
	for i in input_str:
		if input_str[index] in symbols:
			first_op=int(input_str[:index])
			last_op=int(input_str[index+1:])
			op=input_str[index]
			if op == '+':
				print('{} + {} = '.format(first_op, last_op))
				return print(first_op + last_op)
			elif op == '-':
				print('{} - {} = '.format(first_op, last_op))
				return print(first_op - last_op)
			elif op == '/':
				print('{} / {} = '.format(first_op, last_op))
				return print(first_op / last_op)
			elif op == '*':
				print('{} * {} = '.format(first_op, last_op))
				return print(first_op * last_op)
			elif op == '%':
				print('{} % {} = '.format(first_op, last_op))
				return print(first_op % last_op)
		else:
			index += 1

	return print('Not a arthematic expression')

with open("mathprob.txt") as math_inputs:
	for line in math_inputs:
		calculator(line)
