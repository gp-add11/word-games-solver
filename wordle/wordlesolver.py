'''
Purpose:
Script to solve wordle - 5-letter word guessing game.

Author:
gp-add11

Version:
0.1.1 (alpha) - January 2022
'''

#Imports
import numpy as np
from utils.aux_functions import *

#Parameter variables
data_file = 'data/words_list.txt'
MAX_SOLUTIONS_TO_DISPLAY = 20
MIN_POSSIBILITIES_NEXT_GUESS = 2

# Helper functions
### Moved to utils/aux_functions.py

words = get_n_letter_words(data_file)

# Define alphabets, word import and some other variables first
guessed_words, matched_letters, positioned_letters = user_input()
possible_target_words = np.array(words)[calculate_guess_feedback(guessed_words, positioned_letters, matched_letters, words)]

print('\n=== There is (are) {} possible solution(s) ==='.format(len(possible_target_words)))

if len(possible_target_words) < MAX_SOLUTIONS_TO_DISPLAY:
    for word in possible_target_words:
        print(word)

# Guess next word
if len(possible_target_words) > MIN_POSSIBILITIES_NEXT_GUESS:
    print('\n=== Suggesting next word to guess... ===')
    distinct_decisive_letters = set(''.join(possible_target_words)).difference(matched_letters).difference(positioned_letters)
    print(more_characters_guesser(distinct_decisive_letters, possible_target_words, words))

