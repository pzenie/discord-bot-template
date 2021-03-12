from commands.base_command  import BaseCommand

class Start(BaseCommand):

    def __init__(self):
        description = "Starts a new pug"
        params = []
        super().__init__(description, params)

    async def handle(self, params, message, client, pug):
        if pug.is_free():
            pug.start_registering()
        else:
            await message.channel.send("Pug currently in progress! Please finish the pug or enter the results with !end [winning team number: 1 or 2] to start a new one.")
            return
        await message.channel.send("Pug registration started!")
