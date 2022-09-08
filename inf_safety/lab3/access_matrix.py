import random
import math

random.seed(872352)

c_O = 4 # count of objects
c_U = 6 # count of users
c_S = 8 # count of levels

O = ['report.pdf', 'main.cpp', 'order.doc', 'kitty.png'] # objects
U = ['Ivan', 'Alexey', 'Oleg', 'Dmitriy', 'George', 'Xi Jinping'] # users

S = {
	0: { 'bin': '000', 'access': ['ban'] },
	1: { 'bin': '001', 'access': ['grant'] },
	2: { 'bin': '010', 'access': ['write'] },
	3: { 'bin': '011', 'access': ['write', 'grant'] },
	4: { 'bin': '100', 'access': ['read'] },
	5: { 'bin': '101', 'access': ['read', 'grant'] },
	6: { 'bin': '110', 'access': ['write', 'read'] },
	7: { 'bin': '111', 'access': ['write', 'read', 'grant'] },
}


def get_random_int_in_range(min, max):
	return math.trunc( random.random() * max ) + min


adminid = get_random_int_in_range(0, c_U)


matrix = [
	[
		(
			S[7]['bin'] # full access if admin
			if i == adminid
			else S[get_random_int_in_range(0, c_S)]['bin'] # else random level
		) for j in range(c_O)
	] # columns
	for i in range(c_U)
] # rows

def max_length(l):
	return max(map(lambda x: len(x), l))

def print_access_matrix(m, rows, columns):
	row_length = max_length(rows)
	column_length = max_length(columns)

	template = '{:>{width}}'

	def column_format(cell):
		return template.format(cell, width=column_length)

	def row_format(cell):
		return template.format(cell, width=row_length)


	print(' ' * row_length, ' '.join(map(
		column_format,
		columns
	)))

	print('\n'.join([
		'{} {}'.format(
			row_format(rows[i]),
			" ".join( map(column_format, row) )
		) for i, row in enumerate(m)
	]))

def get_level_by_bin(code):
	for level in S:
		if S[level]['bin'] == code:
			return (level, S[level])