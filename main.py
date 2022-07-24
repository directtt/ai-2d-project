import pygame
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from src.utils.xgb_model import XgbModel
from src.utils.cnn_model import CnnModel
from src.world import World
from src.tractor import Tractor
from src.settings import Settings
from src.constants import Constants as C
from utils.display_info import display_tile_info
from src.utils.water_all_plants import WaterAllPlants
from src.utils.collect_crops import CollectCrops
from src.utils.end_crops import EndCrops


def main():
    warnings.simplefilter(action='ignore', category=FutureWarning)
    pygame.init()

    settings = Settings()
    xgb_model = XgbModel()
    world = World(settings, xgb_model)
    cnn_model = CnnModel(world)
    cnn_model.init_model()
    tractor = Tractor("Spalinowy", "Nawóz 1", settings, 0 * settings.tile_size, 0 * settings.tile_size, C.RIGHT)

    pygame.mixer.init()
    pygame.mixer.music.load('assets/sounds/Volume Alpha 18. Sweden.wav')
    pygame.mixer.music.play(-1)

    clock = pygame.time.Clock()  # FPS purpose
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption('TRAKTOHOLIK')
    screen.blit(pygame.image.load('assets/images/display_info/img_frame.jpg'), (700, 0))

    plants_to_water = [tile for tile in world.tiles if tile.to_water == 1]
    plants_wheat = [tile for tile in world.tiles if tile.rodzaj_rosliny == 'pszenica']
    plants_potato = [tile for tile in world.tiles if tile.rodzaj_rosliny == 'ziemniak']

    water_all_plants = WaterAllPlants(tractor, world, plants_to_water)
    collect_wheat = CollectCrops(tractor, plants_wheat, (0, 0))
    end_wheat = EndCrops(tractor, (0, 0), (0, 0))
    collect_potatoes = CollectCrops(tractor, plants_potato, (0, 0))
    end_potatoes = EndCrops(tractor, (0, 0), (9, 0))

    run = True
    while run:
        clock.tick(settings.fps)
        world.draw_tiles(screen)
        world.draw_lines(screen)
        tractor.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    display_tile_info(world, screen)

        water_all_plants.update(tractor, world)

        if not C.COLLECT_WHEAT and tractor.curr_position == water_all_plants.last_cords:
            collect_wheat = CollectCrops(tractor, plants_wheat, water_all_plants.last_cords)
            C.COLLECT_WHEAT = 1
        if C.COLLECT_WHEAT:
            collect_wheat.update(tractor, world)

        if not C.END_WHEAT and tractor.curr_position == collect_wheat.last_cords:
            end_wheat = EndCrops(tractor, collect_wheat.last_cords, (0, 0))
            C.END_WHEAT = 1
        if C.END_WHEAT:
            end_wheat.update(tractor)

        if not C.COLLECT_POTATOES and tractor.curr_position == end_wheat.last_cords:
            collect_potatoes = CollectCrops(tractor, plants_potato, end_wheat.last_cords)
            C.COLLECT_POTATOES = 1
        if C.COLLECT_POTATOES:
            collect_potatoes.update(tractor, world)

        if not C.END_POTATOES and tractor.curr_position == collect_potatoes.last_cords:
            end_potatoes = EndCrops(tractor, collect_potatoes.last_cords, (9, 0))
            C.END_POTATOES = 1
        if C.END_POTATOES:
            end_potatoes.update(tractor)

        # if C.END_POTATOES:
        #     if tractor.curr_position == end_potatoes.last_cords:
        #         screen.blit(pygame.image.load('assets/images/the_end.png'), (190, 310))

        pygame.time.wait(settings.freeze_time)
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
