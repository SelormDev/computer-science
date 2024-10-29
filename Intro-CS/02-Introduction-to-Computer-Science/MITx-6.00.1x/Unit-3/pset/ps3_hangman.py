# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "C:/Users/selor/Desktop/computer-science/Intro-CS/02-Introduction-to-Computer-Science/MITx-6.00.1x/Unit-3/pset/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for letter in secretWord:
        if not letter in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    currentGuess = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            currentGuess += letter
        else:
            currentGuess += "_ "
    return currentGuess

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    letters = "abcdefghijklmnopqrstuvwxyz"
    list_letter = [letter for letter in letters 
     ]
    for letter in lettersGuessed:
        if letter in list_letter:
            del(list_letter[list_letter.index(letter)])
    return ''.join(list_letter)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    secretWordToLower = secretWord.lower()
    guessesLeft = 8
    lettersGuessed = []
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    print('-------------')
    
    
    while guessesLeft >= 1:
        print('You have ' + str(guessesLeft) + ' guesses left.')
        print('Available letters: ' + str(getAvailableLetters(lettersGuessed)))
        guessedLetter = input("Please guess a letter: ").lower()
        
        if guessedLetter in lettersGuessed:
            print('Oops! You\'ve already guessed that letter: ' + str(getGuessedWord(secretWordToLower, lettersGuessed)))
        elif guessedLetter not in secretWordToLower:
            lettersGuessed.append(guessedLetter)
            print('Oops! That letter is not in my word: ' + str(getGuessedWord(secretWordToLower, lettersGuessed)))
            guessesLeft = guessesLeft - 1
        else:
            lettersGuessed.append(guessedLetter)
            print('Good guess: ' + str(getGuessedWord(secretWordToLower, lettersGuessed)))
            
        
        print('-------------')
        
        if isWordGuessed(secretWordToLower, lettersGuessed):
            print('Congratulations, you won!')
            break
        if guessesLeft == 0:
            print('Sorry, you ran out of guesses. The word was ' + str(secretWordToLower))
        
    
    






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
hangman('ElSe')
