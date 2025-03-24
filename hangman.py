from utils import GameRunner, GetInput
import requests
import random
import os

WORDLIST_SOURCE = "https://www.mit.edu/~ecprice/wordlist.10000"

lives = 5

#Main Game Loop
@GameRunner
def Hangman():
    wordList = InitializeWordList(WORDLIST_SOURCE)
    randomWord = GetRandomWord(wordList, 6)
    wordDisplay = ""
    global lives 
    lives = 5

    os.system('cls')
    print("Hello welcome to hangman!\n")

    for char in randomWord:
        wordDisplay += "_"
    print(wordDisplay)

    while(not PlayerWon(wordDisplay)):
        if lives <= 0:
            print(f"You Lose! The word was: {randomWord}")
            return
        print(f"{lives} lives remaining")
        answer = input("Enter a guess: ")
        wordDisplay = CheckAnswer(answer, randomWord, wordDisplay)
        os.system('cls')
        print(wordDisplay)
    print("You Win!")

def PlayerWon(wordDisplay):
    for char in wordDisplay:
        if char == "_":
            return False
    return True

def RemoveLife():
    global lives
    lives -= 1

def CheckAnswer(playerGuess, wordToGuess, wordDisplay):
    correctLetterFound = False
    newWordDisplay = ""

    for i in range(len(wordToGuess)):
        #replace new correct character
        if wordToGuess[i] == playerGuess and wordDisplay[i] == "_":
            newWordDisplay += wordToGuess[i]
            correctLetterFound = True
        #Keep old correct guesses
        elif wordDisplay[i] != "_":
            newWordDisplay += wordToGuess[i]
        #Incorrect guesses
        else:
            newWordDisplay += "_"

    if not correctLetterFound:
        RemoveLife()
    return newWordDisplay

def GetRandomWord(wordList, minLength):
    randomWord = random.randint(0, len(wordList) - 1)

    #repeat until word of minimum length is found
    while len(wordList[randomWord]) < minLength:
        randomWord = random.randint(0, len(wordList) - 1)

    return wordList[randomWord].decode('utf-8')
    
def InitializeWordList(site):
    response = requests.get(site)
    wordList = response.content.splitlines()
    return wordList
Hangman()