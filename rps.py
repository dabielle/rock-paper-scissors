#Rock Paper Scissors
import random
wList = ['rock', 'paper', 'scissors']

playerNum = input('Please input number of players(max 2): ')

while True: 
	if int(playerNum) == 2:

	
		playerOne = input('Player One - Choose your weapon: rock, paper or scissors: ')
		playerTwo = input('Player Two - Choose your weapon: rock, paper or scissors: ')
		if playerOne.casefold() == playerTwo.casefold(): print('Draw')
		elif playerOne.casefold() == 'rock':
			if playerTwo.casefold() == 'scissors':
				print('Player One wins')
			elif playerTwo.casefold() == 'paper':
				print('Player Two wins')
		elif playerOne.casefold() == 'paper':		
			if playerTwo.casefold() == 'rock':
				print('Player One wins')
			elif playerTwo.casefold() == 'scissors':
				print('Player Two wins')
		elif playerOne.casefold() == 'scissors':		
			if playerTwo.casefold() == 'rock':
				print('Player Two wins')
			elif playerTwo.casefold() == 'paper':
				print('Player One wins')
		else:
			print('Unknown Weapon, Try again.')
		#play again option
		usr_command = input("Please type 'Continue' to play again or 'Quit' to exit: ")
		if usr_command.casefold() == 'quit':
			print('Thank You for Playing')
			break
		elif usr_command.casefold() != 'quit' and usr_command.casefold() != 'continue':
			print('Incorrect , Try again')
			usr_command = input("Please type 'Continue' to play again or 'Quit' to exit: ")

	elif int(playerNum) == 1:
	
		playerOne = input('Player One - Choose your weapon: rock, paper or scissors: ')
		playerTwo = random.choice(wList)
		print('The Computer chose ' + playerTwo + ' as their Weapon')
		if playerOne.casefold() == playerTwo.casefold(): print('Draw')
		elif playerOne.casefold() == 'rock':
			if playerTwo.casefold() == 'scissors':
				print('Player One wins')
			elif playerTwo.casefold() == 'paper':
				print('Player Two wins')
		elif playerOne.casefold() == 'paper':		
			if playerTwo.casefold() == 'rock':
				print('Player One wins')
			elif playerTwo.casefold() == 'scissors':
				print('Player Two wins')
		elif playerOne.casefold() == 'scissors':		
			if playerTwo.casefold() == 'rock':
				print('Player Two wins')
			elif playerTwo.casefold() == 'paper':
				print('Player One wins')
		else:
			print('Unknown Weapon, Try again.')
		#play again option
		usr_command = input("Please type 'Continue' to play again or 'Quit' to exit: ")
		if usr_command.casefold() == 'quit':
			print('Thank You for Playing')
			break
		elif usr_command.casefold() != 'quit' and usr_command.casefold() != 'continue':
			print('Incorrect , Try again')
			usr_command = input("Please type 'Continue' to play again or 'Quit' to exit: ")
	elif int(playerNum) != 1 and int(playerNum) != 2:
		print('Incorrect number of players, Try again')
		playerNum = input('Please input number of players(max 2): ')
