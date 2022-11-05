import random
import time
from sense_hat import SenseHat
from player import Player
from berry import Berry
sense = SenseHat()

color = [255, 255, 255]
class Game():
    def __init__(self):
        self.score = 0
        self.game_over = False
        self.speed = 1
        self.berries = []
        self.player = Player(sense, 56,63)
        self.berry = Berry(color, 1, 0)
    def play(self):
        self.start()
        self.berry.display()
        while not self.game_over:
            self.player.display(0)
            self.berry.display()
            self.berry.drop()
            for event in sense.stick.get_events():
                if event.action == "pressed" and event.direction == "left":
                    self.player.move_left()
                elif event.action == "pressed" and event.direction == "right":
                    self.player.move_right()
    def start(self):
        sense.show_message("Catchem", text_colour = [255,255,255])
        # black_screen = [(0,0,0)] * 64
        # sense.set_pixels(black_screen)

        

        # while not self.game_over:
# sense.show_message("Catchem", text_colour = [255,255,255])
