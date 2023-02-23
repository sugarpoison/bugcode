#Program 14: Guessing Game

# .upper will convert the input to all uppercase.
capitalGuess = input("What is the capital of Ohio? ").upper()
numberOfGuesses = 1

# Python is case sensitive. Uppercase words and phrases will be different than lowercase ones.
while capitalGuess != "COLUMBUS":
    numberOfGuesses = numberOfGuesses + 1
    if numberOfGuesses > 3:
        print("Game Over! You guessed incorrectly 3 times.")
        break
    capitalGuess = input("Guess again. ")
if numberOfGuesses <= 3:    
    print("You guessed it. The capital of Ohio is Columbus. It took you " + str(numberOfGuesses) + " guesses.")
