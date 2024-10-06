# Challenge 1: Food Ratings

rating = float(input("How was the food? "))

if rating > 4.5:
    print('Extraordinary')
elif rating > 4:
    print('Excellent')
elif rating > 3:
    print('Good')
elif rating > 2:
    print('Fair')
else:
    print('Poor')