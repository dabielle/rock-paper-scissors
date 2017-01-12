#Rock Paper Scissors


while True:
	playerOne = input('Choose your weapon: 1 = rock, 2 = paper, 3 = scissors: ')
	playerTwo = input('Choose your weapon: 1 = rock, 2 = paper, 3 = scissors: ')
	if int(playerOne) == int(playerTwo): print('Draw')
	elif int(playerOne) == 1:
		if int(playerTwo) == 3:
			print('Player One wins')
		elif int(playerTwo) == 2:
			print('Player Two wins')
	elif int(playerOne) == 2:		
		if int(playerTwo) == 1:
			print('Player One wins')
		elif int(playerTwo) == 3:
			print('Player Two wins')
	elif int(playerOne) == 3:		
		if int(playerTwo) == 1:
			print('Player Two wins')
		elif int(playerTwo) == 2:
			print('Player One wins')
	else:
		print('incorrect number')
	usr_command = input("Continue: 1, Quit = 2: ")
	if int(usr_command) == 2:
		print('Thank You for Playing')
		break
	elif int(usr_command) != 1 or int(usr_command) != 2:
		print('Incorrect number, Try again')
		usr_command = input("Continue: 1, Quit = 2: ")