def GetNextDate(day, month, year, num_days_forward):
    # Return next date as a str.



    while (num_days_forward != 0):
        if (num_days_forward > 0): #Where the days need to be subtracted
            day = day + 1
            num_days_forward = num_days_forward - 1

            maxDay = 28
    
            if (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12):
                maxDay = 31
            elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
                maxDay == 30
            elif (month == 2):
                con1 = year % 4
                con2 = year % 100
                con3 = year % 400
                if ((con1 == 0) and (con2 != 0) or (con3 == 0)):
                    maxDay == 29
                else:
                    maxDay == 28
            if (day > maxDay):
                day = 1
                month = (month + 1)
            if (month > 12):
                month = month - 12
                year = year + 1




                
        if (num_days_forward < 0): #Where the days need to be added
            day = day - 1
            num_days_forward = num_days_forward + 1
            if (day == 0):
                
                month = month - 1
                
                if (month == 0):
                    month = 12
                    year = year - 1

                    
                if (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12):
                     day = 31
                elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
                    day = 30
                elif (month == 2):
                    con1 = year % 4
                    con2 = year % 100
                    con3 = year % 400
                    if ((con1 == 0) and (con2 != 0) or (con3 == 0)):
                        day = 29
                    else:
                        day = 28               
        
        
        

    return str(day) + '/' + str(month) + '/' + str(year)

print(GetNextDate(16, 9, 2016, 10))# -> ‘9/26/2016’
print(GetNextDate(31, 12, 2016, 40))# -> ‘2/9/2017’
print(GetNextDate(28, 2, 2004, -800))# -> ‘12/20/2001’
               
'''
    

   

    return str(day) + '/' + str(month) + '/' + str(year)

print(GetNextDate(16, 9, 2016))
print(GetNextDate(31, 12, 2016))
print(GetNextDate(28, 2, 2004))
'''
