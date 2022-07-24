import tensorflow as tf
import os
import random
import pygame
import numpy as np
from tile import Tile
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


class CnnModel:
    """ Class to represent trained CNN model that predicts plant type from images """

    def __init__(self, world):
        self.model = tf.keras.models.load_model('assets/cnn_model')
        self.cactus_images = os.listdir('assets/images/neural_network/validation/cactus')
        self.potato_images = os.listdir('assets/images/neural_network/validation/potato')
        self.wheat_images = os.listdir('assets/images/neural_network/validation/wheat')
        self.cactuses = [tile for tile in world.tiles if tile.rodzaj_rosliny == 'kaktus']
        self.potatoes = [tile for tile in world.tiles if tile.rodzaj_rosliny == 'ziemniak']
        self.wheat = [tile for tile in world.tiles if tile.rodzaj_rosliny == 'pszenica']
        self.IMG_SHAPE = (256, 256)

    def init_model(self):

        cactus: Tile
        for cactus in self.cactuses:
            i = random.randint(0, len(self.cactus_images) - 1)
            cactus_img = self.cactus_images[i]
            img_path = 'assets/images/neural_network/validation/cactus/' + cactus_img
            cactus.cnn_image = pygame.image.load(img_path)

            img_model = tf.keras.preprocessing.image.load_img(img_path, target_size=self.IMG_SHAPE)
            prediction = self.make_prediction(img_model)
            cactus.predicted_plant = self.decode_prediction(prediction)

        potato: Tile
        for potato in self.potatoes:
            potato: Tile
            i = random.randint(0, len(self.potato_images) - 1)
            potato_img = self.potato_images[i]
            img_path = 'assets/images/neural_network/validation/potato/' + potato_img
            potato.cnn_image = pygame.image.load(img_path)

            img_model = tf.keras.preprocessing.image.load_img(img_path, target_size=self.IMG_SHAPE)
            prediction = self.make_prediction(img_model)
            potato.predicted_plant = self.decode_prediction(prediction)

        wheat: Tile
        for wheat in self.wheat:
            i = random.randint(0, len(self.wheat_images) - 1)
            wheat_img = self.wheat_images[i]
            img_path = 'assets/images/neural_network/validation/wheat/' + wheat_img
            wheat.cnn_image = pygame.image.load(img_path)

            img_model = tf.keras.preprocessing.image.load_img(img_path, target_size=self.IMG_SHAPE)
            prediction = self.make_prediction(img_model)
            wheat.predicted_plant = self.decode_prediction(prediction)

    def make_prediction(self, img_model):
        X = tf.keras.preprocessing.image.img_to_array(img_model)
        X = np.expand_dims(X, axis=0)
        X = X / 255.0
        prediction = self.model.predict(X, verbose=0)

        return prediction

    def decode_prediction(self, prediction):
        prediction = np.argmax(prediction, axis=1)

        if prediction[0] == 0:
            return 'kaktus'
        elif prediction[0] == 1:
            return 'ziemniak'
        elif prediction[0] == 2:
            return 'pszenica'
