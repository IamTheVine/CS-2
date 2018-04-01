# Python for Beginners Immersion Course
# Exercise 3.1 and 3.2
# Albert Molina
# 2-Apr-2018


try :
	Hours = float(input('Enter Hours: '))
	Rate = float(input('Enter Rate: '))
	Above40 = 0
	if Hours > 40 :
		Above40 = Hours - 40
		Hours = 40
	Pay = float((Hours * Rate) + (Above40 * Rate * 1.5))
	print('Pay: ' + str(Pay))

except:
	print('please enter numeric input')