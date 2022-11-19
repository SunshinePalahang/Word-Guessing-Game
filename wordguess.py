# Word Guessing Game
# Generate 10 random words from a list of words and then the user will
# have to guess those words by guessing its characters/letters using input.
# The user will only have 30 chances. (not limited characters each chances)

# randomly pick 10 words
from random import choice

with open ('words.txt') as file:
    all_words = [line.strip().lower() for line in file if not line.startswith('#')]

words = [choice(all_words) for n in range (10)]
# user input
# user correct guess and chances left
# user score