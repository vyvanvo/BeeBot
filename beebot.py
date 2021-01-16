import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "bee")

@client.event
#when the bot is ready
async def on_ready():
    print("beebot is ready")

client.run("ODAwMTAwMzE1MTg5MzQ2MzE2.YANNfA.A3ThDWdomTzPlWMg_WEGhWnGHDw")

