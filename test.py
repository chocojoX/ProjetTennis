from Player import Player
from Game import Game
from Set import Set
from Match import Match

if __name__ == "__main__":
    print("Starting test...")
    p1 = Player("Nadal", strength=22, serve_accuracy=20, serve_strength=20, defense=40, attack=20)
    p2 = Player("Federer", strength=20, serve_accuracy=20, serve_strength=20, defense=20, attack=40)

    match = Match(p1, p2, n_sets=3, verbose=2)
    result = match.run()
    print(result)
