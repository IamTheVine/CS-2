# Python for Beginners Immersion Course
# Exercise 8.6
# Albert Molina
# 08-May-2018
# Description : max and min



NumList = list()

while True :
	NumInp = input('Enter a number: ')
	if NumInp.upper() == 'DONE' : break
	try :
		NumList.append(float(NumInp))
	except :
		print('   ' + NumInp + ' is not a number')

print('Maximum: ' + str(max(NumList)))
print('Minimum: ' + str(min(NumList)))
