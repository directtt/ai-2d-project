class Constants:
    """ Class to represent all constants for the app """

    MOVE = "move"
    UP = [0, 1]
    DOWN = [0, -1]
    RIGHT = [1, 0]
    LEFT = [-1, 0]
    ROTATE_RIGHT = "rotate_right"
    ROTATE_LEFT = "rotate_left"
    TURN_AROUND = 'turn_around'

    # Technical terms

    WATER_STATE = 'stan_nawodnienia'
    SOIL_TYPE = 'rodzaj_gleby'
    FERTILIZATION_STATUS = 'stan_nawiezienia'
    GROWTH_LEVEL = 'stopien_rozwoju'
    PLANT_TYPE = 'rodzaj_rosliny'
    FERTILISER_TYPE = 'rodzaj_nawozu'
    TO_WATER = 'to_water'

    # Plants

    NONE = 'brak'
    CACTUS = 'kaktus'
    POTATO = 'ziemniak'
    WHEAT = 'pszenica'

    # Genetic algorithm points average

    POINTS_AVERAGE = 6.33

    # MOVING FLAGS
    COLLECT_WHEAT = 0
    END_WHEAT = 0
    COLLECT_POTATOES = 0
    END_POTATOES = 0
