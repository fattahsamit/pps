class Pokemon:
    def __init__(self, entry, name, types, description, is_caught, level, region, height, weight):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught

        self.level = level
        self.region = region
        self.height = height
        self.weight = weight

    def speak(self):
        print(self.name, self.name)

    def display_details(self):
        print("Entry Number:", self.entry)
        print("Name:", self.name)
        print("Type:", self.types)
        print("Description:", self.description)
        if self.is_caught : print(self.name + " has already been caught!")
        else: print(self.name + " remains uncaught")

        print("Level:", self.level)
        print("Region:", self.region)
        print("Height:", self.height)
        print("Weight:", self.weight)

pikachu = Pokemon(25, 'Pikachu', 'Electric', "It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.", True, 58 , 'Kanto', '1 ft 4 inches', '13.2 lbs')
pikachu.display_details()
pikachu.speak()

bulbasaur = Pokemon(1, 'Bulbasaur', 'Grass', "For some time after its birth, it uses the nutrients that are packed into the seed on its back in order to grow.", True, 45 , 'Kanto', '2 ft 4 inches', '15.2 lbs')
bulbasaur.display_details()
bulbasaur.speak()

mewtwo = Pokemon(150, 'Mewtwo', 'Psychic', "Its DNA is almost the same as Mew's. However, its size and disposition are vastly different.", False, 250 , 'Kanto', '6 ft 7 inches', '269 lbs')
mewtwo.display_details()
mewtwo.speak()