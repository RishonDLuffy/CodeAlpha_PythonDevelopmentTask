#Create simple text based hangman game 
#By Rishon D'Souza


#Imports
import random
import os


#Setup
Words = ["TOMATO", "LETTUCE", "ONION", "CARROT", "BROCCOLI"]
ChosenWord =random.choice(Words)
FailCount = 0
attempt=None
attempts=[]
Hangmanpicture = {
    0:"""      _______
     |/      |
     |      (_)
     |      
     |      
     |      
     |
    _|___""",
    1:"""      _______
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
    _|___""",
    2:"""      _______
     |/      |
     |      (_)
     |      \\|
     |       
     |      
     |
    _|___""",
    3:"""      _______
     |/      |
     |      (_)
     |      \\|/
     |       
     |      
     |
    _|___""",
    4:"""      _______
     |/      |
     |      (_)
     |      \\|/
     |       |
     |      
     |
    _|___""",
    5:"""      _______
     |/      |
     |      (_)
     |      \\|/
     |       |
     |      / 
     |
    _|___""",
    6:"""      _______
     |/      |
     |      (_)
     |      \\|/
     |       |
     |      / \\
     |
    _|___""",
}

def printCurrentStats(FailCount):
    global RevealedWord
    print(Hangmanpicture[FailCount])
    print("Attempts left:",6-FailCount)
    RevealedWord = [letter if letter in attempts else "_" for letter in ChosenWord]
    print(" ".join(RevealedWord)) 


printCurrentStats(FailCount)


#Main
while True:
    attempt=input("Your guess?:").upper()                   #User Guess
    os.system('cls' if os.name == 'nt' else 'clear')

    if not attempt.isalpha() or len(attempt) != 1:          #Response to invalid
        print("Please enter a single letter.")
        printCurrentStats(FailCount)
        continue

    if attempt in attempts:                                 #Response to Repeat
        print("That Letter has already been revealed.")
        printCurrentStats(FailCount)
        continue

    if attempt in ChosenWord:                               #Response to valid
        print("Correct guess.")
        attempts.append(attempt)
    else:
        print("Incorrect guess.")
        FailCount +=1

    printCurrentStats(FailCount)
    if "_" not in RevealedWord:                              #Checks for win
        print("You WIN!!")
        break
    
    if FailCount==6:                                         #Checks for loss
        print("You FAILLL")
        print("The Word:",ChosenWord)
        break
    
    

