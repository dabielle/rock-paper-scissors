#Rock Paper Scissors
import random
import aifunction
wList = ['rock', 'paper', 'scissors']
playerNum = input('Please input number of players(max 2): ')

while True: 
	usr_command = input('Would you like to continue or quit?(Type c or q): ')
	if usr_command.casefold() == 'q':
		print('Thanks for Playing')
		break
	elif usr_command.casefold() != 'q' and usr_command.casefold() != 'c':
		print('Incorrect , Try again')
	if int(playerNum) == 2:
		playerOne = input('Player One - Choose your weapon: rock, paper or scissors: ')
		playerTwo = input('Player Two - Choose your weapon: rock, paper or scissors: ')
		aifunction.test_logic(playerOne, playerTwo)

	elif int(playerNum) == 1:
		playerOne = input('Player One - Choose your weapon: rock, paper or scissors: ')
		playerTwo = random.choice(wList)
		print('The Computer chose ' + playerTwo + ' as their Weapon')
		aifunction.test_logic(playerOne, playerTwo)
		
	elif playerNum.input != 1 and playerNum.input != 2:
		print('Incorrect number of players, Try again')
		playerNum = input('Please input number of players(max 2): ')