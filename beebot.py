import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = 'buzz ')
token = "ODAwMTAwMzE1MTg5MzQ2MzE2.YANNfA.A3ThDWdomTzPlWMg_WEGhWnGHDw"

#positive quotes

#motivational quotes
motivational_quotes = ['\"If you cannot do great things,do small things in a great way\" -*Napoleon Hill*']

@client.event
#when the bot is ready
async def on_ready():
    print('beebot is ready.')

@client.command()
async def qotd(ctx):
    await ctx.send('A smooth sea never make a skillful sailor.')

@client.command(name='motivational')
async def motivation(ctx):
    m_quote = random.choice(motivational_quotes)
    await ctx.send(m_quote)


client.run(token)

