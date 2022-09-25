import random
import string
import math

products = {
	'apple': 10,
	'cucumber': 8,
	'tomato': 12,
	'water': 20,
	'juice': 16,
	'cabbage': 14,
	'chips': 30,
	'cookie': 25,
	'pumpkin': 35,
	'melon': 45,
	'watermelon': 45,
	'potate': 5,
	'fish': 136,
	'meat': 104,
}

def get_random_int_in_range(min, max):
	return math.trunc( random.random() * max ) + min

def add(
	name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)),
	cost = get_random_int_in_range(0, 1000)
):
	products[name] = cost


def command_add():
	product_name = input('Input product name: ')
	product_cost = None

	while not product_cost:
		try:
			product_cost = int(input('Input product cost: '))
		except:
			print('Wrong input. Product cost must be an integer')

	add(product_name, product_cost)


def run_product_list_cmd_client():
	while True:
		cmd = input('Input command: ')

		if cmd == 'help':
			CMDS = [
				'help - print all commands',
				'add - add product',
				'addr - add random',
				'compute - compute sum of all costs',
				'quit - quit the system'
			]
			print('\n'.join(CMDS))
		elif cmd == 'quit':
			print('See you soon!')
			break
		elif cmd == 'add':
			command_add()
		elif cmd == 'addr':
			add()
		elif cmd == 'compute':
			print('Sum of costs of all products =', sum(map(lambda product: products[product], products)))
		else:
			print('Unknown command')

run_product_list_cmd_client()