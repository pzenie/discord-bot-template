import math
from random                 import randint

async def start_draft(message, pug):
    captains = pick_captains(pug.players)
    captain1 = captains[0]
    captain2 = captains[1]
    pug.draftList = pug.players
    pug.draft_player(captain1, 0)
    pug.draft_player(captain2, 1)
    pug.captains = (captain1, captain2)
    pug.picker = captain1
    await message.channel.send("Team 1 captain: " + captain1.mention + ", Team 2 captain: " + captain2.mention)
    await prompt_for_pick(message, pug.draftList, pug.picker)

def player_matching_mention(players, mention):
    for p in players:
        if p.mention == mention:
            return p
    return None

async def prompt_for_pick(message, availablePlayers, picker):
    prompt = "It's " + picker.mention + " pick! Use !pick [playername] to pick a player. Available players:"
    for p in availablePlayers:
        prompt += "\n" + p.name + " Elo: " + str(p.elo)
    await message.channel.send(prompt)

def pick_captains(players):
    players.sort(key=lambda player: player.elo, reverse=True)
    captain1 = randint(0, 5)
    if captain1 + 1 < 6:
        captain2 = captain1 + 1
    else:
        captain2 = captain1 - 1
    return (players[captain1], players[captain2])

def player_present(players, player):
    for p in players:
        if p.name == player.name:
            return True
    return False

# Function to calculate the Probability 
def Probability(rating1, rating2): 
  
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400)) 
  
  
# Function to calculate Elo rating 
# K is a constant. 
# d determines whether 
# Player A wins or Player B.  
def EloRating(Ra, Rb, K, d): 
   
  
    # To calculate the Winning 
    # Probability of Player B 
    Pb = Probability(Ra, Rb) 
  
    # To calculate the Winning 
    # Probability of Player A 
    Pa = Probability(Rb, Ra) 
  
    # Case -1 When Player A wins 
    # Updating the Elo Ratings 
    if (d == 1) : 
        Ra = Ra + K * (1 - Pa) 
        Rb = Rb + K * (0 - Pb) 
      
  
    # Case -2 When Player B wins 
    # Updating the Elo Ratings 
    else : 
        Ra = Ra + K * (0 - Pa) 
        Rb = Rb + K * (1 - Pb) 
      
  
    print("Updated Ratings:-") 
    print("Ra =", round(Ra, 6)," Rb =", round(Rb, 6)) 