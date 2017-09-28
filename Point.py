import numpy as np
import random
from Exchange_tools import service, hit


class Point:
    def __init__(self, player1, player2, service):
        self.p1 = player1
        self.p2 = player2
        self.service = service
        if service==0:
            self.server = player1
        else:
            self.server = player2
        self.serve_advantage = 1.2


    def run(self):
        serve = service.Service(self.server)
        serve_difficulty = serve.run()

        if serve_difficulty == -1:
            print("double faute")
            return 1-self.service
        receiver = 1-self.service
        ball_difficulty = serve_difficulty
        cpt = 0
        while True:
            cpt+=1
            if receiver==0:
                player_to_hit = self.p1
            else:
                player_to_hit = self.p2

            racket_hit = hit.Hit(player_to_hit, ball_difficulty)
            ball_difficulty = racket_hit.run()
            if ball_difficulty == -1:
                # receiver missed his shot
                return 1-receiver
            receiver = 1-receiver


        #
        # if self.service == 0:
        #     proba1 = a*self.p1.strength/(a*self.p1.strength + self.p2.strength)
        # else:
        #     proba1 = self.p1.strength/(self.p1.strength + a*self.p2.strength)
        # p = random.random()
        # if p<proba1:
        #     return 0
        # else:
        #     return 1
