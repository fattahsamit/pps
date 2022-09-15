# Returns either the index of the location in the array,
#  or -1 if the array did not contain the targetValue
def doSearch(array, targetValue):
    min = 0
    max = len(array) - 1

    while max>=min:
        guess = (min + max)//2
        
        if (array[guess] == targetValue):
            return guess
        
        elif (array[guess] < targetValue):
            min = guess + 1

        else:
            max = guess - 1
    
    return -1

g = doSearch( [22, 44, 66, 88], 88)
print(g)
