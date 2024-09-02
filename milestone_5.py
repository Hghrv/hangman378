#Imports the module random
import random

#Creates the Hangman class

class Hangman:
    word_list = ["lemon", "mango", "banana", "orange", "avocado"]
    def __init__(self, word_list, num_lives=5):
        #Initialises the attributes pf the class
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word = random.choice(word_list)
        self.num_letters = len(set(self.word))
        self.word_guessed = ['_' for element in range(0, len(self.word))]
      

    #Defines the methods in the class: the check_guess and  ask_for_input functions
    def check_guess(self, guess):
        #Defines the behaviour after checking if the letter is in the word or not 
        guess.lower()
        if guess in self.word:
            self.num_letters = self.num_letters - 1
            print(f"Good guess! {guess} is in the word.")
            for index in range(0, len(self.word)):
                if self.word[index] == guess:
                    self.word_guessed[index] = guess
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        print(self.word_guessed)

    def ask_for_input(self):
    #Iteratively checks that the input is a valid letter
        while True:
            guess = input("Guess a single letter of your choice : _ ")
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
           

#Sets the logic of the game
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if  game.num_lives == 0:
            print('You lost!')
            print(f'The hidden word was: {game.word}')
            break
        elif game.num_letters > 0 :
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break
play_game(Hangman.word_list)