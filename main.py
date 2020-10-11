import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("bot is ready.")

client.run('NzY0Nzk4NjM3NjE1NDgwODQy.X4LgPA.mWK2rfXHZfNTECa1BK934JkgDpQ')
