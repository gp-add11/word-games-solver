'''
Purpose:
Script to solve wordle - 5-letter word guessing game.

Author:
gp-add11

Version:
0.1.0 (alpha) - January 2022
'''

#Imports
import numpy as np
from utils.aux_functions import *

#Parameter variables
data_file = 'data/words_list.txt'
MAX_SOLUTIONS_TO_DISPLAY = 20

# Helper functions
### Moved to utils.aux_functions.py

words = get_n_letter_words(data_file)

# Define alphabets, word import and some other variables first
guessed_words, matched_letters, positioned_letters = user_input()
possibilities = np.array(words)[calculate_guess_feedback(guessed_words, positioned_letters, matched_letters, words)]

print('\n=== There are {} possible solutions ==='.format(len(possibilities)))

if len(possibilities) < MAX_SOLUTIONS_TO_DISPLAY:
    for word in possibilities:
        print(word)
