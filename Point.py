import numpy as np
import random


class Point:
    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2


    def run(self):
        proba1 = self.p1.strength/(self.p1.strength + self.p2.strength)
        p = random.random()
        if p<proba1:
            return 0
        else:
            return 1
