"""
Author: Lane Missel
Created: November 13, 2024

Contains the class Line for use in the Simulator class.
"""

from player import Skater

class Line:
    def __init__(self, skaters: list):
        self.skaters = skaters

    
    def get_faceoff(self) -> Skater:
        """
        Returns best faceoff taker on the line.
        """
        faceoff: Skater = self.skaters[0]
        skater: Skater = None

        # choose skater based on stick_checking ability
        for skater in self.skaters[1:]:
            if skater.checking > faceoff.checking:
                faceoff = skater

        return faceoff