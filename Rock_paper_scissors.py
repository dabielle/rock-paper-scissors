#Rock Paper Scissors

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