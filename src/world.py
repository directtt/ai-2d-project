import pygame

from constants import Constants
from src.tile import Tile
from utils.GeneticAlgorithm import GeneticAlgorithm


class World:
    """ Class to represent complete game board, storing Tile classes inside Sprite Group """

    def __init__(self, settings, model):
        self.settings = settings
        self.model = model
        self.world_data = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
                           [0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
                           [0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
                           [0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
                           [0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.wheat_chest = pygame.image.load('assets/images/chest_wheat.png')
        self.potatoes_chest = pygame.image.load('assets/images/chest_potato.png')
        self.rock = pygame.image.load('assets/images/cobblestone.jpg')
        self.dirt_empty = pygame.image.load('assets/images/dirt_empty.jpeg')
        self.dirt_cactus = pygame.image.load('assets/images/dirt_cactus.jpg')
        self.dirt_wheat = pygame.image.load('assets/images/dirt_wheat.jpg')
        self.dirt_potato = pygame.image.load('assets/images/dirt_potato.jpg')
        self.farmland_empty = pygame.image.load('assets/images/farmland_empty.png')
        self.farmland_cactus = pygame.image.load('assets/images/farmland_cactus.jpg')
        self.farmland_wheat = pygame.image.load('assets/images/farmland_wheat.jpg')
        self.farmland_potato = pygame.image.load('assets/images/farmland_potato.jpg')
        self.tiles = pygame.sprite.Group()  # mamy tiles jako Sprite Group, to sie przyda potem do kolizji itp.
        self.plants = GeneticAlgorithm().get_plants()
        self.create_tiles()

        wheat_chest_tile = self.get_tile(0, 0)
        wheat_chest_tile.image = pygame.transform.scale(self.wheat_chest, (settings.tile_size, settings.tile_size))
        wheat_chest_tile.cnn_image = wheat_chest_tile.image

        potato_chest_tile = self.get_tile(9, 0)
        potato_chest_tile.image = pygame.transform.scale(self.potatoes_chest, (settings.tile_size, settings.tile_size))
        potato_chest_tile.cnn_image = potato_chest_tile.image

    def create_tiles(self):
        row_count = 0
        df_idx = 0
        for row in self.world_data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    type = 'farm'  # type farm mówimy nam ogólnie, ze jest to pole uprawne, szczegóły rośliny potem
                    cost = 100000
                    stan_nawodnienia = self.model.df.iloc[df_idx][Constants.WATER_STATE]
                    rodzaj_gleby = self.model.df.iloc[df_idx][Constants.SOIL_TYPE]
                    stan_nawiezienia = self.model.df.iloc[df_idx][Constants.FERTILIZATION_STATUS]
                    stopien_rozwoju = self.model.df.iloc[df_idx][Constants.GROWTH_LEVEL]
                    rodzaj_rosliny = self.plants[df_idx].__str__()
                    rodzaj_nawozu = self.model.df.iloc[df_idx][Constants.FERTILISER_TYPE]
                    to_water = self.model.df.iloc[df_idx][Constants.TO_WATER]

                    if to_water == 0 and rodzaj_rosliny == Constants.NONE:
                        img = pygame.transform.scale(self.farmland_empty, (self.settings.tile_size, self.settings.tile_size))
                    elif to_water == 0 and rodzaj_rosliny == Constants.CACTUS:
                        img = pygame.transform.scale(self.farmland_cactus, (self.settings.tile_size, self.settings.tile_size))
                    elif to_water == 0 and rodzaj_rosliny == Constants.WHEAT:
                        img = pygame.transform.scale(self.farmland_wheat, (self.settings.tile_size, self.settings.tile_size))
                    elif to_water == 0 and rodzaj_rosliny == Constants.POTATO:
                        img = pygame.transform.scale(self.farmland_potato, (self.settings.tile_size, self.settings.tile_size))
                    if to_water == 1 and rodzaj_rosliny == Constants.NONE:
                        img = pygame.transform.scale(self.dirt_empty, (self.settings.tile_size, self.settings.tile_size))
                    elif to_water == 1 and rodzaj_rosliny == Constants.CACTUS:
                        img = pygame.transform.scale(self.dirt_cactus, (self.settings.tile_size, self.settings.tile_size))
                    elif to_water == 1 and rodzaj_rosliny == Constants.WHEAT:
                        img = pygame.transform.scale(self.dirt_wheat, (self.settings.tile_size, self.settings.tile_size))
                    elif to_water == 1 and rodzaj_rosliny == Constants.POTATO:
                        img = pygame.transform.scale(self.dirt_potato, (self.settings.tile_size, self.settings.tile_size))
                    df_idx += 1

                elif tile == 0:
                    img = pygame.transform.scale(self.rock, (self.settings.tile_size, self.settings.tile_size))
                    type = 'rock'  # podobnie j.w., na polu rock nie mamy upraw
                    cost = 1

                    stan_nawodnienia = None
                    rodzaj_gleby = None
                    stan_nawiezienia = None
                    stopien_rozwoju = None
                    rodzaj_rosliny = None
                    rodzaj_nawozu = None
                    to_water = None

                img_rect = img.get_rect()
                img_rect.x = col_count * self.settings.tile_size
                img_rect.y = row_count * self.settings.tile_size
                tile = Tile(type, col_count, len(self.world_data) - row_count - 1, img, img_rect, cost,
                            stan_nawodnienia, rodzaj_gleby, stan_nawiezienia, stopien_rozwoju, rodzaj_rosliny,
                            rodzaj_nawozu, to_water)
                self.tiles.add(tile)
                col_count += 1
            row_count += 1

    def draw_tiles(self, screen):
        self.tiles.draw(screen)

    def draw_lines(self, screen):
        for line in range(len(self.world_data)):
            pygame.draw.line(screen, (255, 255, 255), (0, line * self.settings.tile_size),
                             (self.settings.screen_height - 1, line * self.settings.tile_size))
            pygame.draw.line(screen, (255, 255, 255), (line * self.settings.tile_size, 0),
                             (line * self.settings.tile_size, self.settings.screen_height))

    def get_tile(self, x, y):
        for tile in self.tiles:
            if tile.position == (x, y):
                return tile

    def get_tile_cost(self, x, y):
        for tile in self.tiles:
            if tile.position == (x, y):
                return tile.cost