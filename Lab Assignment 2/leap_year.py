def isLeapYear(year):
    con1 = year % 4
    con2 = year % 100
    con3 = year % 400
    if ((con1 == 0) and (con2 != 0) or (con3 == 0)):
        return True
    else:
        return False

print(isLeapYear(307))
print(isLeapYear(2200))
print(isLeapYear(2000))
print(isLeapYear(1800))
print(isLeapYear(3696))
