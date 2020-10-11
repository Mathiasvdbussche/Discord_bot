import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("bot is ready.")

@client.command()
async def ping(ctf):
    await ctf.send('bong!')

@client.command()
async def roll(d6):
    await d6.send(random(1,6))

client.run('')
