# Python for Beginners Immersion Course
# Exercise 7.1
# Albert Molina
# 29-Apr-2018

fhand = open('mbox-short.txt','r')
LineCount = 0
LineProcessed = 0
for line in fhand :
	LineCount = LineCount + 1
	if line != '\n' :
		LineProcessed = LineProcessed + 1
		print(line.upper())

print('Process completed')
print('Total Lines : ' + str(LineCount))
print('Total Lines Processed: ' + str(LineProcessed))