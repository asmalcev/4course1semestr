import math
import random
from operator import mul
from functools import reduce

random.seed(2364791)


def read_N():
	N = None
	while not N:
		try:
			N = int(input('Input N: '))
			return N
		except:
			print('Wrong input. N is integer')

def get_random_int_in_range(min, max):
	return math.trunc( random.random() * max ) + min

crows = ccolumns = 4
def generate_matrix(n = 10):
	return [
		[get_random_int_in_range(-2, n * 2) for i in range(ccolumns)]
		for j in range(crows)
	]

def print_matrix(m):
	print('\n'.join(map(lambda row: ' '.join(map(str, row)), m)))

def update_matrix(matrix):
	geometric_mean = pow(reduce(mul, [matrix[i][i] for i in range(crows)]), 1 / crows)

	secondary_diagonal = [matrix[i][crows - i - 1] for i in range(crows)]
	index_of_max = secondary_diagonal.index(max(secondary_diagonal))

	matrix[index_of_max][crows - index_of_max - 1] = geometric_mean

	for i in range(crows):
		for j in range(ccolumns):
			if not (i == index_of_max and j == crows - index_of_max - 1) and matrix[i][j] > 0:
				matrix[i][j] = 0



N = read_N()

matrix = generate_matrix(N)
print_matrix(matrix)
update_matrix(matrix)
print('\nUpdated matrix')
print_matrix(matrix)

print('\nNew matrix with std. value (10)')
matrix = generate_matrix()
print_matrix(matrix)
update_matrix(matrix)
print('\nUpdated matrix')
print_matrix(matrix)