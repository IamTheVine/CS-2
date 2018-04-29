# Python for Beginners Immersion Course
# Exercise 7.1
# Albert Molina
# 29-Apr-2018

InputFile = input('Enter the file name: ')
fhand = open(InputFile, 'r')

TextToFind = 'X-DSPAM-CONFIDENCE:'
LenText = len(TextToFind)
LenComp = 7 
SpamSum = float(0.0)
SpamCount = 0

for line in fhand :
	LineUpper = line.upper()
	TextFind = LineUpper.find(TextToFind)
	if TextFind > -1 :
		BegLocValue = TextFind+LenText
		EndLocValue = TextFind+LenText + LenComp
		SpamSum = SpamSum + float((line[BegLocValue : EndLocValue]))
		SpamCount = SpamCount + 1

print('Average spam confidence: ' + str(SpamSum / SpamCount))