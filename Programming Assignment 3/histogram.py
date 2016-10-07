def PrintHistogram(nums):
    # Prints the histogram for a list of numbers

    # Dictionary to hold each key (number) and value (number of occurences)
    numbers = { }

    # Iterate through all the values in the list
    for i in nums:

        # Increment the number of asterics for the corresponding value in the dictionary
        if i not in numbers:
            numbers[i] = '*'
        else:
            numbers[i] = numbers[i] + '*'

    # Print the histogram values
    for i in numbers:
        print('%s: %s' % (str(i), numbers[i]))

PrintHistogram([-2, -2, -3, -2])
PrintHistogram([1, 2.5, 3, 4, 4, 3, 6])
