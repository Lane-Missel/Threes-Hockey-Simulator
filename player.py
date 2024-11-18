"""
Author: Lane Missel
Created: November 18, 2024

File contains classes related to players in game:
"""


class SkaterSkills:
    """
    Object for storing all relevent skater skills.
    """
    def __init__(self, shooting, passing, offense, defense, skating, control, checking, blocking):

        for arg in [shooting, passing, offense, defense, skating, control, checking, blocking]:
            assert(isinstance(arg, int), "Argument must be of type 'int'")

        self.shooting = shooting
        self.passing = passing
        self.offense = offense
        self.defense = defense
        self.skating = skating
        self.control = control
        self.checking = checking
        self.blocking = blocking


class GoaltenderSkills:
    """
    Object for storing all relevent goaltending skills
    """
    def __init__(self, basic, intermediate, advanced, rebound):

        for arg in [basic, intermediate, advanced, rebound]:
            assert(isinstance(arg, int), "Argument must be of type 'int'")

        self.basic = basic
        self.intermediate = intermediate
        self.advanced = advanced
        self.rebound = rebound


class SkaterStatistics:
    """
    For tracking skater statistics each game.
    """
    def __init__(self):
        # shift information
        self.shifts = 0
        self.time_on_ice = 0

        # shots
        self.shots_taken = 0
        self.goals = 0

        # passes
        self.pass_attempts = 0
        self.passes_completed = 0
        self.assists = 0

        # defense
        self.shot_blocks = 0


class GoaltenderStatistics:
    """
    For tracking goaltender statistics each game
    """
    def __init__(self):
        self.time_on_ice = 0
        self.shots_faced = 0
        self.shots_saved = 0


class Player:
    def __init__(self, skills = None, statistics = None):
        self.skills = skills
        self.statistics = statistics

    @staticmethod
    def create(subtype = None, skills = None):
        """
        Creates the specified player
        """
        if subtype == "Sniper":
            return Sniper(skills)
    
        if subtype == "Playmaker":
            return Playmaker(skills)
        
        if subtype == "Forward":
            return Forward(skills)
        
        if subtype == "Twoway":
            return Twoway(skills)
        
        if subtype == "Defender":
            return Defender(skills)
        
        if subtype == "Goaltender":
            return Goaltender(skills)
        
        raise Exception("'subtype' not specified correctly")


class Goaltender(Player):
    def __init__(self, skills = None):
        assert(isinstance(skills, GoaltenderSkills))
        super().__init__(skills, statistics = GoaltenderStatistics())


class Skater(Player):
    """
    Class containing all skater information.
    """
    def __init__(self, skills = None):
        assert(isinstance(skills, SkaterSkills))
        super().__init__(skills, SkaterStatistics())


# Skater subtypes
class Sniper(Skater):
    """
    A skater focused on scoring goals.
    """
    def __init__(self, skills = None):
        super().__init__(skills)


class Playmaker(Skater):
    """
    A skater focused on creating scoring chances.
    """
    def __init__(self, skills = None):
        super().__init__(skills)


class Forward(Skater):
    """
    A skater focused on offensive play.
    """
    def __init__(self, skills = None):
        super().__init__(skills)


class Twoway(Skater):
    """
    A skater who balances offensive and defensive play.
    """
    def __init__(self, skills = None):
        super().__init__(skills)


class Defender(Skater):
    """
    A skater focused on defensive play.
    """
    def __init__(self, skills = None):
        super().__init__(self, skills)
        


    



