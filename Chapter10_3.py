# Python for Beginners Immersion Course
# Exercise 10.3
# Albert Molina
# 20-May-2018
# Description :  This program counts the distribution of the hour of the day for each of the messages. 
#    You can pull the hour from the "From" line by finding the time string and then splitting that string into parts using the colon character. 
#    Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.


try :
	InpFile = input('Enter filename : ')
	FileHandler = open(InpFile)
except :
	print('Please input valid filename')
	exit()

FileDict = dict()

for line in FileHandler :
	LineTup = line.lower()
	for Char in LineTup :
		if Char >= 'a' and Char <= 'z' :
			FileDict[Char] = FileDict.get(Char, 0) + 1

# Using tupples and list, print the 
NewLstTup= sorted( [(key, val) for key, val in FileDict.items()]) 
for key, val in NewLstTup :
	print(key + '  ' + str(val))

