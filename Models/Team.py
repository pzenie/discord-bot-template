class Team:

    def __init__(self, members=[], elo=0):
        # The first member is the captain
        self.members = members
        self.elo = 0

    def add_member(self, player):
        self.members.append(player)
        self.update_elo()

    def update_elo(self):
        totalElo = 0
        for p in self.members:
            totalElo += p.elo
        self.elo = totalElo / len(self.members)