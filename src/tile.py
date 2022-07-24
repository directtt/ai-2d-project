from pygame.sprite import Sprite


class Tile(Sprite):
    """ Class to represent single board tile """

    def __init__(self, type, row_id, col_id, image, rect, cost, stan_nawodnienia, rodzaj_gleby,
                 stan_nawiezienia, stopien_rozwoju, rodzaj_rosliny, rodzaj_nawozu, to_water):
        super().__init__()
        self.type = type
        self.row_id = row_id
        self.col_id = col_id
        self.position = (row_id, col_id)
        self.image = image
        self.cnn_image = image
        self.rect = rect
        self.cost = cost

        # nwm, ten kod po polsku moze kiedys do zmiany, póki co mi sie nie chce
        self.stan_nawodnienia = stan_nawodnienia
        self.rodzaj_gleby = rodzaj_gleby
        self.stan_nawiezienia = stan_nawiezienia
        self.stopien_rozwoju = stopien_rozwoju
        self.rodzaj_rosliny = rodzaj_rosliny
        self.rodzaj_nawozu = rodzaj_nawozu
        self.to_water = to_water

        self.predicted_plant = None

    def __repr__(self):
        return "(type: %s, position: (%s, %s), cost: %s, rodzaj_rośliny: %s, to_water: %s)" % \
               (self.type, self.row_id, self.col_id, self.cost, self.rodzaj_rosliny, self.to_water)

    def get_type(self):
        return self.type

    def get_position(self):
        return self.row_id, self.col_id

    def get_cost(self):
        return self.cost

    def get_plant_type(self):
        return self.rodzaj_rosliny

    def get_to_water(self):
        return self.to_water