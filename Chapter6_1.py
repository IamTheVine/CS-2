# Python for Beginners Immersion Course
# Exercise 6.1
# Albert Molina
# 22-Apr-2018



StrConstant = "  X-DSPAM-Confidence:0.8475  "
StrStripped = StrConstant.strip()
FindChar = ":"


if not FindChar in StrStripped :
	print("Colon " + FindChar + "not found")
	quit()

ColonPos = StrStripped.find(FindChar)
StrToFloat= float(StrStripped[ColonPos+1:])
print(ColonPos)
print(StrToFloat)


# using replace()
StrReplaced = StrStripped.replace(FindChar,"$")
print("Replaced all : with $")
print(StrReplaced)

# Using Sub() function
StrLen = len(StrStripped)
print('String Length is :' + str(StrLen))



# StrUpper = StrConstant.upper()
# SubStrInp = input('Enter Substring:').upper()