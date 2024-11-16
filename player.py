"""
Author: Lane Missel
Created: November 13, 2024

Contains the class Player for use in the Simulator class.
"""

class Player:
    def __init__(self, first, last, number, position):
        self.first = first
        self.last = last
        self.number = number
        self.position = position
        self.energy = None


class Skater(Player):
    def __init__(self, first, last, number, position, offense, defense, shooting, passing, control, skating, checking, blocking):
        super().__init__(first, last, number, position)
        self.offense = offense # abiity to make good offensive decisions
        self.defense = defense # make good defensive decisions
        self.shooting = shooting # ability to score
        self.passing = passing # pass and pass receive
        self.control = control # keep puck away from opponenent
        self.skating = skating # get and stay open
        self.checking = checking # gain possession from opposition
        self.blocking = blocking # block an opponenents shot
        self.faceoffs_taken = 0
        self.faceoffs_wins = 0
