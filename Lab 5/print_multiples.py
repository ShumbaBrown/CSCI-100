'''
PrintMultiples prints all the multiples of a number within a range.
'''
def PrintMultiples(start, end, multiple):
    # Create an empty list to hold the multiples
    multiples = [ ]

    # Check if the multiple is valid
    if (multiple <= 0):
        print('Input multiple must be greater than 0')
    else:
        # Ensure that start is less than end
        if (start >= end):
            temp = start
            start = end
            end = temp

        temp = start

        # Iterate through all the numbers in the range
        while (temp <= end):
            # Check if each number is a multiple 
            if (temp % multiple == 0):
                # Add each number that is a multiple to the lis
                multiples.append(temp)

            # Increment the number
            temp += 1

        # Check if the list is empty then print result
        if (len(multiples) == 0):
            print("There are no multiples of %d in the range %d to %d" % (multiple, start, end))
        else:
            print(multiples)

PrintMultiples(4, 10, 2)
PrintMultiples(7, -7, 3)
PrintMultiples(-6, -6, 1)
PrintMultiples(7, 10, 6)
PrintMultiples(1, 5, 0)
