# Word Guessing Game
# Generate 10 random words from a list of words and then the user will
# have to guess those words by guessing its characters/letters using input.
# The user will only have 20 chances. (not limited characters each chances)

# randomly pick 10 words
from random import choice
from colorama import Fore, Style

with open ('words.txt') as file:
    all_words = [line.strip().lower() for line in file if not line.startswith('#')]

words = [choice(all_words) for n in range (10)]
print("<--------------------WORD GUESSING GAME-------------------->")
print()
print("Guide:")
print("     • Guess the 10 random words by guessing its letters.")
print("     • You can enter any letters each time.")
print("     • You only have 20 chances.\n")
# user input
# user correct guess and chances left

chances = 20
score = 0
while True:
    if chances != 0:
        print(Fore.RED+"You have "+ str (chances)+ " chances left.")
        print(Style.RESET_ALL)
        letters = input("Make a guess: ")
        chances -=1
        print(Fore.BLUE+"You guessed " + str(score)+" word(s).")
        print(Style.RESET_ALL)
        for word in words:
            if letters == word:
                print(Fore.GREEN+"You got "+ word)
                print(Style.RESET_ALL) 
                score += 1
            for letter in word:
                print(letter if letter in letters else "_", end=" ")
            print()       
# user score
    else:
        print(Fore.RED+"No chances left.")
        print(Style.RESET_ALL)
        print("You guessed " + str(score)+" word(s).")
        print(Fore.GREEN+"Correct Words:")
        print(*words, sep="\n")
        print(Style.RESET_ALL)
        exit = input("Would you like to continue: ")
        if exit == "n":
            print("THANK YOU FOR USING MY PROGRAM! \n ©️ 2022 All rights reserved.") 
        break
