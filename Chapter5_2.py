# Python for Beginners Immersion Course
# Exercise 5.1
# Albert Molina
# 16-Apr-2018



NumCtr = 0
NumSum = 0
NumAvg = 0
NumMax = None
NumMin = None

while True :
	NumEnter = input('Enter a number: ')

	if NumEnter == "done" :
		break

	try :
		NumInput = float(NumEnter) 
		NumSum = NumSum + NumInput
		
		if NumMax == None :
			NumMax = NumInput
			NumMin = NumInput

		if NumMax < NumInput :
			NumMax = NumInput 

		if NumMin > NumInput :
			NumMin = NumInput 
		NumCtr = NumCtr + 1

	except :
		print('Invalid Input')

print('Total : ', NumSum)
print('Count : ', NumCtr)
print('Average:', NumSum / NumCtr)
print('Maximum: ', NumMax)
print('Minimum: ', NumMin)