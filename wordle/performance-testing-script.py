'''
Script to evaluate performance of wordle solver if it is let to automatically solve the puzzle.

Version:
February 2022
0.1.0 (alpha)
'''
#Imports
import numpy as np
from utils.aux_functions import *

MAX_ALLOWED_GUESS_COUNT = 5

def target_word_finder(target_word: str, words_list: list) -> tuple:
    guess_count = 0 #Need to verify the update of this variable as conclusions depend on it.
    guessed_words = [] # can be checked with direct string
    last_guess = ''
    matched_letters = set()
    WORD_LENGTH = 5
    positioned_letters = '_'*WORD_LENGTH
    predicted_target_word = 'UNKNOWN' # kept when guesser gets stuck.
    while last_guess != target_word:
        for pos, letter in enumerate(last_guess):
            if letter in target_word:
                matched_letters.add(letter)
            if letter == target_word[pos]:
                temp = list(positioned_letters)
                temp[pos] = letter
                positioned_letters = ''.join(temp)
        possible_target_words = np.array(words_list)[calculate_guess_feedback(guessed_words= guessed_words,
                                                                         positioned_letters= positioned_letters,
                                                                         matched_letters= ''.join(matched_letters),
                                                                         words_list= words_list)]
        if len(possible_target_words) == 1:
            guess_count += 1
            predicted_target_word = possible_target_words[0]
            possible_target_words = predicted_target_word
            break
        elif are_anagrams(possible_target_words):
            last_guess = list(filter(lambda x: x not in guessed_words, possible_target_words.tolist()))[0]
        else:
            last_guess = more_characters_guesser(letters_for_next_word= set(''.join(possible_target_words)).difference(matched_letters).difference(positioned_letters), 
                                                 possible_target_words= possible_target_words, 
                                                 words_list= words_list)
        guess_count += 1
        guessed_words.append(last_guess)
        if last_guess == target_word: #Redundant, do-while would have been ideal!
            predicted_target_word = last_guess
            possible_target_words = predicted_target_word
            break
        if guess_count > MAX_ALLOWED_GUESS_COUNT:
            break
    
    return guess_count, predicted_target_word, possible_target_words # Possible target words kept temporarily to analyse when prediction is incorrect.

def are_anagrams(possible_target_words: np.array) -> bool:
    first_distinct_characters = set(possible_target_words[0])
    _anagram = True
    for word in possible_target_words[1:]:
        if first_distinct_characters != set(word):
            _anagram = False
            break
    return _anagram


	
performance_results = []
accuracy = 0
inaccuracy = 0
curr_alphabet = 'a' #Kept to track status of execution
print(curr_alphabet)
results_cache = []
for word in words: #Replace words variable with approproate
    if curr_alphabet != word[0]:
        curr_alphabet = word[0]
        print(curr_alphabet)
    target_word = word
    attempts, prediction, possible_predictions = target_word_finder(word, words) #Replace words variable with approproate
    results_cache.append((word, attempts, prediction, possible_predictions))
    if prediction == word:
        accuracy += 1
    else:
        inaccuracy += 1
    performance_results.append(attempts)

import collections
collections.Counter(performance_results)
###Counter({4: 2054, 3: 796, 2: 21, 5: 1081, 1: 1, 6: 267, 7: 40, 8: 6})