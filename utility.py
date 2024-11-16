"""
Author: Lane Missel
Created: November 14, 2024

Helper functions.
"""


from player import Skater

from random import random


def faceoff(player0: Skater, player1: Skater):
    """
    Returns index of attacking team after faceoff.
    """
    assert(player0 is Skater, player1 is Skater)

    total = player0.checking + player1.checking

    return total * random() < player0.checking


def ratio(x, y):
    """
    Returns chances of x being chosen given uniform dist.
    """
    return x / (x + y)
