import random

symbols = ['🍒',' 🍇', '🍉', '7️⃣']

def play():
    results = random.choices(symbols, k=3)
    print(results[0] + " | " + results[1] + " | " + results[2])

    jackpot = ['7️⃣', '7️⃣', '7️⃣']
    if results == jackpot:
        print('Jackpot! 💰')
    else:
        print("Thanks for playing!")

keep_playing = 'Y'

while keep_playing == 'Y':
    play()
    keep_playing = input("Keep playing? Press Y for YES and N for NO. ")
