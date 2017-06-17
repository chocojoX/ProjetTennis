import Set

class Match():
    def __init__(self, player1, player2, n_sets=2, verbose=2):
        self.n_sets=n_sets
        self.score = []
        self.score_sets1 = 0
        self.score_sets2 = 0
        self.p1 = player1
        self.p2 = player2
        self.first_serve = 0
        self.status = -1
        self.verbose = verbose


    def run(self):
        while self.status<0:
            current_set = Set.Set(self.p1, self.p2, verbose=self.verbose-1, first_serve=self.first_serve)
            res = current_set.run()
            set_score = [current_set.score1, current_set.score2]
            self.update_first_serve(current_set)
            self.score.append(set_score)
            if res==0:
                self.score_sets1 = self.score_sets1 + 1
            else:
                self.score_sets2 = self.score_sets2 + 1
            self.update_status()
        self.print_score()
        return self.status


    def update_status(self):
        if self.score_sets1 >= self.n_sets:
            self.status=0
        elif self.score_sets2 >= self.n_sets:
            self.status = 1
        else:
            self.status = -1


    def update_first_serve(self, current_set):
        self.first_serve = (self.first_serve + current_set.score1 + current_set.score2)%2


    def print_score(self):
        if self.status == 0:
            self.winner = self.p1
        elif self.status == 1:
            self.winner = self.p2
        else:
            print("End of match, no winner :(")
        score_to_print = ""
        for i, score in enumerate(self.score):
            score_to_print = score_to_print + " %i-%i" %(score[0], score[1])
        print("%s won %s" %(self.p1.name, score_to_print))
