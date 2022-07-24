import pygame
from tile import Tile
from world import World

WHITE = (255, 255, 255)


def display_tile_info(world_map: World, screen: pygame.Surface):

    # pobranie (x, y) kursora
    (mx, my) = pygame.mouse.get_pos()\

    # obliczenie który to tile
    tile_x, tile_y = int(mx / 70), int(my / 70)

    # odczytanie info z tilea
    tile_info: Tile = world_map.get_tile(tile_x, 9 - tile_y)

    # wyświetlenie obrazu
    # 9 - y bo gdzieś w kodzie jest odwrócona oś y
    screen.blit(pygame.transform.scale(tile_info.cnn_image, (140, 140)), (735, 35))

    # init fonta
    font = pygame.font.Font('assets/images/display_info/Minecraft.ttf', 16)

    # typ tile'a
    pygame.draw.rect(screen, (139, 139, 139), pygame.Rect(724, 252, 162, 23))
    text_render = font.render(tile_info.get_type(), True, WHITE)
    screen.blit(text_render, (731, 257))

    # pozycja tile'a
    pygame.draw.rect(screen, (139, 139, 139), pygame.Rect(724, 327, 162, 23))
    text_render = font.render(str(tile_info.get_position()), True, WHITE)
    screen.blit(text_render, (731, 332))

    # to water
    pygame.draw.rect(screen, (139, 139, 139), pygame.Rect(724, 401, 162, 23))
    text_render = font.render(str(tile_info.to_water), True, WHITE)
    screen.blit(text_render, (731, 406))

    # plant type
    pygame.draw.rect(screen, (139, 139, 139), pygame.Rect(724, 475, 162, 23))
    text_render = font.render(str(tile_info.get_plant_type()), True, WHITE)
    screen.blit(text_render, (731, 480))

    # predicted plant type
    pygame.draw.rect(screen, (139, 139, 139), pygame.Rect(724, 549, 162, 23))
    text_render = font.render(str(tile_info.predicted_plant), True, WHITE)
    screen.blit(text_render, (731, 554))
