'''
PrintPrimeFactors prints all the prime factors of a number.
'''
def PrintPrimeFactors(num):
    # If input less than 2 print there are no prime factors
    if (num < 2):
        print('There are no prime factors for %d' % (num))
    
    else:
        # List to store all the prime factors
        factors = []

        # Variable to handle all prime numbers
        i = 2

        # Check for prime numbers and append them to the list
        while (i <= num):
            if (num % i == 0):
                factors.append(i)
                num = num / i
                i = 2
            else:
               i = i + 1 + i % 2

        # Print the first item in the list
        print('%d' % (factors[0]), end = '')

        # Print remaining items i the list
        j = 1
        while (j < len(factors)):
            print(' * %d' % (factors[j]), end = '')
            j += 1
        print('\n')
        
PrintPrimeFactors(1)
PrintPrimeFactors(2)
PrintPrimeFactors(10)
PrintPrimeFactors(11)
PrintPrimeFactors(24)

