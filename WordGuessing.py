import random

def randomWordCount(word):
    run = 0
    for i in range(len(word)):
        "_"
        run += 1


userName = ""

print("Word Guessing Game")
print("You have to guess the letters and complete the word.")
print("Good Luck!")


randomWordList = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

randomWord = random.choice(randomWordList)

maxGuesses = maxGuesses = len(randomWord) + 2
guesses = maxGuesses
letterList = ""
inputLetter = ""


while guesses > 0:

    for letter in randomWord:
        
        if letter in letterList:
            print(letter)
            continue

        elif letter == inputLetter.lower():
            print(letter)
            if randomWord.count(inputLetter.lower()) != 1:
              letterList = str(letterList) + str(inputLetter *(randomWord.count(inputLetter)))
            else:
                letterList += inputLetter
            continue
                
        else :
            print("_")

    if len(inputLetter) > 1 or inputLetter.isdigit():
        print("Invalid input!")
        print("Please enter a single letter.")
        continue
        
    if inputLetter not in randomWord:
        guesses -= 1
        print("Wrong!")
        print(f"You have {guesses} guesses left!")

    if len(letterList) == len(randomWord):
        print("Congratulations!")
        print("You completed the word \" " + randomWord + " \" correctly." )
        print("Thank you for playing.")
        break 

    if guesses == 0:

        print("You are out of guesses.")
        print("Better Luck next time.")
        break


    inputLetter = input("guess a Character: ")
            
    






    
