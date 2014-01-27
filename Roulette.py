#!/usr/bin/python
# v1.0

"""Russian roulette style game for the command line"""

import math
import random

CHAMBER_COUNT = 6

bullet_chamber = 0
current_chamber = 0
player_turn = False

def setup_game():
	"""Sets a game up"""
	
	global bullet_chamber
	global current_chamber
	global player_turn
	
	bullet_chamber = math.ceil(random.random()*CHAMBER_COUNT)
	current_chamber = 1
	
	print "Gun prepared..."
	# determine who's first
	if random.random() >= 0.5:
		player_turn = True
		print "Player goes first"
	else:
		player_turn = False
		print "Computer goes first"

def pull_trigger():
	"""Trigger pulling function -> bool"""
	
	global current_chamber
	
	discharged = (current_chamber == bullet_chamber)
	if not discharged:
		print "*Click*\n"
	else:
		print "*BANG!*\n"
		
	current_chamber += 1
	return discharged	

def game_loop():
	"""Function containing the game's loop"""
	
	global player_turn
	
	while True:
		if player_turn:
			raw_input("Your turn...")
		else:
			print "Computer's turn..."
			
		if pull_trigger():
			break
		
		player_turn = not(player_turn)
		
	if player_turn:
		print "Computer wins"
	else:
		print "Player wins"
		

# Program loop
while True:
	if bullet_chamber > 0:		# don't display this on first run
		if raw_input("Play again? (y/n)").lower() == "n":
			break	# terminate
	
	setup_game()
	game_loop()

# EOF
