#! python3
# hangman.py - A text-based adaptation of the hangman game.

import random

wordPool = [
    'chemistry', 'aardvark', 'muse', 'water', 'love',
    'perfect', 'substrate', 'content', 'banner', 'template',
    'forlorn', 'solution', 'choice', 'compass', 'construct',
    'abstract', 'compact', 'prejudice', 'contrite', 'privy'
    ]
wordIndex = random.randint(0, len(wordPool) - 1)
word = wordPool[wordIndex].upper()

guessCount = len(word)
wordBlank = []

def generate():
    for number in range(len(word)):
        wordBlank.append('_')

def printer():
    for item in wordBlank:
        print(item, end=' ')

def checkGuess():
    for i in range(len(word)):
        if guess == word[i]:
            wordBlank[i] = word[i]
            
def checkGame():
    if '_' not in wordBlank:
        return 'win'
    
print('****HANGMAN GAME****\nYou Are Welcome To Play!')
print('\nThe word to guess is: ', end=' ')
generate()
printer()
print('\nYou have', guessCount, 'guesses.')
        
while guessCount > 0:    
    guess = input('\nGuess a letter or the entire word: ').upper()    
    
    if len(guess) == 1:
        guessCount -= 1
        print('You guessed letter \'' + guess + '\'')
        if guess in word:
            print('You are correct!')
            checkGuess()
            printer()
            if checkGame() == 'win':
                print('\nCongratulations! You win.')
                break
            if guessCount == 0:
                print('\nSorry, you are out of guesses.\nYou lose!\nThe word is', word)
            else:
                print('\nGuesses left: ', guessCount)
        else:
            print('Incorrect guess!')
            printer()
            if guessCount == 0:
                print('\nSorry, you are out of guesses.\nYou lose!\nThe word is', word)
            else:
                print('\nGuesses left: ', guessCount)
        
    elif len(guess) > 1:
        guessCount -= 1
        print('You guessed the word \'' + guess + '\'')        
        if guess == word:            
            print('Your guess is correct.')
            print('Congratulations! You win!')
            break
        else:
            print('Incorrect guess!')
            printer()
            if guessCount == 0:
                print('\nSorry, you are out of guesses.\nYou lose!\nThe word is', word)
            else:
                print('\nGuesses left: ', guessCount)
