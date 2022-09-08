import random
import math

random.seed(872352)

c_O = 4 # count of objects
c_U = 6 # count of users
c_A = 3 # count of access levels

O = ['report.pdf', 'main.cpp', 'order.doc', 'kitty.png'] # objects
U = ['Ivan', 'Alexey', 'Oleg', 'Dmitriy', 'George', 'Xi Jinping'] # users

A = {
	0: 'super secret',
	1: 'secret',
	2: 'free access'
}

def get_random_int_in_range(min, max):
	return math.trunc( random.random() * max ) + min

def max_length(l):
	return max(map(lambda x: len(x), l))

OV = [get_random_int_in_range(0, c_A) for i in range(c_O)]
UV = [get_random_int_in_range(0, c_A) for i in range(c_U)]

def print_vector(elements, access):
	width = max_length(elements)

	template = '{:>{width}}'

	print('\n'.join([
		'{}. '.format(i + 1)
		+ template.format(element, width=width)
		+ ' - access level: {}'.format(A[access[i]])
		for i, element in enumerate(elements)
	]))