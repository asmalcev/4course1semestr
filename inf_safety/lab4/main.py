from access import (
	O as Objects,
	OV as ObjectsAccessLevels,
	U as Users,
	UV as UsersAccessLevels,
	print_vector,
)

print('Objects access levels:')
print_vector(Objects, ObjectsAccessLevels)

print('\nUsers access levels:')
print_vector(Users, UsersAccessLevels)


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

def print_user_objects(objects, objects_access_levels, user_access_level):
	print('Available objects:')
	for i, obj in enumerate(objects):
		if user_access_level <= objects_access_levels[i]:
			print('{}. {}'.format(
				i + 1,
				obj
			))

print_user_objects(Objects, ObjectsAccessLevels, UsersAccessLevels[userid])


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
		print_user_objects(Objects, ObjectsAccessLevels, UsersAccessLevels[userid])
	elif cmd == 'request':
		obj = input('choose object (input id) 📃: ')

		try:
			obj = int(obj) - 1

			if obj in range(0, len(Objects)):
				if ObjectsAccessLevels[obj] >= UsersAccessLevels[userid]:
					print('✅ Success!')
				else:
					print('You haven\'t enough rights for this action 😥')
			else:
				print('Couldn\'t find given object 😥')
		except:
			print('An invalid object id was specified')

	else:
		print('Unknown command')