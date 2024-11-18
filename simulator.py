"""
Author: Lane Missel
Created: November 18, 2024

File contains game engine/simulator.
"""

import team

class Simulator:
    def __init__(self, zones = 3, config = None):
        self.config = {
            "periods": 3,
            "period_length": 1200,
            "overtime_length": None,
        }

        # update configuration if specified.
        if isinstance(config, dict):
            for key in config.keys():
                self.config[key] = config[key]

        self.teams = [None, None] # keeps track of team objects

        # these attributes all store players that have been temperarily removed from the Team object.
        self.skaters = [([], []) for _ in range(zones)] # keep track of active skaters
        self.goaltenders = [None, None] # keeps track of current goaltenders
        self.left_game = [[], []] # keeps track of players that can no longer play

        # state attributes
        self.period = None
        self.time_remaining = None
        self.stoppage = None
        self.puck_possession = None
        self.puck_zone = None


    def load_teams(self, teams):
        assert(isinstance(teams, list))
        assert(len(teams) == 2)
        
        for i in range(2):
            assert(isinstance(teams[i], team.Team))
            self.teams[i] = teams[i]

    
    def reset(self):
        self.period = 0
        self.time_remaining = None
        self.stoppage = None
        self.puck_possession = None
        self.puck_zone = None


    def simulate_game(self):
        # check necessary state
        assert(self.period == 0)
        if self.teams[0] is None:
            raise Exception("Teams have not been added.")
        
        # start simulation
        while self.period is not None:
            self.period += 1
            self.time_remaining = self.config["period_length"]

            self.simulate_period()


    def simulate_period(self):
        self.stoppage = True
        while self.time_remaining > 0:
            self.time_remaining -= 1
            self.simulate_tick()


    def simulate_tick(self):
        if self.stoppage(self):
            # Change lines
            players = [None, None]
            for i in range(2):
                players[i] = self.teams[0].get_line()

                # add teams back to bench
                for i in range(3):
                    for skater in self.skaters[i]:
                        self.teams[i].add_skater(skater)
                    self.skaters[i] = []

            # take faceoff
            


            self.stoppage = False
            return


        # simulate a step of the simulation



        
        
        
        




        