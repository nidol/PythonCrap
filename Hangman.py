#!/usr/bin/python

"""
A simple game of hangman
v1.0.1
"""

import math
import random

TOTAL_WRONG_GUESSES = 6
WORDS_FILENAME = "words.txt"
VALID_CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getWordList(filename):
	"""
	Loads and returns a list of words from a file
	"""
	with open(filename, "r") as f:
		results = f.read().strip().upper().split('\n')
	f.closed
	return results

def getRandomWord(words):
	"""
	Returns a random item from a list
	"""
	return words[int(math.floor(random.random()*len(words)))]

def getProgress(word, guessed_chars):
	"""
	Returns the progress of the correctly guessed letters
	"""
	match = ""
	for i in word:
		if guessed_chars.find(i) > -1:
			match += i
		else:
			match += "_"
	return match
	
def getCharacter():
	data = raw_input("Enter a character: ").upper()
	if len(data) == 0 or VALID_CHARACTERS.find(data[0]) == -1:
		return ""
		
	return data[0]
		
words = getWordList(WORDS_FILENAME)
current_word = getRandomWord(words)
guessed_correct = ""
guessed_wrong = ""

# Game Loop
while len(guessed_wrong) < TOTAL_WRONG_GUESSES:
	result = getProgress(current_word, guessed_correct)
	if (result == current_word):
		break;	# game ends
	else:
		print "You have " + str(TOTAL_WRONG_GUESSES - len(guessed_wrong)) + " guesses left"
		temp = ""
		for i in result:
			temp += i + " "
		print temp
		
	char = getCharacter()
	if char == "":
		print "Invalid character"
		continue	# loop unchanged
	
	if guessed_correct.find(char) > -1 or guessed_wrong.find(char) > -1:
		print "You already guessed that character!"
		continue	# loop unchanged
	elif current_word.find(char) > -1:
		guessed_correct += char
	else:
		guessed_wrong += char

if getProgress(current_word, guessed_correct) == current_word:
	print "You win! The word was: " + current_word
else:
	print "Game Over. The word was: " + current_word
	
# EOF
