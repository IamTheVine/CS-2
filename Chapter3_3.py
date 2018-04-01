# Python for Beginners Immersion Course
# Exercise 3.3
# Albert Molina
# 2-Apr-2018


try :
	Score = float(input('Enter score: '))
	if Score >= 0.9 :
		print('A')
	elif Score >= 0.8 :
		print('B')
	elif Score >= 0.7 :
		print('C')
	elif Score >= 0.6 :
		print('D')
	else :
		print('F')

except :
	print('Bad score')

