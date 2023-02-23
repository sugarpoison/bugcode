colorGuess = input("What's my favorite color? ")
numberOfGuesses = 1

while colorGuess != "Purple":
    numberOfGuesses =  numberOfGuesses + 1
    if numberOfGuesses > 3:
        print("Wow! You're stupid! You got it wrong 3 times! Be ashamed.")
        break
    coloGuess = input("Try again!")
if numberOfGuesses <= 3:
    print("Yeah I guess that's right. It took you " + str(numberOfGuesses) + " tries.")