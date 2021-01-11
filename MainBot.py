import os

import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("GUILD_NAME")

# Enable intents so that we have access to the member list and so on from the bot!
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Currently connected guilds:")
    for guild in client.guilds:
        print("""{name}
         \t * id = {id}
         \t * owner = {owner}
         \t * Online users = {onlineUsers} """.format(name=guild.name, id=guild.id, owner=guild.owner, onlineUsers=len([
             # One liner that gets the online count of people
             memberOnline for memberOnline in guild.members if memberOnline.status == discord.Status.online])))
        print("Lista de usuarios")
        for member in guild.members:
            if member.status is discord.Status.online:
                print(f"- {member.name}")


client.run(TOKEN)