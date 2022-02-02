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
from utils.word_search_functions import *

#Parameter variables
data_file = 'data/words_list.txt'
MAX_SOLUTIONS_TO_DISPLAY = 20
MIN_POSSIBILITIES_NEXT_GUESS = 2

# Helper functions
### Moved to utils/aux_functions.py

words = get_n_letter_words(data_file)

loop = 'y'

while loop.strip().lower() == 'y':

    loop = 'n' #To avoid infinite loops

    # Define alphabets, word import and some other variables first
    guessed_words, matched_letters, positioned_letters = user_input()
    possible_target_words = np.array(words)[calculate_guess_feedback(guessed_words, positioned_letters, matched_letters, words)]

    print('\n=== There is (are) {} possible solution(s) ==='.format(len(possible_target_words)))

    if len(possible_target_words) < MAX_SOLUTIONS_TO_DISPLAY:
        for word in possible_target_words:
            print(word)

    guess_suggested = ''

    if len(possible_target_words) >= MIN_POSSIBILITIES_NEXT_GUESS:
        print('\n=== Suggesting next word to guess... ===')
        if are_anagrams(possible_target_words= possible_target_words):
            guess_suggested = list(filter(lambda x: x not in guessed_words, possible_target_words.tolist()))[0]
        else:
            distinct_decisive_letters = set(''.join(possible_target_words)).difference(matched_letters).difference(positioned_letters)
            guess_suggested = more_characters_guesser(distinct_decisive_letters, possible_target_words, words)
        print(guess_suggested)
        loop = input("Check for another guess? (y/n): ")
    elif len(possible_target_words) == 1:
        print('Target word found: ', possible_target_words[0], '. Terminating program')
    else:
        print("Word not in dictionary. Please check the inputs once") #An exception can be raised if all words are verified to be in list and user input is incorrect.
        
