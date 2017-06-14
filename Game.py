import numpy as np
import time
from Point import Point


class Game:
    def __init__(self, player1, player2, service=0, verbose=True):
        self.score1 = 0
        self.score2 = 0
        self.p1 = player1
        self.p2 = player2
        self.order = [0, 15, 30, 40]
        self.n_points = len(self.order)
        self.status = -1
        self.service = 0
        self.verbose = verbose

    def run(self):
        while self.status==-1:
            point = Point(self.p1, self.p2)
            res = point.run()
            if res==0:
                self.score1 += 1
            else:
                self.score2 += 1
            self.update_status()
            if self.verbose:
                time.sleep(0.5)
                self.print_score()
        if self.score1 >self.score2:
            return 0
        else:
            return 1


    def print_score(self):
        if self.status==-1:
            if self.score1<self.n_points and self.score2<self.n_points:
                s1 = self.order[self.score1]
                s2 = self.order[self.score2]
                print("%i-%i" %(s1, s2))
            else:
                #Score above 40
                if self.score1==self.score2:
                    print("40-A")
                elif self.score1>self.score2:
                    print("Advantage %s" %self.p1.name)
                else:
                    print("Advantage %s" %self.p2.name)
        elif self.status == 0:
            print("Game %s" %self.p1.name)
        else:
            print("Game %s" %self.p2.name)


    def update_status(self):
        # Sets game state to 0 if player 1 has won the game, 1 if player 2 has won the game, -1 if the game is not yet finished
        if self.score1>self.n_points-1 and self.score1>self.score2+1:
            self.state = 0

        elif self.score2>self.n_points-1 and self.score2>self.score1+1:
            self.state = 1

        else:
            self.state = -1
