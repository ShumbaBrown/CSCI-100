def RoundNumToNearestMultiple(num, n):
    con1 = num // n
    con2 = con1 * n
    con3 = (con1 + 1) * n
    con4 = con3 - num
    con5 = num - con2

    if con5 < con4:
        return con2
    else:
        return con3


print(RoundNumToNearestMultiple(9, 2))
print(RoundNumToNearestMultiple(712, 25))
print(RoundNumToNearestMultiple(713, 25))
print(RoundNumToNearestMultiple(0, 5))
print(RoundNumToNearestMultiple(79, 1))

    
