# Challenge 5: Sum of squares

number = int(input("Enter an integer: "))
total = 0

for i in range(number+1):
    total += i**2

print(total)