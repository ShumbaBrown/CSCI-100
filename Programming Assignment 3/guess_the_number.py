def GuessTheNumber(mystery_num):
    # Continually ask the user for guesses until they guess correctly.

    # Variable to store the number of guesses
    guesses = 0

    # loop continually ask the user for a guess until it is correct
    while (True):
        # Prompt the user of a guess
        guess = int(input('Enter a guess: '))
        guesses += 1

        # Update the user as to whether the guess is too high, too low or correct
        if (guess > mystery_num):
            print('Too high!')
        elif (guess < mystery_num):
            print('Too low!')
        else:
            if (guesses == 1):
                print('You\'re correct! It took you 1 guess')
            else:
                print('You\'re correct! It took you %d guesses' % (guesses))
            # If the guess is correct exit the loop
            break
        

GuessTheNumber(100)
