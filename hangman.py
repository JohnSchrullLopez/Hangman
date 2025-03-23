from utils import GameRunner, GetInput
import requests
import random

WORDLIST_SOURCE = "https://www.mit.edu/~ecprice/wordlist.10000"

@GameRunner
def Hangman():
    wordList = InitializeWordList(WORDLIST_SOURCE)
    randomWord = GetRandomWord(wordList)
    wordDisplay = ""

    print("Hello welcome to hangman!\n")

    for char in randomWord:
        wordDisplay += "_"
    print(wordDisplay)

    while(not PlayerWon(wordDisplay)):
        answer = input("Enter a guess: ")
        wordDisplay = CheckAnswer(answer, randomWord, wordDisplay)
        print(wordDisplay)

def PlayerWon(wordDisplay):
    for char in wordDisplay:
        if char == "_":
            print("False return")
            return False
    return True

def CheckAnswer(playerGuess, wordToGuess, wordDisplay):
    newWordDisplay = ""
    for i in range(len(wordToGuess)):
        #replace new correct character
        if wordToGuess[i] == playerGuess and wordDisplay[i] == "_":
            newWordDisplay += wordToGuess[i]
        #Keep old correct guesses
        elif wordDisplay[i] != "_":
            newWordDisplay += wordToGuess[i]
        #Incorrect guesses
        else:
            newWordDisplay += "_"
    return newWordDisplay

def GetRandomWord(wordList):
    randomWord = random.randint(0, len(wordList) - 1)
    return wordList[randomWord].decode('utf-8')
    
def InitializeWordList(site):
    response = requests.get(site)
    wordList = response.content.splitlines()
    return wordList
Hangman()