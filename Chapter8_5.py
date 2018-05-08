# Python for Beginners Immersion Course
# Exercise 8.5
# Albert Molina
# 08-May-2018
# Description : Printing sender's email address

SenderPos = 2
FileInp = input('Enter text file: ')
try :
	fhand = open(FileInp)
except :
	print('Filename '+ FileInp + ' not found')
	quit()

for line in fhand :
	words = line.split()
	if len(words) >= SenderPos and words[0] == 'From' :
		print(words[SenderPos-1]) 
