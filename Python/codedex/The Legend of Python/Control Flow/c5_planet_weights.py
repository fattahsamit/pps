# Challenge 5: Planet Weights

weight = float(input('Earth weight: '))
planet_number = int(input('Planet number: '))

if planet_number == 1:
    print(weight*0.38)
elif planet_number == 2:
    print(weight*0.91)
elif planet_number == 3:
    print(weight*0.38)
elif planet_number == 4:
    print(weight*2.53)
elif planet_number == 5:
    print(weight*1.07)
elif planet_number == 6:
    print(weight*0.89)
elif planet_number == 7:
    print(weight*1.14)
else:
    print('Invalid planet number')