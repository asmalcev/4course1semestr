import math
import random
from operator import mul
from functools import reduce

random.seed(2364791)

N = None

while not N:
	try:
		N = int(input('Input N: '))
	except:
		print('Wrong input. N is integer')

crows = ccolumns = 4

def get_random_int_in_range(min, max):
	return math.trunc( random.random() * max ) + min

matrix = [
	[get_random_int_in_range(-2, N * 2) for i in range(ccolumns)]
	for j in range(crows)
]

def print_matrix(m):
	print('\n'.join(map(lambda row: ' '.join(map(str, row)), m)))

print_matrix(matrix)

geometric_mean = pow(reduce(mul, [matrix[i][i] for i in range(crows)]), 1 / crows)

secondary_diagonal = [matrix[i][crows - i - 1] for i in range(crows)]
index_of_max = secondary_diagonal.index(max(secondary_diagonal))

matrix[index_of_max][crows - index_of_max - 1] = geometric_mean

for i in range(crows):
	for j in range(ccolumns):
		if not (i == index_of_max and j == crows - index_of_max - 1) and matrix[i][j] > 0:
			matrix[i][j] = 0

print('\nUpdated matrix')
print_matrix(matrix)