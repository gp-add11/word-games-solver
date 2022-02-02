'''
Main functions that use auxiliary functions to find words and return to user/main script.

Author:
gp-add11

Version:
0.1.1 (alpha) 
February 2022
'''

import numpy as np
from .aux_functions import *

def more_characters_guesser(letters_for_next_word: set, possible_target_words: np.array, words_list: list) -> str:
    # This function is returing only one word even if there are multiple possible good candidates for the next guess. 
    # Also, that one word is decided based on alpabetical order
    letter_score = {}
    for letter in letters_for_next_word:
        score = 0
        for word in possible_target_words:
            if letter in word:
                score += 1
        letter_score[letter] = score
    
    words_scores = []
    for word in words_list:
        score = 0
        for letter in set(word):
            if letter in letters_for_next_word:
                score += letter_score[letter]
        words_scores.append(score)
    
    return words_list[np.array(words_scores).argmax()]


def target_word_finder(target_word: str, words_list: list, max_guesses:int = 6) -> tuple:
    guess_count = 0 #Need to verify the update of this variable as conclusions depend on it.
    guessed_words = [] # can be checked with direct string
    last_guess = ''
    matched_letters = set()
    WORD_LENGTH = 5 #Should be a hyperparameter/constant defined elsewhere
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
        if guess_count > max_guesses:
            break
    
    return guess_count, predicted_target_word, possible_target_words # Possible target words kept temporarily to analyse when prediction is incorrect.

