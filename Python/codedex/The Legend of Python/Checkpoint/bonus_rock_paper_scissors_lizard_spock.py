# Checkpoint 🐍⛳️
# Rock Paper Scissors Lizard Spock ✊✋✌️🦎🖖

import random
print('================================')
print('Rock Paper Scissors Lizard Spock')
print('================================')
print('1) ✊')
print('2) ✋')
print('3) ✌️')
print('4) 🦎')
print('5) 🖖')

# Take input from the user
player = int(input("Pick a number: "))
computer = random.randint(1,5)
print()

# Player's choice
if player == 1:
    print('You chose: ✊')
elif player == 2:
    print('You chose: ✋')
elif player == 3:
    print('You chose: ✌')
elif player == 4:
    print('You chose: 🦎')
elif player == 5:
    print('You chose: 🖖')

# Computer's choice
if computer == 1:
    print('CPU chose: ✊')
elif computer == 2:
    print('CPU chose: ✋')
elif computer == 3:
    print('CPU chose: ✌')
elif computer == 4:
    print('CPU chose: 🦎')
elif computer == 5:
    print('CPU chose: 🖖')

# Scenario: Player chose ✊
if player == 1:
    if computer == 1:
        print('Draw')
    elif computer == 2:
        print('The player lost, better luck next time!')
    elif computer == 3:
        print('The player won!')
    elif computer == 4:
        print('The player won!')
    else:
        print('The player lost, better luck next time!')
# Scenario: Player chose ✋
elif player == 2:
    if computer == 1:
        print('The player won!')
    elif computer == 2:
        print('Draw')
    elif computer == 3:
        print('The player lost, better luck next time!')
    elif computer == 4:
        print('The player lost, better luck next time!')
    else:
        print('The player won!')
# Scenario: Player chose ✌
elif player == 3:
    if computer == 1:
        print('The player lost, better luck next time!')
    elif computer == 2:
        print('The player won!')
    elif computer == 3:
        print('Draw')
    elif computer == 4:
        print('The player won!')
    else:
        print('The player lost, better luck next time!')
# Scenario: Player chose 🦎
elif player == 4:
    if computer == 1:
        print('The player lost, better luck next time!')
    elif computer == 2:
        print('The player won!')
    elif computer == 3:
        print('The player lost, better luck next time!')
    elif computer == 4:
        print('Draw')
    else:
        print('The player won!')
# Scenario: Player chose 🖖
elif player == 5:
    if computer == 1:
        print('The player won!')
    elif computer == 2:
        print('The player lost, better luck next time!')
    elif computer == 3:
        print('The player won!')
    elif computer == 4:
        print('The player lost, better luck next time!')
    else:
        print('Draw')
else:
   print('Invalid number!') 
