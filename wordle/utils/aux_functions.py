'''
Purpose:
Auxiliary functions for wordlesolver.py

Author:
gp-add11

Version:
0.1.0 (alpha) - January 2022

'''

# Imports
from typing import Union
import numpy as np
import string

# Variables
alphabets = list(string.ascii_lowercase) # May not be used in program, can use str.isalpha() instead.


# Helper functions

def and_operation(x: Union[list,np.array], y: Union[list,np.array]) -> np.array:
    '''
    Function to perform boolean AND operation over two lists or arrays and return the output.
    Inputs:
    
    Returns:
    
    '''
    if isinstance(x, list):
        x = np.array(x)
    if isinstance(y, list):
        y = np.array(y)
    return x & y

    
def contains_letters(letters: str, words_list: list) -> np.array:
    curr_bool_array = np.ones(shape = (len(words_list),), dtype = bool) # array of all True
    if len(letters) == 0:
        return curr_bool_array  # Return an array of all True
    else:
        for char in letters:
            curr_bool_array = and_operation(curr_bool_array,
                                            [char in word for word in words_list])
        return curr_bool_array

        
def set_position_letters(positioned_letters: str, words_list: list) -> np.array:
    curr_bool_array = np.ones(shape = (len(words_list),), dtype = bool) # array of all True
    if len(positioned_letters) > 5:
        raise ValueError("More than 5-character string received")
    elif len(positioned_letters) < 5:
        positioned_letters = positioned_letters + ('_'*(5-len(positioned_letters)))
    positioned_letters = positioned_letters.replace(' ', '_')
    for idx, char in enumerate(positioned_letters):
        if char == '_':
            continue
        elif char in alphabets:
            curr_bool_array = and_operation(curr_bool_array,
                                            [word[idx] == char for word in words_list])
        else: # Redundant since input values are already processed
            raise ValueError("Unknown character: " + char)
            break
    return curr_bool_array
    

def doesnt_contain_letters(not_matching_letters: str, words_list: list) -> np.array:
    curr_bool_array = np.ones(shape = (len(words_list),), dtype = bool) # array of all True
    if len(not_matching_letters) == 0:
        return curr_bool_array
    else:
        for char in not_matching_letters:
            curr_bool_array = and_operation(curr_bool_array,
                                            [char not in word for word in words_list])
        return curr_bool_array
        
def calculate_guess_feedback(guessed_words: list, positioned_letters: str, matched_letters: str, words_list: list) -> np.array:
    '''
    Function to calculate possible solutions based on previous user guesses.
    Inputs:
        guessed_words: list of string of words that user has guessed so far.
        positioned_letters: string of characters with correct positions in the target word.
        matched_letters: string of characters in the target word, whose position may be unknown.
        words_list: list of string of words
    Returns:
        numpy array of boolean elements, with calculated feedback i.e. the words not matching the conditions eliminated.
        
    '''
    all_matched_letters = set(positioned_letters.replace(' ','').replace('_','')) \
                            .union(set(matched_letters))
    
    guessed_words_letters = set()
    for word in guessed_words:
        guessed_words_letters = guessed_words_letters.union(set(word))
    
    unmatched_letters = guessed_words_letters.difference(all_matched_letters)
    
    return contains_letters(''.join(all_matched_letters), words_list) \
            & doesnt_contain_letters(''.join(unmatched_letters), words_list) \
            & set_position_letters(positioned_letters, words_list)    
            

def user_input() -> tuple:
    guessed_words = input_cleaner(input('Enter guessed words separated by space:\n')).split()
    matched_letters = input_cleaner(input('Enter letters that have successful match so far:\n'))
    positioned_letters = input_cleaner(input('Enter letters whose position is known (replace unknown position values with underscore):\n'))
    return guessed_words, matched_letters, positioned_letters
    
    
def input_cleaner(input_string: str) -> str:
    '''
    Function to check if any of the value in string is neither an alphabet nor blankspace nor underscore.
    Removes all such numeric or other special characters and returns lowercase version of the string of remaining characters.
    '''
    return ''.join(e for e in input_string if e.isalpha() or e in (' ', '_')).lower()
    
    
def get_n_letter_words(file:str, num_char:int = 5):
    with open(file) as f:
        words = f.read()
    words = words.lower().split('\n')
    return list(filter(lambda word: len(word) == num_char, words))
    
