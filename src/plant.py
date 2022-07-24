from pygame.sprite import Sprite

class Plant(Sprite):
    """ Class representing plants """

    def __init__(self, species, tile):
        super().__init__()
        self.species = species
        self.tile = tile
        self.position = tile.position
        if species == "potato":
            self.min_hydration = 60
            self.max_hydration = 80
            self.plant_protectant = "Altima 500SC"
            self.fertilizer = "mocznik.pl"
        elif species == "tomato":
            self.min_hydration = 70
            self.max_hydration = 80
            self.plant_protectant = "do uzupełnienia"
            self.fertilizer = "do uzupełnienia"
        elif species == "beetroot":
            self.min_hydration = 50
            self.max_hydration = 75
            self.plant_protectant = "do uzupełnienia"
            self.fertilizer = "do uzupełnienia"
        elif species == "cucumber":
            self.min_hydration = 70
            self.max_hydration = 90
            self.plant_protectant = "do uzupełnienia"
            self.fertilizer = "do uzupełnienia"
        self.growth = 0 # value between 0 and 1
        self.wilted = False

    def remove(self):  # to chyba do usunięcia, bo to tile zawiera planta, a nie na odwrót
        self.tile.plant = None

    def grow(self):
        return True
    # function growing plant during tick
    # using parameters of field tile to calculate growth
    # for example if tile is hydrated and fertilized it will grow faster