import numpy as np


class Player:
    def __init__(self, name, strength=20, serve_accuracy=20, serve_strength=20, defense=20, attack=20):
        self.strength = strength
        self.serve_accuracy = serve_accuracy
        self.serve_strength = serve_strength
        self.defense = defense
        self.attack = attack
        self.name = name
        self.confidence = 0
