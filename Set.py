import numpy as np
from Game import Game
import time


class Set:
    def __init__(self, player1, player2, first_serve=0, tie_break=False):
        self.tie_break=tie_break
        self.p1 = player1
        self.p2 = player2
        self.score1 = 0
        self.score2 = 0
        self.first_serve = first_serve
        self.service = first_serve
        self.status = -1  #-1 is ongoing, -0.5 is tie_break 0 is won by player1, 1 is won by player2


    def run(self):
        while self.status <0:
            self.service = (self.score1 + self.score2 + self.first_serve) % 2
            game = Game(self.p1, self.p2, service=self.service)
            res = game.run()
            if res == 0:
                self.score1 = self.score1 + 1
            else:
                self.score2 = self.score2 + 1
            self.update_status()
            print("%i - %i" %(self.score1, self.score2))
            time.sleep(0.5)
        return self.status


    def update_status(self):
        if max(self.score1, self.score2)<6:
            self.status = -1
        elif min(self.score1, self.score2)>4:
            if self.tie_break:
                if self.score1==7:
                    self.status = 0
                elif self.score2==7:
                    self.status = 1
                elif self.score1==6 and self.score2==6:
                    self.status = -0.5
                else:
                    self.status = -1

            else:
                if self.score1>self.score2-1:
                    self.status = 0
                elif self.score2>self.score1-1:
                    self.status = 1
                else:
                    self.status = -1
        elif self.score1==6:
            self.status = 0
        elif self.score2==6:
            self.status = 1
        else:
            print("Error in update_status of set...")
