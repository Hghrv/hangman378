while True:
    guess = input("Guess a single letter of your choice : _ ")
    if len(guess) == 1 and guess.isalpha() == True:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
