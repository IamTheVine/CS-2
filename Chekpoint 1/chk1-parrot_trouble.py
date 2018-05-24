# Python for Beginners Immersion Course
# Checkpoint 1.6
# Albert Molina
# 10-May-2018
# Description : We have a loud talking parrot. The "hour" input is the current hour time in the range 0..23. 
#     We are in trouble if the parrot is talking(input True if talking and False if not) and the hour is before 7 or after 20. Return True if we are in trouble.
#         

# Global variables
ParrotTalkAM = 7
ParrotTalkPM = 20

# User define function for stipping and converting to uppercase
def StringClean(usrString) :
	cleanString = usrString.strip()
	cleanString = cleanString.upper()
	return cleanString 

try :
	InpParrotTalk = input('Is the Parrot talking (Y/N)? : ')
	InpHour = int(input('What is the time now (hour only 0 - 23) : '))
except :
	print('Please input valid number')
	quit()

InpParrotTalk = StringClean(InpParrotTalk)
if not (InpParrotTalk == 'Y' or InpParrotTalk == 'N') :
	print('Invalid answer, pease input Y or N')
	QuitVal = True

if InpHour > 23 or InpHour < 0 :
	print('Invalid hour value, input 0 to 23 only')
	QuitVal = True

if QuitVal :
	quit()
	
if InpParrotTalk == 'Y' and (InpHour < ParrotTalkAM or InpHour > ParrotTalkPM) :
	print('True - We are in Trouble!')
else :
	print('False - Nothig to worry')
