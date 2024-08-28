#Defines the check_guess function
def check_guess(guess):
    guess.lower()
    #Checks whether the guess in the word
    if guess is in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

#Defines the ask_for_input function
def ask_for_input():
    #Iteratively checks that the input is a valid letter
    while True:
        guess = input("Guess a single letter of your choice : _ ")
        if len(guess) == 1 and guess.isalpha() == True:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)
ask_for_input()