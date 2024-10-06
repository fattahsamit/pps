# Challenge 3: Dice Roll

import random

guess = int(input("What is the total (2-12)? "))

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

total = die1 + die2

while guess != total:
    guess = int(input("What is the total (2-12)? "))
    
    # dice reroll
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

print('You got it!')