from Player import Player
from Game import Game
from Set import Set

if __name__ == "__main__":
    print("Starting test...")
    p1 = Player("Nadal")
    p2 = Player("Federer")

    game = Set(p1, p2, first_serve=0, tie_break=False)
    result = game.run()
    print(result)
