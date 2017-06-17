from Player import Player
from Game import Game
from Set import Set
from Match import Match

if __name__ == "__main__":
    print("Starting test...")
    p1 = Player("Nadal")
    p2 = Player("Federer")

    match = Match(p1, p2, n_sets=2, verbose=2)
    result = match.run()
    print(result)
