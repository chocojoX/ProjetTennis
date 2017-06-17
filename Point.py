import numpy as np
import random


class Point:
    def __init__(self, player1, player2, service):
        self.p1 = player1
        self.p2 = player2
        self.service = service
        self.serve_advantage = 1.2


    def run(self):
        a = self.serve_advantage
        if self.service == 0:
            proba1 = a*self.p1.strength/(a*self.p1.strength + self.p2.strength)
        else:
            proba1 = self.p1.strength/(self.p1.strength + a*self.p2.strength)
        p = random.random()
        if p<proba1:
            return 0
        else:
            return 1
