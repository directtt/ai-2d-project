from src.utils.astar import a_star_search
from src.tractor import Tractor


class WaterAllPlants:
    def __init__(self, tractor: Tractor, world, plants_to_water):
        self.start_cords = tractor.curr_position
        self.goals = [plant.position for plant in plants_to_water]
        self.cords_idx = tractor.find_nearest_cords(tractor.curr_position, self.goals)
        self.end_cords = self.goals[self.cords_idx]
        self.start_dir = tractor.curr_direction
        self.path = a_star_search(self.start_cords, self.end_cords, self.start_dir, world)
        self.last_cords = None

    def update(self, tractor: Tractor, world):
        if self.path:
            action = self.path.pop(0)
            tractor.update(action)
        else:
            if self.goals:
                tractor.water_plant(world, self.end_cords)
            if len(self.goals) > 1:
                self.start_cords = self.goals.pop(self.cords_idx)
                self.cords_idx = tractor.find_nearest_cords(tractor.curr_position, self.goals)
                self.end_cords = self.goals[self.cords_idx]
                self.start_dir = tractor.curr_direction
                self.path = a_star_search(self.start_cords, self.end_cords, self.start_dir, world)
            elif len(self.goals) == 1:
                self.last_cords = self.goals.pop()
                tractor.update_position()
