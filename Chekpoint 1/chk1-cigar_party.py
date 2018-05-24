# Python for Beginners Immersion Course
# Checkpoint 1.7
# Albert Molina
# 10-May-2018
# Description : When squirrels get together for a party, they like to have cigars. 
#   A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. 
#   Unless it is the weekend, in which case there is no upper bound on the number of cigars. 
#   Return True if the party with the given values is successful, or False otherwise.

# Global variables
CigarUpperVal = 60
CigarLowerVal = 40

# User define function for stipping and converting to uppercase
def StringClean(usrString) :
	cleanString = usrString.strip()
	cleanString = cleanString.upper()
	return cleanString 

try :
	InpCigarUsed = int(input('Input number of Cigars consumed : '))
	InpWeekEnd = input('Is weekend today (Y/N) ? : ')
except :
	print('Please input valid number')
	quit()

InpWeekEnd = StringClean(InpWeekEnd)
if not (InpWeekEnd == 'Y' or InpWeekEnd == 'N') :
	print('Invalid answer, pease input Y or N')
	quit()

if InpWeekEnd == 'Y' and InpCigarUsed >= CigarLowerVal :
	print('True - Party is successful')
elif InpWeekEnd == 'N' and InpCigarUsed >= CigarLowerVal and InpCigarUsed <= CigarUpperVal :
	print('True - Party is successful')
else :
	print('False - Party is NOT successful')
