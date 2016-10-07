def PrintHistogram(nums):
    # Prints the histogram for a list of numbers
    my_list = []

    # Add elements of nums to my_list
    for i in nums:
        if i not in my_list:
            my_list.append(i)

    # Print histogram
    for i in range(len(my_list)):
        print('%s: %s' % (str(my_list[i]), '*' * nums.count(my_list[i])))


PrintHistogram([-2, -2, -3, -2])
PrintHistogram([1, 2.5, 3, 4, 4, 3, 6])
