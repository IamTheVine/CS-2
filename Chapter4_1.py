# Python for Beginners Immersion Course
# Exercise 4.1 
# Albert Molina
# 12-Apr-2018


def computepay(Hours, Rate) :
	Hours = float(Hours)
	Rate = float(Rate)
	Above40 = 0
	if Hours > 40 :
		Above40 = Hours - 40
		Hours = 40
	Pay = float((Hours * Rate) + (Above40 * Rate * 1.5))
	return Pay

try :	
	HoursInp = input('Enter Hours: ')
	RateInp = input('Enter Rate: ')
	PayTotal = computepay(HoursInp, RateInp)
	print('Pay: ' + str(PayTotal))

except:
	print('please enter numeric input')
