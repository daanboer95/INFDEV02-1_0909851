import sys

npc = raw_input("versus npc[1] or 2-player[2]?\n")
if(npc == 1):
    c1 = raw_input("Player: Rock, Paper, Scissors, Lizard, Spock?\n")
elif(npc == 2):
    c1 = raw_input("Player 1: Rock, Paper, Scissors, Lizard, Spock?\n")
    c2 = raw_input("Player 2: Rock, Paper, Scissors, Lizard, Spock?\n")
else:
    sys.stdout.write("Invalid answer")
