#!/usr/bin/env python
# Exercise 1  
# the program generates a random number with number of digits equal to length. 
# If the command line argument length is not provided, the default value is 1. 
# Then, the program prompts the user to type in a guess, 
# informing the user of the number of digits expected. 
# The program will then read the user input, and provide basic feedback to the user. 
# If the guess is correct, the program will print a congratulatory message with 
# the number of guesses made and terminate the game. 
# Otherwise, the program will print a message asking the user to guess a higher or lower number, 
# and prompt the user to type in the next guess.
########################

import random
import sys


'''
get a length of number from the comand line
if no number, length = 1

create a number that has the right # of digits

have the user guess a number, telling them the length of that number

if correct:
	print congratulatory message and state number of guesses made
elif too low:
	have them guess again and tell them it was too low
else to high:
	have them guess again and tell them it was too high
'''

def set_length():
	'''Set the length of the computer generated number to the number set by the user
	 or to one, if not set
	 '''
	user_length = len(sys.argv[1])
	if user_length < 1:
		user_length = 1
		return user_length
	else:
		return user_length

def create_random():
	'''Generate random number
	'''
	computer_num = random.randint(1, 50)
	return computer_num


def get_user_num():	
	'''Get the user's first guess and succeeding guesses if needed
	'''
	user_number = raw_input("Guess a ?? digit number: ")
	try:
		user_guess = int(user_number)
	except: 
		user_guess = raw_input("Try again: ")
		return get_user_num()		
	else:
		return user_guess


def test_numbers():
	computer_num = create_random()
	guesses = 1
	while True:
		user_guess = get_user_num()
		if user_guess == computer_num:
			print("Great job you got the number right in " + str(guesses) + " tries.")
			break
		else:
			if user_guess < computer_num:
				print("Your number is too low.")
			else:
				print("Your number was too high")	
		guesses = guesses + 1





##############################################################################
def main():  # DO NOT CHANGE BELOW
	test_numbers()


if __name__ == '__main__':
    main()