con = False
while con == False:
	print('Simple contact book ')
	print()
	print('1.Add contact')
	print('2.search contact')
	print('0.Exit')
	User = input()
	if User == '1':
		print()
		print('Add new contact')
		Name = input('Enter contact name: ')
		Phone = input('Enter contact phone: ')
		print()
		print('Saved successfully!')
		print('Name = ' + Name)
		print('Phone = ' + Phone)
		print()
	elif User == '2':
			print()
			print('Search contact .........')
			search = input('Enter contact name or phone: ')
			if search == Name or search == Phone:
				print()
				print('View ...')
				print('Name = ' + Name)
				print('Phone = ' + Phone)
			else:
				print()
				print('No contact found yet ! ')
	if User == '0':
		con = True