# Word Guessing Game
# Generate 10 random words from a list of words and then the user will
# have to guess those words by guessing its characters/letters using input.
# The user will only have 30 chances. (not limited characters each chances)

# randomly pick 10 words
from random import choice

with open ('words.txt') as file:
    all_words = [line.strip().lower() for line in file if not line.startswith('#')]

words = [choice(all_words) for n in range (10)]
print("<--------------------WORD GUESSING GAME-------------------->")
print()
print("Guide:")
print("     • Guess the 10 random words by guessing its letters.")
print("     • You can enter any letters each time.")
print("     • You only have 30 chances.\n")
# user input
# user correct guess and chances left
chances = 30
score = 0
while True:
    if chances != 0:
        print("You have "+ str (chances)+ " chances left.")
        letters = input("Make a guess: ")
        chances -=1
        for word in words:
            if letters == word:
                print("You got "+ word) 
                score += 1
            for letter in word:
                print(letter if letter in letters else "_", end=" ")
            print()       
# user score
    else:
        print("No chances left.\n You guessed " + str(score)+" word(s).")
        break