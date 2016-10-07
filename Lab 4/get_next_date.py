def GetNextDate(day, month, year):
    # Return next date as a str.
    maxDay = 28
    
    if (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12):
        maxDay = 31
    elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
        maxDay == 30
    elif (month == 2):
        maxDay == 28

    day = day + 1
    if (day > maxDay):
        day = 1
        month = (month + 1)
        if (month > 12):
            month = month - 12
            year = year + 1

    return str(day) + '/' + str(month) + '/' + str(year)

print(GetNextDate(16, 9, 2016))
print(GetNextDate(31, 12, 2016))
print(GetNextDate(28, 2, 2004))
