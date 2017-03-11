# 6.00 Problem Set 4
#
# Caesar Cipher Skeleton
#
import string
import random

WORDLIST_FILENAME = "words.txt"


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print ("  ", len(wordlist), "words loaded.")
    return wordlist


wordlist = load_words()


def is_word(wordlist, word):
    """
    Determines if word is a valid word.

    wordlist: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordlist.

    Example:
    >>> is_word(wordlist, 'bat') returns
    True
    >>> is_word(wordlist, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in wordlist


def random_word(wordlist):
    """
    Returns a random word.

    wordlist: list of words  
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)


def random_string(wordlist, n):
    """
    Returns a string containing n random words from wordlist

    wordlist: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([random_word(wordlist) for _ in range(n)])


def random_scrambled(wordlist, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordlist: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words


    NOTE:
    This function will ONLY work once you have completed your
    implementation of apply_shifts!
    """
    s = random_string(wordlist, n) + " "
    shifts = [(i, random.randint(0, 26)) for i in range(len(s)) if s[i - 1] == ' ']
    return apply_shifts(s, shifts)[:-1]


def get_fable_string():
    """
    Returns a fable in encrypted text.
    """
    f = open("fable.txt", "r")
    fable = str(f.read())
    f.close()
    return fable


# (end of helper code)
# -----------------------------------

#
# Problem 1: Encryption
#
def build_coder(shift):
    alphabet = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                'U', 'v', 'W', 'X', 'Y', 'Z']
    alpha = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']

    shifted = dict()

    # Takes the alphabet (uppercase) and for every value the array has assigns a cyclic shifted correspoding value to it
    for i in range(alphabet.__len__()):
        if i + shift < alphabet.__len__():
            shifted[alphabet[i]] = alphabet[i + shift]
        else:

            newvalue = (i + shift) % (alphabet.__len__())
            shifted[alphabet[i]] = alphabet[newvalue]

        # Same as above but for lower case alpa (lower)
    for i in range(alpha.__len__()):
        if i + shift < alpha.__len__():
            shifted[alpha[i]] = alpha[i + shift]
        else:
            nv = (i + shift) % (alpha.__len__())
            shifted[alpha[i]] = alpha[nv]
    return shifted


def build_decoder(shift):
    uppercase = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                 'T', 'U', 'v', 'W', 'X', 'Y', 'Z']
    lowercase = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                 't', 'u', 'v', 'w', 'x', 'y', 'z']
    decodelib = dict()

    for i in range(uppercase.__len__()):
        if i - shift < 0:
            newshift = uppercase.__len__() - (shift - i)
            decodelib[uppercase[i]] = uppercase[newshift]
        else:
            decodelib[uppercase[i]] = uppercase[i - shift]

    for j in range(lowercase.__len__()):
        if j - shift < 0:
            ns = lowercase.__len__() - (shift - j)
            decodelib[lowercase[j]] = lowercase[ns]
        else:
            decodelib[lowercase[j]] = lowercase[j - shift]

    return decodelib


def apply_coder(text, coder):
    newstring = ''
    for i in range(text.__len__()):
        if coder.get(text[i]):
            newstring = newstring + coder.get(text[i])
        else:
            newstring = newstring + text[i]
    return newstring


def apply_shift(text, shift):
    lib = build_coder(shift)
    tekst = ''
    for i in range(text.__len__()):
        if lib.get(text[i]):
            tekst += lib[text[i]]
        else:
            tekst += text[i]
    return tekst

#


wordlist = load_words()
def find_best_shift(wordlist, text):
    poplist=[]
    for i in range(27):
        streng = apply_shift(text, i)
        strengelist = streng.split()
        for j in range(strengelist.__len__()):
            if is_word(wordlist, strengelist[j]):
                #print str(strengelist[j]) + str(j) + " " + str(27-i)
                poplist.append(27-i)
    #making a list cuz then i can gimp this code for later ^^tehee
    return poplist.__getitem__(0)


#
# Problem 3: Multi-level encryption.
#
def apply_shifts(text, shifts):
    """
    Applies a sequence of shifts to an input text.

    text: A string to apply the Ceasar shifts to 
    shifts: A list of tuples containing the location each shift should
    begin and the shift offset. Each tuple is of the form (location,
    shift) The shifts are layered: each one is applied from its
    starting position all the way through the end of the string.  
    returns: text after applying the shifts to the appropriate
    positions

    Example:
    >>> apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    """
    ### TODO.


#
# Problem 4: Multi-level decryption.
#


def find_best_shifts(wordlist, text):
    """
    Given a scrambled string, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.

    Hint: Make use of the recursive function
    find_best_shifts_rec(wordlist, text, start)

    wordlist: list of words
    text: scambled text to try to find the words for
    returns: list of tuples.  each tuple is (position in text, amount of shift)
    
    Examples:
    >>> s = random_scrambled(wordlist, 3)
    >>> s
    'eqorqukvqtbmultiform wyy ion'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> shifts
    [(0, 25), (11, 2), (21, 5)]
    >>> apply_shifts(s, shifts)
    'compositor multiform accents'
    >>> s = apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    >>> s
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> print apply_shifts(s, shifts)
    Do Androids Dream of Electric Sheep?
    """


def find_best_shifts_rec(wordlist, text, start):
    """
    Given a scrambled string and a starting position from which
    to decode, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.

    Hint: You will find this function much easier to implement
    if you use recursion.

    wordlist: list of words
    text: scambled text to try to find the words for
    start: where to start looking at shifts
    returns: list of tuples.  each tuple is (position in text, amount of shift)
    """
    ### TODO.


def decrypt_fable():
    """
    Using the methods you created in this problem set,
    decrypt the fable given by the function get_fable_string().
    Once you decrypt the message, be sure to include as a comment
    at the end of this problem set how the fable relates to your
    education at MIT.

    returns: string - fable in plain text
    """
    ### TODO.

# What is the moral of the story?
#
#
#
#
#
