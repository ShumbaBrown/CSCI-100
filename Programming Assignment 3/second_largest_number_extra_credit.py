def GetNthLargestNumber(nums, n):
    # Returns the nth largest unique number in nums.
    largest = -999
    nth_largest = -999
    numbers = []
    i = 0

    # Check if n is valid
    if (n <= len(nums)):
        # Add elements of nums to numbers if that element isnt already present
        for j in nums:
            if j not in numbers:
                numbers.append(j)

        # Sort the list in descending order
        numbers.sort(reverse = True)

        # print the nth number in the sorted list
        if (n <= len(numbers)):
            print(numbers[n - 1])
        else:
            print('None')
                
    else:
        print('None')
                
               
GetNthLargestNumber([2, 4, 6, 5, 3, 1, 5, 4], 1) 
GetNthLargestNumber([2, 4, 6, 5, 3, 1, 5, 4], 2) 
GetNthLargestNumber([2, 4, 6, 5, 3, 1, 5, 4], 3) 
GetNthLargestNumber([2, 4, 6, 5, 3, 1, 5, 4], 10) 
GetNthLargestNumber([], 1)

