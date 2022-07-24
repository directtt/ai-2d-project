from constants import Constants
from random import randint, choice


class BasePlant:

    def __init__(self):
        self.appearance_points = 0
        self.difficulty_points = 0
        self.profit_points = 0

    def first_population_generator(self):
        pass

    def __int__(self):
        return sum([self.appearance_points, self.profit_points]) - self.difficulty_points

    def __float__(self):
        return self.__int__()


def stop_condition(average):
    return round(average, 2) == Constants.POINTS_AVERAGE


def plant_selector(plant_name: str) -> BasePlant:
    if plant_name == Constants.POTATO:
        return Potato()
    elif plant_name == Constants.WHEAT:
        return Wheat()
    elif plant_name == Constants.CACTUS:
        return Cactus()


class BaseField:
    """Class that represents what plants grow on a certain field divided into 9 tiles"""

    possibilities = [Constants.WHEAT, Constants.POTATO, Constants.CACTUS]

    def __init__(self, plants):
        self.plants: list(BasePlant) = plants
        self.evaluation = self.evaluate_function()

    def mutate(self):
        self._perform_mutation()
        self.evaluation = self.evaluate_function()

    def _perform_mutation(self):
        random_index = randint(0, 8)
        self.plants[random_index] = plant_selector(choice(self.possibilities))

    def crossover(self, other_field):
        length = int(randint(0, 8))
        new_plants = self.plants[:length] + other_field.plants[length:]
        return BaseField(new_plants)

    def evaluate_function(self) -> float:
        current_fields_average = self.__float__()
        return abs(current_fields_average - Constants.POINTS_AVERAGE)

    def __str__(self):
        return ''.join([str(plant) + ' ' for plant in self.plants])

    def __float__(self):
        return sum([int(plant) for plant in self.plants]) / 9


class Potato(BasePlant):

    def __init__(self):

        super().__init__()
        self.appearance_points = 3
        self.difficulty_points = 4
        self.profit_points = 7

    def __str__(self):
        return Constants.POTATO


class Cactus(BasePlant):

    def __init__(self):

        super(Cactus, self).__init__()
        self.appearance_points = 4
        self.difficulty_points = 3
        self.profit_points = 2

    def __str__(self):
        return Constants.CACTUS


class Wheat(BasePlant):

    def __init__(self):

        super(Wheat, self).__init__()
        self.appearance_points = 5
        self.difficulty_points = 7
        self.profit_points = 9

    def __str__(self):
        return Constants.WHEAT
