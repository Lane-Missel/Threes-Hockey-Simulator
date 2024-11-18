"""
Author: Lane Missel
Created: November 18, 2024

File contains Team class.
"""

import player

class Team:
    def __init__(self):
        self.skaters = []
        self.goaltenders = []


    def add_skater(self, skater):
        assert(isinstance(skater, player.Skater))
        self.skaters.append(skater)


    def add_goaltender(self, goaltender):
        assert(isinstance(goaltender, player.Goaltender))
        self.goaltenders.append(goaltender)


    def get_line(self):
        skaters = []
        for _ in range(3):
            skaters.append(self.skaters.pop(0))
        return skaters

