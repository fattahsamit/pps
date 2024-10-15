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
        print('Paper covers Rock.\nThe player lost, better luck next time!')
    elif computer == 3:
        print('Rock breaks Scissors.\nThe player won!')
    elif computer == 4:
        print('Rock crushes Lizard.\nThe player won!')
    else:
        print('Spock vaporizes Rock.\nThe player lost, better luck next time!')
# Scenario: Player chose ✋
elif player == 2:
    if computer == 1:
        print('Paper covers Rock.\nThe player won!')
    elif computer == 2:
        print('Draw')
    elif computer == 3:
        print('Scissors cut Paper.\nThe player lost, better luck next time!')
    elif computer == 4:
        print('Lizard eats Paper.\nThe player lost, better luck next time!')
    else:
        print('Paper disproves Spock.\nThe player won!')
# Scenario: Player chose ✌
elif player == 3:
    if computer == 1:
        print('Rock breaks Scissors.\nThe player lost, better luck next time!')
    elif computer == 2:
        print('Scissors cut Paper.\nThe player won!')
    elif computer == 3:
        print('Draw')
    elif computer == 4:
        print('Scissors beat Lizard.\nThe player won!')
    else:
        print('Spock smashes Scissors.\nThe player lost, better luck next time!')
# Scenario: Player chose 🦎
elif player == 4:
    if computer == 1:
        print('Rock crushes Lizard.\nThe player lost, better luck next time!')
    elif computer == 2:
        print('Lizard eats Paper.\nThe player won!')
    elif computer == 3:
        print('Scissors beat Lizard.\nThe player lost, better luck next time!')
    elif computer == 4:
        print('Draw')
    else:
        print('Lizard poisons Spock.\nThe player won!')
# Scenario: Player chose 🖖
elif player == 5:
    if computer == 1:
        print('Spock vaporizes Rock.\nThe player won!')
    elif computer == 2:
        print('Paper disproves Spock.\nThe player lost, better luck next time!')
    elif computer == 3:
        print('Spock smashes Scissors.\nThe player won!')
    elif computer == 4:
        print('Lizard poisons Spock.\nThe player lost, better luck next time!')
    else:
        print('Draw')
else:
   print('Invalid number!') 
