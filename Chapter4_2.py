# Python for Beginners Immersion Course
# Exercise 3.3
# Albert Molina
# 2-Apr-2018


""" This is line comment
asdfasd
asdfasdf
asdf
"""

def computegrade(pScore) :
	Score = float(pScore)
	if Score >= 0.9 :
		Grade = 'A'
	elif Score >= 0.8 :
		Grade = 'B'
	elif Score >= 0.7 :
		Grade = 'C'
	elif Score >= 0.6 :
		Grade = 'D'
	else :
		Grade = 'F'

	return Grade	


try :
	ScoreInp = input('Enter score: ')
	CompGrade = computegrade(ScoreInp)
	print('Grade: ', CompGrade)

except :
	print('Bad score')

