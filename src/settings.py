class Settings:
    """ Class to represent all static settings for the app, maybe later as .cfg """

    def __init__(self):
        # Game settings
        self.fps = 60
        self.freeze_time = 100

        # Screen settings
        self.screen_width = 910
        self.screen_height = 700

        # World settings
        self.world_size = 10

        # Tile settings
        self.tile_size = 70

        # Tractor settings
        self.tractor_speed = self.tile_size
