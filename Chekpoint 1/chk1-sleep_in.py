# Python for Beginners Immersion Course
# Checkpoint 1.3
# Albert Molina
# 10-May-2018
# Description : Write a program to accept Weekday and Vacation values. Weekday is True if it is a weekday, and the vacation is True if we are on vacation. 
#          We sleep in if it is not a weekday or we're on vacation. DisplayTrue if we sleep in.
#         


# Initiating global variables. So as not to hard code the numbers in the program.
# Defining the 2 weekends or Dayoffs, 1-Sun, 2-Mon, 3-Tue, 4-Wed, 5-Thu, 6-Fri, 7-Sat 
DayOff1 = 1
DayOff2 = 7
# 

try :
	InpDOW = int(input('Input day of the week (1-Sun, 2-Mon, 3-Tue, 4-Wed, 5-Thu, 6-Fri, 7-Sat) '))
	InpHoliday = input('Are you on Holiday (Y/N)? ')
except ValueError :
	# Error trapping, in case the user inputted an invalid number.
	print('Please input valid value (1 to 7 only)')
	quit()

# Verify if the inputted DOW is from 1 to 7.
if InpDOW < 1 or InpDOW > 7 :
	print('Please input valid Day of the Week')
	quit()

# strip and convert the Holiday value to upper case. User may input lower case.
InpHoliday = InpHoliday.upper()
InpHoliday = InpHoliday.strip()

# verify, Holiday value should only be Y or N
if not (InpHoliday == 'Y' or InpHoliday == 'N') :
	print('Invalid Holiday, please input Y or N')
	quit ()

# From here, inputted values is clean and valid.

# Check if the inputted DOW is Weekend.
if InpDOW == DayOff1 or InpDOW == DayOff2  :
	FinalDayOff = True
else :
	FinalDayOff = False

if InpHoliday == 'Y' or FinalDayOff : 
	print('True, Sleep-in zzzzzz.')
else :
	print("Hey, wake-up! time to work")