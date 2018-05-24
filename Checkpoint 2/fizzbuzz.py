# Python for Beginners Immersion Course
# Checkpoint 2
# Albert Molina
# 25-May-2018
# Description :  Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number 
#  and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

# Global Variables declaration
NumMax = 50
Multiple1 = 3
Multiple2 = 5

Ctr = 0
while Ctr <= 50 :
	MultMsg = str(Ctr)
	IndMult1 = 0
	if (Ctr % Multiple1) == 0 :
		MultMsg = 'Fizz'
		IndMult1 = 1
	if (Ctr % Multiple2) == 0 :
		if IndMult1 == 1 :
			MultMsg = MultMsg + 'Buzz'
		else :
			MultMsg = 'Buzz'
	print(MultMsg)
	Ctr = Ctr + 1

