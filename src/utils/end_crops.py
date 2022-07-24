from src.tractor import Tractor
from src.utils.bfs import BFSSearcher


class EndCrops:
    def __init__(self, tractor: Tractor, start_cords, goal):
        self.start_cords = start_cords
        self.goals = [goal]
        self.cords_idx = tractor.find_nearest_cords(tractor.curr_position, self.goals)
        self.end_cords = self.goals[self.cords_idx]
        self.start_dir = tractor.curr_direction
        self.path = BFSSearcher().search(self.start_cords, self.end_cords, self.start_dir) # a_star_search(self.start_cords, self.end_cords, self.start_dir, world)
        self.last_cords = None

    def update(self, tractor: Tractor):
        if self.path:
            action = self.path.pop(0)
            tractor.update(action)
        else:
            # tractor.collect_crop(world, self.end_cords)
            if len(self.goals) > 1:
                self.start_cords = self.goals.pop(self.cords_idx)
                self.cords_idx = tractor.find_nearest_cords(tractor.curr_position, self.goals)
                self.end_cords = self.goals[self.cords_idx]
                self.start_dir = tractor.curr_direction
                self.path = BFSSearcher().search(self.start_cords, self.end_cords, self.start_dir) # a_star_search(self.start_cords, self.end_cords, self.start_dir, world)
            elif len(self.goals) == 1:
                self.last_cords = self.goals.pop()
                tractor.update_position()

