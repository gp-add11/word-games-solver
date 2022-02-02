'''
Script to evaluate performance of wordle solver algorithm if it is let to automatically solve the puzzle.

Author:
gp-add11

Version:
February 2022
0.1.1 (alpha)
'''

#Imports
import numpy as np
from utils.aux_functions import *
from utils.word_search_functions import *
import collections

MAX_ALLOWED_GUESS_COUNT = 10

#Data
data_file = 'data/words_list.txt' #Can be moved to separate constants file
words = get_n_letter_words(data_file)

performance_results = []
accuracy = 0
inaccuracy = 0
curr_alphabet = 'a' #Kept to track status of execution
print(curr_alphabet)
results_cache = []
for word in words: 
    if curr_alphabet != word[0]:
        curr_alphabet = word[0]
        print(curr_alphabet)
    target_word = word
    attempts, prediction, possible_predictions = target_word_finder(word, words, MAX_ALLOWED_GUESS_COUNT) #Replace words variable with approproate
    results_cache.append((word, attempts, prediction, possible_predictions))
    if prediction == word:
        accuracy += 1
    else:
        inaccuracy += 1
    performance_results.append(attempts)

print("======= Results: ========")

#Accuracy
print("Accuracy of word guess")
print("Correct: ", str(accuracy), ", Incorrect: ", str(inaccuracy))

#Attempts
print("Attempts taken to guess each word automatically: ")
guess_counts = collections.Counter(performance_results)
for k in sorted(list(guess_counts.keys())):  #Unpacking with dict.items() has keys unsorted
    print(k, guess_counts[k])
### Expected result: Counter({4: 2054, 3: 796, 2: 21, 5: 1081, 1: 1, 6: 267, 7: 40, 8: 6})
