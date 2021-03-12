from commands.base_command  import BaseCommand
from commands.utils import player_present, start_draft
from database.create import get_player, update_player
from Models.Player import Player

class Join(BaseCommand):

    def __init__(self):
        description = "Adds self to active pug"
        params = []
        super().__init__(description, params)

    async def handle(self, params, message, client, pug):
        if pug.is_in_progress():
            await message.channel.send("Pug currently in progress! Please finish the pug or enter the results with !end [winning team number: 1 or 2] to start a new one.")
            return
        elif pug.is_free():
            pug.start_registering()

        test = len(pug.players)
        player = Player(test,str(test),"@"+str(test), 0, 0, 0, 1200) #get_player(message.author.id)

        if (player == None):
            player = Player(message.author.id, message.author.name, message.author.mention, 0, 0, 0, 1200)
            update_player(player.id, player.name, player.mention, player.games, player.wins, player.losses, player.elo)
        elif player_present(pug.players, player):
            await message.channel.send(player.mention + " already in the pug!")
            return

        if pug.add_player(player):
            await message.channel.send("Beginning game!")
            pug.start_pug()
            await start_draft(message, pug)
            return
        await message.channel.send("Added " + player.mention + " to the pug!")
        playerString = "Players:"
        for p in pug.players:
            playerString += "\n" + p.name
        await message.channel.send(playerString)