class Player:

    def __init__(self, id, name, mention, games=0, wins=0, losses=0, elo=1200):
        # The first member is the captain
        self.id = id
        self.name = name
        self.mention = mention
        self.games = games
        self.wins = wins
        self.losses = losses
        self.elo = elo

    def add_win(self, elo):
        self.games+=1
        self.wins+=1
        self.elo = elo

    def add_loss(self, elo):
        self.games+=1
        self.losses+=1
        self.elo = elo