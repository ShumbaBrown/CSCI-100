'''
CountPrimeNumbers returns the number of prime numbers in a given list.
'''
def CountPrimeNumbers(nums):
    # Initialize count to 0
    count = 0

    
    for i in nums:                  # Iterate through all the numbers in the list
        if (i > 1):                 # Check if the value is valid. It must be greater than 1
            prime = True            # Assign prime to True
            j = 2                   # Assign j to 2
            while j < i:            # Iterate through all the numbers less than i
                if (i % j == 0):    # If j is a factor of i then i is not prime
                    prime = False
                    break
                j += 1              # Increment j
                
            if (prime == True):     # If i is a prime number then increment the counter
                count += 1
                     

    return count

print(CountPrimeNumbers({4, 7, 8, 11, 17}))
print(CountPrimeNumbers({27281, 23547, 23549, 23551, 41661}))
print(CountPrimeNumbers({-3, -2, -1, 0, 1, 2, 3}))
print(CountPrimeNumbers({}))

        
