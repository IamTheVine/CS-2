# Python for Beginners Immersion Course
# Checkpoint 2
# Albert Molina
# 20-May-2018
# Description :  Write a Python program to guess a number between 1 to 9. Note : User is prompted to enter a guess. 
#  If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, 
#  Write a Python program to guess a number between 1 to 9. Note : User is prompted to enter a guess. rt
#  user will get a "Well guessed!" message, and the program will exit. Hint: Use the random function. 


from random import *

try: 
	while True :
		InpNum = input('Input any number from 1 to 9 : ')
		if InpNum == '0' :
			exit()
		InpNum = int(InpNum)
		RandNum = randint(1,9)

		if InpNum == RandNum :
			print('Well guessed!')
		else :
			print('Random number is ' + str(RandNum))

except :
	print('Please valid number')
	exit()

