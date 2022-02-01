MAX_ALLOWED_GUESS_COUNT = 10

def target_word_finder(target_word: str, words_list: list) -> tuple:
    guess_count = 0
    guessed_words = [] # can be checked with direct string
    last_guess = ''
    matched_letters = set()
    WORD_LENGTH = 5
    positioned_letters = '_'*WORD_LENGTH
    predicted_target_word = 'UNKNOWN' # kept when guesser gets stuck. Ex. abode
    while last_guess != target_word:
        #print("Guess number: ", str(guess_count))
        for pos, letter in enumerate(last_guess):
            if letter in target_word:
                matched_letters.add(letter)
            if letter == target_word[pos]:
                temp = list(positioned_letters)
                temp[pos] = letter
                positioned_letters = ''.join(temp)
        #print("Guesses for this iteration: ", str(guessed_words), ", Matched letters: ", str(matched_letters), ", Positioned letters: ", str(positioned_letters))
        possible_target_words = np.array(words)[calculate_guess_feedback(guessed_words= guessed_words,
                                                                         positioned_letters= positioned_letters,
                                                                         matched_letters= ''.join(matched_letters),
                                                                         words_list= words_list)]
        guess_count += 1
        #print("Identified ", str(len(possible_target_words)), " possibilities")
        if len(possible_target_words) == 1:
            predicted_target_word = possible_target_words[0]
            #print('############## Target word is {} ##############'.format(predicted_target_word))
            break
        last_guess = more_characters_guesser(letters_for_next_word= set(''.join(possible_target_words)).difference(matched_letters).difference(positioned_letters), 
                                             possible_target_words= possible_target_words, 
                                             words_list= words_list)
        #print("Guessing next word: ", last_guess, '-------------------------------------------------------------------\n')
        guessed_words.append(last_guess)
        if guess_count > MAX_ALLOWED_GUESS_COUNT:
            break
    
    return guess_count, predicted_target_word, possible_target_words # Possible target words kept temporarily
	
performance_results = []
accuracy = 0
inaccuracy = 0
curr_alphabet = 'a'
print(curr_alphabet)
results_cache = []
for word in words:
    #print(word)
    if curr_alphabet != word[0]:
        curr_alphabet = word[0]
        print(curr_alphabet)
    target_word = word
    attempts, prediction, possible_predictions = target_word_finder(word, words)
    results_cache.append((attempts, prediction, possible_predictions))
    if prediction == word:
        accuracy += 1
    else:
        inaccuracy += 1
    if prediction == 'UNKNOWN':
        performance_results.append(attempts + len(possible_predictions))
    else:
        performance_results.append(attempts)