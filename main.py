import discord
import settings
import os
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
        try:
            status = ServerStatus(address)
        except Exception as e:
            await client.send_message(message.channel,"Sorry, but I can't find minecraft server with these ip :c")
            print("Failed to find server: {0}".format(e))
            return

        # And the best part - send response!
        # Try sending image first
        try:
            await client.send_file(message.channel, status.generate_status_image())
            return
        except Exception as err:
            print(err)
        # If sending images fails, send text message
        response = "Players online: {0} \\ {1}\nMOTD: {2}\nVersion: {3}"
        formatted_response = response.format(status.online_players, status.max_players, status.motd, status.version)

        await client.send_message(message.channel, "Here we go!")
        print("Response:\n{0}".format(formatted_response))
        await client.send_message(message.channel, formatted_response)
        status.generate_status_image()

client.run(settings.token())
