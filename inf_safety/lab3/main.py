from access_matrix import (
	O as Objects, c_O,
	U as Users, c_U,
	matrix as access_matrix,
	print_access_matrix,
	get_level_by_bin,
	adminid
)


print('\n✨ System started ✨\n')

def login():
	username = input('Enter username: ')
	userid = -1
	try:
		userid = Users.index(username)
	except:
		while userid == -1:
			print('Incorrect username: There is no user with name "{}" 😥'.format(username))
			username = input('Enter username: ')
			try:
				userid = Users.index(username)
			except:
				pass

	return (username, userid)

username, userid = login()

print('\n✅ Success! You are welcome! 💻\n')



def print_user_objects(objects, userid, matrix):
	for i, obj in enumerate(objects):
		print('{}. {} - access: {}'.format(
			i + 1,
			obj,
			get_level_by_bin(matrix[userid][i])[1]['access']
		))

print_user_objects(Objects, userid, access_matrix)

CMDS = {
	'help': 'print all available commands',
	'grant': 'grant another user with your rights to file',
	'read': 'read file',
	'write': 'write to file',
	'quit': 'quit the user',
	'exit': 'exit the system',
	'accessmatrix': 'print access matrix ❗❗❗ only for admin ❗❗❗',
}


def read_obj(objects):
	obj = input('choose object (input id) 📃: ')

	try:
		obj = int(obj) - 1
		
		if obj in range(0, len(objects)):
			return obj
	except:
		pass

	return None


def read_person(users):
	person = input('choose user (input name) 😀: ')

	if person in users:
		return (person, users.index(person))

	return (None, -1)

def grant(access_giver, access_receiver):
	access = []
	for i in range(len(access_giver)):
		if access_giver[i] == '1':
			access.append('1')
		else:
			access.append(access_receiver[i])

	return ''.join(access)

#
# Commands
#
def cmd_grant():
	obj = read_obj(Objects)

	if obj:
		access = access_matrix[userid][obj]

		if access[2] != '1':
			print('You haven\'t enough rights for this action 😥')
			return

		person, personid = read_person(Users)

		if person:
			access_matrix[personid][obj] = grant(access, access_matrix[personid][obj])

			print('✅ Success! Rights were granted 🎁')
		else:
			print('Couldn\'t find given person 😥')
	else:
		print('Couldn\'t find given object 😥')

def cmd_help():
	for _cmd in CMDS:
		print('{} - {}'.format(_cmd, CMDS[_cmd]))

def cmd_read():
	obj = read_obj(Objects)

	if not obj is None:
		access = access_matrix[userid][obj]

		if access[0] == '1':
			print('✅ Success!')
		else:
			print('You haven\'t enough rights for this action 😥')

	else:
		print('Couldn\'t find given object 😥')

def cmd_write():
	obj = read_obj(Objects)

	if not obj is None:
		access = access_matrix[userid][obj]

		if access[1] == '1':
			print('✅ Success!')
		else:
			print('You haven\'t enough rights for this action 😥')
	else:
		print('Couldn\'t find given object 😥')

#
# main loop
#
while True:
	cmd = input('\nWaiting for your instructions 👀: ')

	if cmd == 'exit':
		print('See you soon! 👾')
		break
	elif cmd == 'quit':
		username, userid = login()
		print_user_objects(Objects, userid, access_matrix)
	elif cmd == 'help':
		cmd_help()
	elif cmd == 'grant':
		cmd_grant()
	elif cmd == 'read':
		cmd_read()
	elif cmd == 'write':
		cmd_write()
	elif cmd == 'accessmatrix':
		if userid == adminid:
			print_access_matrix(access_matrix, Users, Objects)
		else:
			print('You haven\'t enough rights for this action 😥')
	else:
		print('Unknown command. Use "help" command to get list of available commands 📜')