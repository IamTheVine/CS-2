# Python for Beginners Immersion Course
# Exercise 7.1
# Albert Molina
# 29-Apr-2018

try :
	InputFile = input('Enter the file name: ')
	if InputFile.upper() == 'NA NA BOO BOO' :
		print("NA NA BOO BOO TO YOU - You have been punk'd!")
		exit()
	fhand = open(InputFile, 'r')
except FileNotFoundError:
	print('File cannot be opened: ' + InputFile)
	exit()

TextToFind = 'SUBJECT'
SubjectCount = 0

for line in fhand :
	LineUpper = line.upper()
	TextFind = LineUpper.find(TextToFind)
	if TextFind > -1 :
		SubjectCount = SubjectCount + 1

print('There were ' + str(SubjectCount) + ' subject lines in ' + InputFile)