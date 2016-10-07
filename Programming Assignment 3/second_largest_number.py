def GetSecondLargestNumber(nums):
    # Returns the second largest unique number in nums
    largest = -999
    second_largest = -999
    numbers = []
    for i in nums:
        if i not in numbers:
            numbers.append(i)
            if (i > largest):
                second_largest = largest
                largest = i
            elif (i >= second_largest and i != largest):
                second_largest = i
            
                    
    if (len(numbers) >= 2):
        return second_largest
    else:
        return 'None'


print(GetSecondLargestNumber([2, 4, 6, 5, 3, 1])) #-> 5
print(GetSecondLargestNumber([-2, 0, 2])) #-> 0
print(GetSecondLargestNumber([-2, -2, -2])) #-> None
print(GetSecondLargestNumber([-2, -2, -3, -2])) #-> -3
print(GetSecondLargestNumber([1])) #-> None
print(GetSecondLargestNumber([])) #-> None
    
