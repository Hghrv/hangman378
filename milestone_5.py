#Imports the module random
import random

#Creates the Hangman class
class Hangman:
    def __init__(self, word_list, num_lives=5):
        #Initialises the attributes pf the class
        self.word_list = word_list
        self.num_lives = num_lives
        word_list = ["lemon", "mango", "banana", "orange", "avocado"]
        word = word_list.random()
        num_letters = len(set(word))
        word_guessed = ['_' for element in range(0, num_letters)]

    #Defines the methods in the class: the check_guess and  ask_for_input functions
    def check_guess(guess):
        #Defines the behaviour after checking if the letter is in the word or not 
        guess.lower()
        if guess is in word:
            print(f"Good guess! {guess} is in the word.")
            for index in range(0, len(word)):
                if word[index] == guess:
                    word_guessed[index] = guess
            num_letters = num_letters - 1
        else:
            num_lives = num_lives -1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {num_lives} lives left.")

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

#Sets the logic of the game
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if  num_lives == 0:
            print('You lost!')
        elif num_letters > 0 :
            word_guessed
            ask_for_input()
        else:
            word_guessed
            print('Congratulations. You won the game!')
play_game(word_list)