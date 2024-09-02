#Imports the module random
import random

#Creates the Hangman class

class Hangman:
    
    list_of_guesses =[]
    def __init__(self, word_list, num_lives=5):
        #Initialises the attributes pf the class
        self.word_list = word_list
        self.num_lives = num_lives
        self.word_list = ["lemon", "mango", "banana", "orange", "avocado"]
        self.list_of_guesses = []
        self.word = random.choices(self.word_list)
        self.num_letters = len(set(self.word))
        self.word_guessed = ['_' for element in range(0, self.num_letters)]
      

    #Defines the methods in the class: the check_guess and  ask_for_input functions
    def check_guess(self, guess):
        #Defines the behaviour after checking if the letter is in the word or not 
        guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index in range(0, len(self.word)):
                if self.word[index] == guess:
                    self.word_guessed[index] = guess
            self.num_letters = self.num_letters - 1
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            
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
           

               
    
game = Hangman(word_list)
game.ask_for_input()
