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


def add():
	product_name = input('Input product name: ')
	product_cost = None

	while not product_cost:
		try:
			product_cost = int(input('Input product cost: '))
		except:
			print('Wrong input. Product cost must be an integer')

	products[product_name] = product_cost


while True:
	cmd = input('Input command: ')

	if cmd == 'help':
		CMDS = [
			'help - print all commands',
			'add - add product',
			'compute - compute sum of all costs',
			'quit - quit the system'
		]
		print('\n'.join(CMDS))
	elif cmd == 'quit':
		print('See you soon!')
		break
	elif cmd == 'add':
		add()
	elif cmd == 'compute':
		print('Sum of costs of all products =', sum(map(lambda product: products[product], products)))
	else:
		print('Unknown command')
