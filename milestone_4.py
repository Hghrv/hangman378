import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        word_list = ["lemon", "mango", "banana", "orange", "avocado"]
        word = word_list.random()
        num_letters = len(set(word))
        word_guessed = ['_' for element in range(0, num_letters)]
       
    def check_guess(guess):
        guess.lower()
        if guess is in word:
            print(f"Good guess! {guess} is in the word.")
            for index in range(0, len(word)):
                if word[index] == guess:
                    word_guessed[index] = guess
            num_letters = num_letters - 1

    def ask_for_input():
    #Iteratively checks that the input is a valid letter
        while True:
            guess = input("Guess a single letter of your choice : _ ")
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess is in list_of_guesses:
                print("You already tried that letter!")
            else:
                check_guess(guess)
                list_of_guesses.append[guess]

    ask_for_input()