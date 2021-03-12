from Models.Team import Team
from Models.Player import Player

class Pug:

    def __init__(self, max_size=6):
        self.teams = (Team(), Team())
        self.players = []
        self.max_size = max_size
        #0 = non active, 1 = active / registering, 2 = game in progress
        self.isActive = 0
        self.draftList = []
        self.captains = None
        self.picker = None

    def add_player(self, player):
        self.players.append(player)
        if len(self.players) == self.max_size:
            self.start_pug()
            return True
        return False

    def remove_player(self, player):
        if not player in self.players:
            return
        self.players.remove(player)
    
    def draft_player(self, player, team):
        self.teams[team].add_member(player)
        self.draftList.remove(player)
    
    def start_registering(self):
        self.isActive = 1

    def start_pug(self):
        self.isActive = 2

    def end_pug(self):
        self.isActive = 0

    def is_registering(self):
        return self.isActive == 1

    def is_in_progress(self):
        return self.isActive == 2
    
    def is_free(self):
        return self.isActive == 0