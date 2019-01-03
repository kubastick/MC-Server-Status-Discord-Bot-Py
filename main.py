import discord
import settings
from mcsrvstat import ServerStatus

client = discord.Client()


@client.event
async def on_ready():
    print("Bot is ready!")


@client.event
async def on_message(message):
    command: str = message.content
    if command.startswith("!sstatus "):
        # Ok, we are going to start here
        print("Executing command: {0}".format(command))
        await client.send_message(message.channel, "Ok, I'm going to check this minecraft server IP!")
        # Fetch status
        address = command.replace("!sstatus ", "")
        status = ServerStatus(address)
        response = "Players online: {0} \\ {1}\nMOTD: {2}\nVersion: {3}"
        formatted_response = response.format(status.online_players, status.max_players, status.motd, status.version)
        # And the best part - send response!
        await client.send_message(message.channel, "Here we go!")
        print("Response:\n{0}".format(formatted_response))
        await client.send_message(message.channel, formatted_response)

client.run(settings.token())
