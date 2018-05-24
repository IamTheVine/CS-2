# Python for Beginners Immersion Course
# Checkpoint 2
# Albert Molina
# 25-May-2018
# Description :  Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. Note : Use 'continue' statement.  Name the code. Expected Output : 0 1 2 4 5 


NumList = [0,1,2,3,4,5,6]

for Num in NumList :
	if Num == 3 or Num == 6 :
		continue
	else :
		print(Num)

		