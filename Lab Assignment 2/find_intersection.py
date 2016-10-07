def GetIntersectionSize(range_1_min, range_1_max, range_2_min, range_2_max):
    '''
    This function should return the intersection size of the two ranges.
    Replace the line below with the correct code.
    '''
    if (range_1_min > range_2_min):
        bottom = range_1_min
    else:
        bottom = range_2_min

    if (range_1_max < range_2_max):
        top = range_1_max
    else:
        top = range_2_max

    return top - bottom


# You don't need to change anything below this line.
range_1_min = int(input('Enter the min number for range 1: '))
range_1_max = int(input('Enter the max number for range 1: '))
range_2_min = int(input('Enter the min number for range 2: '))
range_2_max = int(input('Enter the max number for range 2: '))


intersection_size = GetIntersectionSize(
    range_1_min, range_1_max, range_2_min, range_2_max)
print('The intersection size is', intersection_size)
