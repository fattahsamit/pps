# Checkpoint 🐍⛳️
# Rock Paper Scissors ✊✋✌️

import random
print('===================')
print('Rock Paper Scissors')
print('===================')
print('1) ✊')
print('2) ✋')
print('3) ✌️')

# Take input from the user
player = int(input("Pick a number: "))
computer = random.randint(1,3)
print()

# Player's choice
if player == 1:
    print('You chose: ✊')
elif player == 2:
    print('You chose: ✋')
elif player == 3:
    print('You chose: ✌')
else:
    print('You chose the wrong number')

# Computer's choice
if computer == 1:
    print('CPU chose: ✊')
elif computer == 2:
    print('CPU chose: ✋')
elif computer == 3:
    print('CPU chose: ✌')

# Scenario: Player chose ✊
if player == 1:
    if computer == 1:
        print('Draw')
    elif computer == 2:
        print('The player lost, better luck next time!')
    else:
        print('The player won!')
# Scenario: Player chose ✋
elif player == 2:
    if computer == 1:
        print('The player won!')
    elif computer == 2:
        print('Draw')
    else:
        print('The player lost, better luck next time!')
# Scenario: Player chose ✌
elif player == 3:
    if computer == 1:
        print('The player lost, better luck next time!')
    elif computer == 2:
        print('The player won!')
    else:
        print('Draw')
else:
   print('Invalid number!') 
