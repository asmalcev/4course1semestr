import random
import math

def merge(l1, l2):
	l1len = len(l1)
	l2len = len(l2)

	result = []

	i = j = 0
	while i < l1len and j < l2len:
		if l1[i] > l2[j]:
			result.append(l2[j])
			j += 1
		else:
			result.append(l1[i])
			i += 1

	while i < l1len:
		result.append(l1[i])
		i += 1

	while j < l2len:
		result.append(l2[j])
		j += 1

	return result

def merge_sort(l):
	llen = len(l)

	if llen <= 1:
		return l

	lpart = merge_sort(l[:llen // 2])
	rpart = merge_sort(l[llen // 2:])

	return merge(lpart, rpart)


TESTS = [
	([3, 2, 1], [1, 2, 3]),
	([328, 1278, 783, 27, 3, 56, 6], [3, 6, 27, 56, 328, 783, 1278]),
	([], []),
	([4], [4]),
	([-3, -2, -1, 4], [-3, -2, -1, 4]),
]


def get_random_int_in_range(min, max):
	return math.trunc( random.random() * max ) + min

def generate_random_test():
	test_len = get_random_int_in_range(0, 200)

	test = []
	for i in range(test_len):
		test.append(get_random_int_in_range(-1000, 1000))

	TESTS.append((test, sorted(test)))

for i in range(50):
	generate_random_test()


def list_equals(l1, l2):
	if not len(l1) == len(l2):
		return False

	for i in range(len(l1)):
		if not l1[i] == l2[i]:
			return False

	return True

i = 1
for test in TESTS:
	sort_result = merge_sort(test[0])
	test_result = list_equals(test[1], sort_result)

	print('Test {}:'.format(i), end=' ')
	if test_result:
		print('passed')
		i += 1
	else:
		print('failed\nresult: {}\nexpected: {}'.format(sort_result, test[1]))
		break
