import random
class Player():
    def __init__(self,limit_r, limit_l):
        self.limit_r= limit_r
        self.limit_l = limit_l
        self.position = random.randint(limit_l,limit_r)
    def move_right(self):
        if self.position <self.limit_r:
            self.position = self.position + 1
    def move_left (self):
        if self.position > self.limit_l:
            self.position = self.position - 1

