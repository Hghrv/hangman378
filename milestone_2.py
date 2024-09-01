#Milestone 1. Environment setup: Git environment setup under Git-Bash terminal successful
# Github repository created successfully
# Github repo successfully cloned in local Git


#Milestone 2. Creates the variables for the game

#Imports the module Random
import random

#Prints a list of favourite fruits
word_list = ["Lemon", "Mango", "Banana", "Orange", "Avocado"]
print(word_list)

#Prints a fruit name randomly from the list of fruits
word = random.choice(word_list)
print(word)

#Requests input from user and assigns it to a string variable
guess = input('Enter a single letter of your choice : _ ')

#Checks that the input is a single alphabetical character
if len(guess)== 1 and guess.isalpha() == True :
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

