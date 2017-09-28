from Player import Player
from Game import Game
from Set import Set
from Match import Match

if __name__ == "__main__":
    print("Starting test...")
    p1 = Player("Nadal", strength=22)
    p2 = Player("Federer", strength=20)

    match = Match(p1, p2, n_sets=3, verbose=2)
    result = match.run()
    print(result)
