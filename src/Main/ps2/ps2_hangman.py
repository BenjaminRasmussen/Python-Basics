# 6.00 Problem Set 3
# 
# Hangman
#   Source is bugged cant execute my part of the game


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split("\n")
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)


# your code begins here!
def progresshangman(word):
    if len(word) < 1:
        guess = str(input("Enter a single letter guess"))
        for i in range(len(word)):
            if word[i] == guess:
                word[i] = None
                return True
            else:
                return False


def hangman():
    word = load_words()
    choose_word(word)
    lives = 4
    while lives > 0:
        if progresshangman(word) == False:
            lives = lives - 1

        else:
            if progresshangman(word) == True:
                print("Game over")
    print("You won")
