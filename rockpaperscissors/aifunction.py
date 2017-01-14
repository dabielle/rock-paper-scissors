#rock paper scissors ai function
import random

def test_logic(playerOne, playerTwo):
	
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

