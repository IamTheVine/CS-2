# Python for Beginners Immersion Course
# Exercise 8.1
# Albert Molina
# 07-May-2018

InpFile = input('Enter file: ')

try :
	FileHandler = open(InpFile)

except :
	quit()

WordList = list()

for line in FileHandler :
	SplitLine = line.split()
	for PerWord in SplitLine :
		if PerWord not in WordList : 
			WordList.append(PerWord)

WordList.sort()
print(WordList)