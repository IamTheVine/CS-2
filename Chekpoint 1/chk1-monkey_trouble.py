# Python for Beginners Immersion Course
# Checkpoint 1.4
# Albert Molina
# 10-May-2018
# Description : We have two monkeys, a and b. Accept the input telling if each is smiling. 
#     We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
#         


InpMonkey1 = input('Is Monkey 1 smiling? (Y/N)')
InpMonkey2 = input('Is Monkey 2 smiling? (Y/N)')


# strip and convert the inputted value to upper case. User may input lower case.
InpMonkey1 = InpMonkey1.upper()
InpMonkey1 = InpMonkey1.strip()
InpMonkey2 = InpMonkey2.upper()
InpMonkey2 = InpMonkey2.strip()

# Verify the inputted value, it should only bee Y or N
InvalidInp = False
if not (InpMonkey1 == 'Y' or InpMonkey1 == 'N') :
	print('Invalid answer on Monkey 1, please input Y or N')
	InvalidInp = True
if not (InpMonkey2 == 'Y' or InpMonkey2 == 'N') :
	print('Invalid answer on Monkey 2, please input Y or N')
	InvalidInp = True

if InvalidInp :
	quit ()

# Execute and display the result
if InpMonkey1 == InpMonkey2 :
	print('True - You are in trouble')
else :
	print('False - All good, nothing to worry :)')
