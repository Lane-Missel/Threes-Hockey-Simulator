"""
Author: Lane Missel
Created: November 13, 2024

Contains the class Team for use in the Simulator class.
"""

from line import Line

class Team:
    def __init__(self, skaters, goaltenders):
        self.skaters = skaters
        self.goaltenders = goaltenders


    def get_line(self, lead: int, zone: int) -> Line:
        """
        Returns the line for the next shift.
        """
        # depending on lead, and location, put out best players for next shift.
        pass