# 33. Drive-Thru

def welcome():
    print("Welcome to the Krusty Crab 🦀")
    print("--------------------------")
    print("MENU:")
    print("--------------------------")
    print("Press 1 for 🍔 Cheeseburger")
    print("Press 2 for 🍟 Fries")
    print("Press 3 for 🥤 Soda")
    print("Press 4 for 🍦 Ice Cream")
    print("Press 5 for 🍪 Cookie")

def get_item(num):
    if num == 1:
        return "🍔 Cheeseburger"
    elif num == 2:
        return "🍟 Fries"
    elif num == 3:
        return "🥤 Soda"
    elif num == 4:
        return "🍦 Ice Cream"
    elif num == 5:
        return "🍪 Cookie"
    else:
        return "Invalid item"
    


def main():
    welcome()
    order = int(input())
    print(get_item(order))

main()