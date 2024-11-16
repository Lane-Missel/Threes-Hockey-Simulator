"""
Author: Lane Missel
Created: November 13, 2024

Contains the 3 on 3 hockey simulator/engine.
"""

from player import Skater
from team import Team
import utility

class Simulator:
    def __init__(self, config: dict):
        """
        Returns an instance of Simulator.
        """
        # class attributes.
        self.teams = [None, None]
        self.score = None
        self.time_remaining = None
        self.zone = None # 0,1, 2with 0 representing the goal which is being attacked.
        self.possession = None
        self.attacking: Team = None
        self.defending: Team = None
        self.puck_carrier: Skater = None
        
        # default valus for simulator.
        self.config = {
            "periods": 3,
            "period_length": 1200,
            "overtime": False,
            "num_zones": 3
        }

        # update configuration values if provided.
        #! should validate user inputs.
        if self.config is not None:
            for key in config.keys():
                self.config[key] = config[key]

    def lead(self, reference_index):
        """
        Returns goal differencial for specified team.
        """
        diff = self.score[0] - self.score[1]
        return diff if reference_index == 0 else -diff


    def load_teams(self, teams: list):
        """
        Updates the teams in the simulator.
        """
        assert(teams is not None)
        assert(len(teams) == 2)
        assert(teams[0] is Team)
        assert(teams[1] is Team)

        self.teams = teams


    def simulate_game(self):
        """
        Simulates a game with the teams provided last by self.new_game().
        """
        assert(self.period is not None)

        # play specified amount of periods
        for i in range(self.config["periods"]):
            self.simulate_period(overtime = False)

        # play overtime if necessary
        if self.config["overtime"]:
            while self.score[0] - self.score[1] == 0:
                self.simulate_period(overtime = True)


    def simulate_period(self, overtime = False):
        """
        Simulates a period within the simulator.
        """
        self.time_remaining = self.config["period_length"]
        self.zone = self.config["num_zones"] // 2 # midice

        while self.time_remaining > 0:
            self.simulate_shift(overtime)


    def simulate_shift(self, overtime = False):
        """
        Simulates a shift within the simulator.
        """
        shift_start = self.time_remaining
        
        # set team lines
        self.teams[0].set_line(self.lead(0), self.zone)
        self.teams[1].set_line(self.lead(1), self.config["num_zones"] - self.zone)

        # get players taking faceoff.
        faceoff0: Skater = self.teams[0].get_faceoff()
        faceoff1: Skater = self.teams[1].get_faceoff()

        # decide attacking team.
        self.possession = utility.faceoff(faceoff0, faceoff1)

        # reassign teams
        self.attacking = self.teams[self.possession]
        self.defending = self.teams[not self.possession]

        # update faceoff stats
        winner = faceoff0 if not self.possession else faceoff1
        winner.faceoff_wins += 1

        for faceoff in [faceoff0, faceoff1]:
            faceoff.faceoffs_taken += 1

        # give puck to one of the other teammates.
        self.puck_carrier = None

        # simulate possessions during shift...
        ongoing = True
        while ongoing and self.time_remaining > 0:
            ongoing = self.simulate_possession(overtime)


    def simulate_possession(self, overtime = False) -> bool:
        """
        Simulates one possession within the simulator.
        """
        ### attacking team must attempt to move up unless in attacking zone
        if self.zone > 0:
            # use mutlitue of difference to determine what to do.
            defense = self.defending.zone_defense()
            offense = self.attacking.zone_offense()

            # can try to stay in zone, skate it up, or pass it up.
            stay = utility.ratio(self.)
            


        # team will attempt to score



    def simulate_tick(self, overtime = False):
        """
        Takes one step within the simulator.
        """
