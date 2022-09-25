def dist(x1, y1, x2, y2):
	return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def print_computed_dists(x_b = 0, y_b = 0, x_e = 0, y_e = 0, *other):
	points = [(x_b, y_b), (x_e, y_e)]

	for i in range(0, len(other), 2):
		if i + 1 < len(other):
			points.append((other[i], other[i + 1]))

	for i in range(len(points)):
		for j in range(i + 1, len(points)):
			print('dist between points {} and {} equals {}'.format(points[i], points[j], dist(*points[i], *points[j])))


TESTS = [
	(1, 2, 3, 4, 5, 6, 7),
	(1, 2, 3),
	(4, 2, 8, 0, -3, -3, -3, -3),
	(),
]

i = 1
for test in TESTS:
	print('\nTest {}: {}'.format(i, test))
	i += 1
	print_computed_dists(*test)