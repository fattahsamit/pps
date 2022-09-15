n = input()
if n%2!=0:
    print("Weird\n")

elif n%2==0:
    if n>=2 and n<=5:
        print("Not Weird\n")
    elif n>=6 and n<=20:
        print("Weird\n")
    elif n>20:
        print("Not Weird\n")