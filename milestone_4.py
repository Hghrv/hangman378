import random
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        word_list = ["lemon", "mango", "banana", "orange", "avocado"]
        word = word_list.random()
        num_letters = len(word)
        word_guessed = ['_' for i in range(0, num_letters) ]
        list_of_guesses =[]
