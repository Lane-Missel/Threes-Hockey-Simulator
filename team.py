"""
Author: Lane Missel
Created: November 13, 2024

Contains the class Team for use in the Simulator class.
"""

from random import random

class Team:
    def __init__(self, skaters, goaltenders):
        self.bench = skaters
        self.goaltenders = goaltenders
        self.active = None


    def zone_defense(self):
        """
        Returns scaled random value for zone defense.
        """
        self._uniform_stat(sum(x.skating + x.defense for x in self.active))


    def zone_offense(self):
        """
        Returns scaled random value for zone offense.
        """
        self._uniform_stat(sum(x.skating + x.offense for x in self.active))
        


    def set_line(self, lead: int, zone: int):
        """
        Returns the line for the next shift.
        """
        # depending on lead, and location, put out best players for next shift.
        last = self.active
        self.active = self.bench[0:2]
        self.bench += last


    def _uniform_stat(self, values):
        half = values / 2
        return half + half * random()
