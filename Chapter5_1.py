# Python for Beginners Immersion Course
# Exercise 5.1
# Albert Molina
# 16-Apr-2018



NumCtr = 0
NumSum = 0
NumAvg = 0

while True :
	NumInput = input('Enter a number: ')

	if NumInput == "done" :
		break

	try :
		NumSum = NumSum + float(NumInput)
		NumCtr = NumCtr + 1

	except :
		print('Invalid Input')

if NumCtr > 0 :
	NumAvg = NumSum / NumCtr

print('Total : ', NumSum)
print('Count : ', NumCtr)
print('Average:', NumAvg)
