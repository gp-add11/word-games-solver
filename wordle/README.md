# Wordle solver

Solving 5-leter word guessing game. 
In a typical game, only six guesses of valid 5-letter words can be made.  

### Scope  
- Assistance for 5-letter word guesses  
- Fully automated solution for 5-letter word guesses  
	-- Performance evaluation of fully automated solution of guessing and evaluation of feedback.  

#### Assistance script
- Takes user inputs:  
	-- Guesses made so far.  
	-- Letters which have a hit (matching) with or without known positions in target word.  
	-- Letters whose position(s) have been determined in the target word.  
- Returns:  
	-- Number of possible target words.  
	-- Suggested next guess word to narrow down soluion space.  

### Performance evaluation script
- Takes no user input.  
- For each possible 5-letter word, determines number of tries it will take to guess that as target word.  
- Results:  
  
| Number of tries taken | Number of target 5-letter words |  
| --------------------- | ------------------------------: |  
| 1                     | 1                               |  
| 2                     | 21                              |  
| 3                     | 796                             |  
| 4                     | 2054                            |  
| 5                     | 1081                            |  
| 6                     | 267                             |  
| 7                     | 40                              |  
| 8                     | 6                               |  
  
- Most words can be guessed within 6 attempts. 
- For 46 words, algorithm loses the game.  
- Heuristics:  
	-- Forming 5-letter word based on letters with highest frequency among all words. 
This is to increase probability of finding matching characters in target word, and to steeply reduce solution space.  
	-- Iterate through words containing same letters. Since frequency-based heuristcs will not work.  
- Observation: First guess is usually `arose` since it contains 5 most frequent letters.

## Future work  
- Check position-based heuristics approach for optimizing word search.  
- Check performance of the script, given initial guesses by user. Also try iterating through various guesses.  
- Generalize all parts to n-letter word.  
- Re-organize code and parameters.  

## Code organization  
- This folder contains main script for solving and perfomance evaluation.  
- `utils` folder contains helper functions.  