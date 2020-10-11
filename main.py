import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("bot is ready.")

@client.command()
async def ping(ctx):
    await ctx.send('pong!')    

client.run('NzY0Nzk4NjM3NjE1NDgwODQy.X4LgPA.YTZkSXqT219CZYOeTpRHnYBjWDY')
