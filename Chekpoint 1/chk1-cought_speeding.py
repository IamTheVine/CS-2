# Python for Beginners Immersion Course
# Checkpoint 1.8
# Albert Molina
# 10-May-2018
# Description : You are driving a little too fast, and a police officer stops you. Write code to compute the result, 
#  encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. 
#  If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, 
#  your speed can be 5 higher in all cases.


# Global Variables
BDaySpeed = 5
Ticket1from = 61
Ticket1to = 80


# User define function for stipping and converting to uppercase
def StringClean(usrString) :
	cleanString = usrString.strip()
	cleanString = cleanString.upper()
	return cleanString

try :
	InpSpeed = int(input('Input speed : '))
	InpBDay = input('Is your birthday today? (Y/N) :')
except :
	print('Please input valid number')
	quit()

# Birthday speed allowance 
InpBDay = StringClean(InpBDay)
if InpBDay == 'Y' :
	InpSpeed = InpSpeed - BDaySpeed

RecTicket = 'No ticket'
if InpSpeed > Ticket1to :
	RecTicket = 'Big ticket'
elif InpSpeed >= Ticket1from :
	RecTicket = 'Small ticket'

print('You received '+ RecTicket)
