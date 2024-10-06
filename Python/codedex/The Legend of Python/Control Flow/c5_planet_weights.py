# Challenge 5: Planet Weights

weight = float(input('Earth weight: '))
planet_number = int(input('Planet number: '))

if planet_number == 1:
    destination_weight = weight*0.38
    print(destination_weight)
elif planet_number == 2:
    destination_weight = weight*0.91
    print(destination_weight)
elif planet_number == 3:
    destination_weight = weight*0.38
    print(destination_weight)
elif planet_number == 4:
    destination_weight = weight*2.53
    print(destination_weight)
elif planet_number == 5:
    destination_weight = weight*1.07
    print(destination_weight)
elif planet_number == 6:
    destination_weight = weight*0.89
    print(destination_weight)
elif planet_number == 7:
    destination_weight = weight*1.14
    print(destination_weight)
else:
    print('Invalid planet number')