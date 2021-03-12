from commands.base_command  import BaseCommand
from commands.utils import player_matching_mention, prompt_for_pick

class Pick(BaseCommand):

    def __init__(self):
        description = "picks a player"
        params = ["playerName"]
        super().__init__(description, params)

    async def handle(self, params, message, client, pug):
        if pug.picker == None:
            await message.channel.send("No pug in draft phase!")
            return
        if message.author.id != pug.picker.id:
            await message.channel.send("Not your turn to pick " + message.author.mention + ". " + pug.picker.mention + " is picking.")
            return
        pickName = params[0]
        player = player_matching_mention(pug.draftList, pickName)
        if player == None:
            await message.channel.send("Player is not in pug or has already been drafted, pick again.")
            return
        
        if pug.picker == pug.captains[0]:
            team = 0
        else:
            team = 1
        
        pug.draft_player(player, team)
        await message.channel.send(player.mention + " has been drafted to team: " + str(team+1))
        if len(pug.draftList) == 1:
            player = pug.draftList[0]
            pug.draft_player(player, 1 - team)
            await message.channel.send(player.mention + " has been drafted to team: " + str(1 - team+1))
            s = "Pug is starting!\nTeam 1 (" + str(pug.teams[0].elo) + "):"
            for p in pug.teams[0].members:
                s += "\n" + p.mention
            s += "\nTeam 2 (" + str(pug.teams[1].elo) + "):"
            for p in pug.teams[1].members:
                s += "\n" + p.mention
            s + "\n After the pug please report the result by using the !done [winning team number (1 or 2)] command"
            await message.channel.send(s)
            return
        if team == 0:
            pug.picker = pug.captains[1 - team]
        await prompt_for_pick(message, pug.draftList, pug.picker)