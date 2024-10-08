# 28. D.R.Y.

a = []
# range() lets you set a range
# input() takes value from the user
for i in range(5):
    a.append(int(input()))


# print() display a value
# max() takes the maximum value 
print("Maximum value: ",max(a))
# sum() shows the total value 
print("Total value: ",sum(a))