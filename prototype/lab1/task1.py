def read_integers():
	integers = None

	while True:
		try:
			integers = [int(word) for word in input('Input 3+ integers: ').split(' ')]

			if len(integers) > 2:
				return integers
			else:
				print('Need 3+ integers')
		except:
			print('Wrong input. Input string must contain only integers')



integers = read_integers()
integers = integers[-3:]



def compare(int1, int2):
	return int1 - int2

def compute_triangle_type(sides):
	if sides[0] == sides[1] == sides[2]:
		return 'equilateral'
	if (
		compare(*sides[:2]) == 0 or
		compare(*sides[0::2]) == 0 or
		compare(*sides[1:]) == 0
	):
		return 'isosceles'

	square_of_max_side = pow(max(sides), 2)
	sum_of_squares_of_other_sides = sum( # sum of squares
			map(lambda side: pow(side, 2),
				filter(lambda side: side != max(sides), sides) # filter by not equals max side
			)
	)

	if square_of_max_side == sum_of_squares_of_other_sides:
		return 'rectangular'
	if square_of_max_side > sum_of_squares_of_other_sides:
		return 'obtuse'
	if square_of_max_side < sum_of_squares_of_other_sides:
		return 'acute-angled'

	return 'versatile'

def check_triangle(sides = [2, 2, 3]):
	if (
		sum(sides[:2]) > sides[2] and
		sum(sides[0::2]) > sides[1] and
		sum(sides[1:]) > sides[0]
	):
		print(sides, 'are sides of triangle.', end=' ')
		print('Triangle type is {}'.format(compute_triangle_type(sides)))
	else:
		print(sides, 'aren\'t sides of triangle')

check_triangle(integers)
check_triangle()