class City:
    def __init__(self, name, country, population, landmarks, nickname, founding_year, mayor):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks
        self.nickname = nickname
        self.founding_year = founding_year
        self.mayor = mayor

dhaka = City('Dhaka', 'Bangladesh', 24000000, ['Lalbagh Fort', 'Parliament House', 'Ahsan Manzil Museum'], 'The Venice of the East', 1608, 'Atiqul Islam')
vancouver = City('Vancouver', 'Canada', 631000, ['Stanley Park', 'Granville Island', 'Grouse Mountain'], 'Van', 1886, 'Kennedy Stewart')

print(vars(dhaka))
print(vars(vancouver))