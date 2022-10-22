import random
import time
from sense_hat import SenseHat
from player import Player
sense = SenseHat()
class Game():
    def __init__(self, score, game_over, speed, berries):
        self.score = 0
        self.game_over = False
        self.speed = 0.5
        self.berries = []
        self.player = Player(56,63)
    def play(self):
        self.start()
        

        # while not self.game_over:
sense.show_message("Catchem", text_colour = [255,255,255])