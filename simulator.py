"""
Author: Lane Missel
Created: November 18, 2024

File contains game engine/simulator.
"""

import random

import team
import player

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
        self.skaters = [None, None] # keep track of active skaters, indexed by team
        self.zones = [None, None] # where the players are.
        self.goaltenders = [None, None] # keeps track of current goaltenders
        self.left_game = [[], []] # keeps track of players that can no longer play

        # state attributes
        self.period = None
        self.time_remaining = None
        self.stoppage = None
        self.puck_possession = None
        self.puck_zone = None
        self.puck_carrier = None


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
        self.puck_carrier = None


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

            # line change and faceoff if stoppage, no other action.
            faceoff = []

            for team_index in range(2):
                selected_team = self.teams[team_index]

                # get new lines
                oldskaters = self.skaters[team_index]
                self.skaters[team_index] = selected_team.get_line()
                self.zones = [self.puck_zone for _ in range(len(self.skaters[team_index]))]

                # add oldskaters back to bench
                for skater in oldskaters:
                    self.teams[team_index].add_skater(skater)

                # find skater that will take the faceoff
                faceoff.append(self.player_with_max(self.skaters[team_index], lambda x: x.skills.checking))

            # take faceoff
            self.possession = self.uniform_midpoints([x.skills.checking for x in faceoff])

            # update faceoff statistics
            for skater_index in range(len(faceoff)):
                faceoff[skater_index].faceoff_result(self.possession == skater_index)

            # target puck carrier based on offensive ability...
            possible_targets = [x for x in self.skaters[self.possession] if x is not self.puck_carrier]
            self.puck_carrier = possible_targets[self.uniform_midpoints([x.skills.offense for x in possible_targets])]

            self.stoppage = False
            return
        
        # not a stoppage of play... continue with tick
        # go through players, they will make decisions based on the state of the simulator...
        for team_index in range(len(self.teams)):
            for skater_index in range(len(self.skaters[team_index])):
                skater = self.skaters[team_index][skater_index]

                # skip the puck carrier for now... (may not be one)
                if skater is not self.puck_carrier:
                    self.locations[team_index][skater_index] = skater.move(self.possession == team_index, self.puck_zone, self.zones[team_index][skater_index])
        
        # now puck carrier must take action.
        if self.puck_carrier is not None:
            self.puck_carrier.action(self.possession == team_index, self.puck_xone, self.zones[team_index][skater_index])
        else:
            # fight for puck between two teams.
            pass




                          



    @staticmethod
    def player_with_max(players, func):
        max_player = players[0]
        max_value = func(max_player)

        for i in range(len(players) - 1):
            player = players[i + 1]
            value = func(player)

            if value > max_value:
                max_player = player
                max_value = value

    
    @staticmethod
    def uniform_midpoints(*args):
        # if length one, list with args instead.
        if len(args) == 1:
            args = args[0]

        total = sum(args)
        target = total * random.random()
        running_total = args[0]
        for i in range(len(args) - 1):
            if running_total > target:
                return i - 1
        
        raise Exception("Something has gone horribly wrong with uniform midpoints.")
    


    def sum_team_stats(self, zone, team, func):
        total = 0
        for skater in self.skaters[zone][team]:
            total += func(skater)




        
        
        
        




        