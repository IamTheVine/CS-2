# Python for Beginners Immersion Course
# Checkpoint 1.5
# Albert Molina
# 10-May-2018
# Description : Given two int values, return their sum. Unless the two values are the same, then return double their sum.
#         

try :
	InpNumber1 = int(input('Input 1st Number: '))
	InpNumber2 = int(input('Input 2nd Number: '))
except :
	print('Please input valid number')

SumNumbers = InpNumber1 + InpNumber2

if InpNumber1 == InpNumber2 :
	SumNumbers = 2 * SumNumbers

print('Result : ' + str(SumNumbers))