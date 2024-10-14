# Challenge 5: Dog Years

def dog_years(name, age):
    dog_year = str(age*7)
    result = name + " is " + dog_year + " years old in human years."
    return result

dog_years('Landon', 3)
dog_years('Red Bean', 6)
dog_years('Cooper', 2)