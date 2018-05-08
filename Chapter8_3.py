# Python for Beginners Immersion Course
# Exercise 8.2 and 8.3
# Albert Molina
# 08-May-2018
# Description : Printing day of the week (DOW) in email text file

DOWpos = 3
FileInp = input('Enter text file: ')
try :
	fhand = open(FileInp)
except :
	print('Filename '+ FileInp + ' not found')
	quit()

for line in fhand :
	words = line.split()
	if len(words) >= DOWpos and words[0] == 'From' :
		print(words[DOWpos-1]) 
