# Python for Beginners Immersion Course
# Checkpoint 1.9
# Albert Molina
# 24-May-2018
# Description : Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, 
#   return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" 
#   and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".


# Global variables
WeekDaysAlarm = 7
WeekEndAlarm =  10
WeekDaysAlarmHol = 10
WeekEndAlarmHol = 0

# User define function for stipping and converting to uppercase
def StringClean(usrString) :
	cleanString = usrString.strip()
	cleanString = cleanString.upper()
	return cleanString 

# try :
InpDOW = int(input("Input Day of the Week (0-Sun, 1-Mon, 2-Tue, 3-Wed, 4-Thu, 5-Fri, 6-Sat): "))
InpHoliday = StringClean(input("Is Holiday today? (Y/N) : "))
#  except :
#print('Please input valid number')
#quit()


# Checking if DOW and Holiday alarm
if InpDOW == 0 or InpDOW == 6 :
	AlarmHr = WeekEndAlarm
	if InpHoliday == 'Y' :
		AlarmHr = WeekEndAlarmHol
else :
	AlarmHr = WeekDaysAlarm
	if InpHoliday == 'Y' :
		AlarmHr = WeekDaysAlarmHol

print('Alarm is ' + str(AlarmHr) )