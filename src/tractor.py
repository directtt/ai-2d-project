import pygame
import numpy as np
from scipy import spatial
from pygame.sprite import Sprite
from constants import Constants as C


class Tractor(Sprite):
    """ Class to represent our agent """

    def __init__(self, engine, fertilizer, settings, initial_x, initial_y, initial_direction):
        super().__init__()
        self.settings = settings
        self.image = pygame.transform.scale(pygame.image.load('assets/images/tractor/tractor-transparent-right.png'),
                                            (self.settings.tile_size - 1, self.settings.tile_size - 1))
        self.rect = self.image.get_rect()
        self.rect.x = initial_x
        self.rect.y = initial_y
        self.curr_position = (round(self.rect.x / self.settings.tile_size),
                              self.settings.world_size - round(self.rect.y / self.settings.tile_size) - 1)
        self.curr_direction = initial_direction  # wektor w ukladzie wspolrzednych wskazujacy kierunek traktora
        self.engine = engine
        self.fertilizer = fertilizer

    def turn_right(self):
        if self.curr_direction == C.UP:
            self.curr_direction = C.RIGHT
            self.image = pygame.transform.scale(
                pygame.image.load('assets/images/tractor/tractor-transparent-right.png'),
                (self.settings.tile_size - 1, self.settings.tile_size - 1))
        elif self.curr_direction == C.RIGHT:
            self.curr_direction = C.DOWN
            self.image = pygame.transform.scale(
                pygame.image.load('assets/images/tractor/tractor-transparent-down.png'),
                (self.settings.tile_size - 1, self.settings.tile_size - 1))
        elif self.curr_direction == C.DOWN:
            self.curr_direction = C.LEFT
            self.image = pygame.transform.scale(
                pygame.image.load('assets/images/tractor/tractor-transparent-left.png'),
                (self.settings.tile_size - 1, self.settings.tile_size - 1))
        elif self.curr_direction == C.LEFT:
            self.curr_direction = C.UP
            self.image = pygame.transform.scale(
                pygame.image.load('assets/images/tractor/tractor-transparent-up.png'),
                (self.settings.tile_size - 1, self.settings.tile_size - 1))

        pygame.time.wait(self.settings.freeze_time)  # bez tego sie kreci jak hot-wheels

    def turn_left(self):
        if self.curr_direction == C.UP:
            self.curr_direction = C.LEFT
            self.image = pygame.transform.scale(
                pygame.image.load('assets/images/tractor/tractor-transparent-left.png'),
                (self.settings.tile_size, self.settings.tile_size))
        elif self.curr_direction == C.LEFT:
            self.curr_direction = C.DOWN
            self.image = pygame.transform.scale(
                pygame.image.load('assets/images/tractor/tractor-transparent-down.png'),
                (self.settings.tile_size, self.settings.tile_size))
        elif self.curr_direction == C.DOWN:
            self.curr_direction = C.RIGHT
            self.image = pygame.transform.scale(
                pygame.image.load('assets/images/tractor/tractor-transparent-right.png'),
                (self.settings.tile_size, self.settings.tile_size))
        elif self.curr_direction == C.RIGHT:
            self.curr_direction = C.UP
            self.image = pygame.transform.scale(
                pygame.image.load('assets/images/tractor/tractor-transparent-up.png'),
                (self.settings.tile_size, self.settings.tile_size))

        pygame.time.wait(self.settings.freeze_time)  # bez tego sie kreci jak hot-wheels

    def turn_around(self):
        self.turn_right()
        self.turn_right()

    def move(self):
        self.rect.x += self.curr_direction[0] * self.settings.tractor_speed
        self.rect.y -= self.curr_direction[1] * self.settings.tractor_speed

        if self.rect.x <= 0:
            self.rect.x = 1  # musi być 1, bo przy idk czemu 0 się buguje i nie może się obrócić
        if self.rect.y <= 0:
            self.rect.y = 1  # j.w.
        if self.rect.x >= self.settings.screen_width - self.settings.tile_size:
            self.rect.x = self.settings.screen_width - self.settings.tile_size
        if self.rect.y >= self.settings.screen_height - self.settings.tile_size:
            self.rect.y = self.settings.screen_height - self.settings.tile_size

        pygame.time.wait(self.settings.freeze_time)  # bez tego sie kreci jak hot-wheels

    def water_plant(self, world, position):
        plant = world.get_tile(position[0], position[1])
        plant.to_water = 0

        if plant.rodzaj_rosliny == 'brak':
            plant.image = pygame.transform.scale(world.farmland_empty,
                                                 (self.settings.tile_size, self.settings.tile_size))
        elif plant.rodzaj_rosliny == 'kaktus':
            plant.image = pygame.transform.scale(world.farmland_cactus,
                                                 (self.settings.tile_size, self.settings.tile_size))
        elif plant.rodzaj_rosliny == 'pszenica':
            plant.image = pygame.transform.scale(world.farmland_wheat,
                                                 (self.settings.tile_size, self.settings.tile_size))
        elif plant.rodzaj_rosliny == 'ziemniak':
            plant.image = pygame.transform.scale(world.farmland_potato,
                                                 (self.settings.tile_size, self.settings.tile_size))

    def collect_crop(self, world, position):
        plant = world.get_tile(position[0], position[1])
        plant.image = pygame.transform.scale(world.farmland_empty,
                                             (self.settings.tile_size, self.settings.tile_size))

    def find_nearest_cords(self, curr_cords, cords_lst):
        # https://stackoverflow.com/questions/39107896/efficiently-finding-the-closest-coordinate-pair-from-a-set-in-python
        tree = spatial.KDTree(cords_lst)
        return tree.query(curr_cords)[1]

    # moze sie jeszcze kiedys przyda
    # def water_plants(self, plants, plants_lst, goals, world):
    #     hit_list = pygame.sprite.spritecollide(sprite=self, group=plants, dokill=False)
    #
    #     print(goals)
    #
    #     for plant in hit_list:
    #         if plant.rodzaj_rosliny == 'brak':
    #             plant.image = pygame.transform.scale(world.farmland_empty, (self.settings.tile_size, self.settings.tile_size))
    #         elif plant.rodzaj_rosliny == 'kaktus':
    #             plant.image = pygame.transform.scale(world.farmland_cactus, (self.settings.tile_size, self.settings.tile_size))
    #         elif plant.rodzaj_rosliny == 'pszenica':
    #             plant.image = pygame.transform.scale(world.farmland_wheat, (self.settings.tile_size, self.settings.tile_size))
    #         elif plant.rodzaj_rosliny == 'ziemniak':
    #             plant.image = pygame.transform.scale(world.farmland_potato, (self.settings.tile_size, self.settings.tile_size))
    #
    #         if plant.position in goals:
    #             goals.remove(plant.position)


        # if pygame.sprite.spritecollideany(self, obstacles):
        #     print(len(obstacles))
            # self.rect.x -= self.curr_direction[0] * self.settings.tile_size  # no to troche prymitywne jest, ale
            # self.rect.y += self.curr_direction[1] * self.settings.tile_size  # jak wejdzie na kolizje to cofamy ruch
                                                                             # w przyszlosci mozna zmienic

    def update_position(self):
        self.curr_position = (round(self.rect.x / self.settings.tile_size),
                              self.settings.world_size - round(self.rect.y / self.settings.tile_size) - 1)

    def update(self, action):
        self.update_position()

        if action == C.ROTATE_RIGHT and self.rect.x:
            self.turn_right()
        elif action == C.ROTATE_LEFT:
            self.turn_left()
        elif action == C.TURN_AROUND:
            self.turn_around()
        elif action == C.MOVE:
            self.move()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def hydrate(self, tile):
        if tile.hydration < tile.plant.min_hydration:
            tile.hydration = tile.plant.max_hydration

    def collect(self, tile):
        if tile.plant.growth >= 0.75:
            tile.remove_plant()

    def cut(self, tile):
        tile.remove_plant()

    def plant(self, tile, plant):
        if not tile.plant:
            tile.add_plant(plant)

    def fertilize(self, tile):
        if not tile.is_fertilized:
            tile.is_fertilized = True
            tile.fertilizer = tile.plant.fertilizer
