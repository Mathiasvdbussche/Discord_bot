import discord

from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("bot is ready.")

@client.command()
async def ping(ctf):
    await ctf.send('bong!')

@client.event
async def on_member_join(member):
    print("Welkom homo " + member)

@client.event
async def on_member_remove(member):
    print(f' {member} has left the server.')


client.run('')

