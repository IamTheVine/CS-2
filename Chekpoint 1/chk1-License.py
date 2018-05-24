# Python for Beginners Immersion Course
# Checkpoint 1
# Albert Molina
# 10-May-2018
# Description : Write a python program simulating driver's license provision. Accept the age of the driver and his total number of practice hours. 
#      If driver’s age is below 16, do not issue license. if 16 or above then check if number of practice hours is more than(ie. >) 200. 
#      if > 200, issue license otherwise don’t.


# Initiating global variables. So as not to hard code the numbers in the program.
AgeMin = 16.0
PracticeHours = 200.0
# 

try :
	InpAge = float(input('Input Age of the Driver: '))
	InpHrPractice = float(input('Input hours practice: '))
except :
	# Error trapping, in case the user inputted an invalid number.
	print('Please input valid number')
	quit()

# Check the age and practice hours
if InpAge >= AgeMin and InpHrPractice >= PracticeHours :
	print('Congratulation! License will be issued')
else :
	print("Sorry, you didn't pass the criteria")