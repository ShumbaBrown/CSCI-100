def PrintMultiplicationTable(num_1, num_2):
    # Prints the multiplication table for num_1 x num_2
    
    for i in range(num_1):
        for j in range(num_2):
            print('%d * %d = %d' % (i + 1, j + 1, (i + 1) * (j + 1)))

PrintMultiplicationTable(2,4)
PrintMultiplicationTable(3,1)
