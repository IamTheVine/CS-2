# Python for Beginners Immersion Course
# Checkpoint 1.2
# Albert Molina
# 10-May-2018
# Description : Write a program to accept the temperature value and to tell a person to bring heavy jacket if temperature is < 20, 
#     if temperature is between 20 and 30, bring light jacket. if temperature > 30, do not bring any jacket.



# Initiating global variables. So as not to hard code the numbers in the program.
HeavyJacketTemp = 20.0
LightJacketTemp = 30.0
# ---

try :
	InpTemp = float(input('Input Temperature: '))
except :
	# Error trapping, in case the user inputted an invalid number.
	print('Please input valid number')
	quit()

# Verify the temperature and recommend what kind of jacket to bring
if InpTemp < HeavyJacketTemp :
	print('Bring Heavy jacket')
elif InpTemp <= LightJacketTemp :
	print('Bring Light jacket')
else :
	print('Weather is good')
