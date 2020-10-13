import discord
import random

from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("bot is ready.")

@client.command()
async def ping(ctf):
    await ctf.send(f'{round(client.latency * 1000)}ms')

@client.command()
async def hi(hi):
    await hi.send("hello there!")

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                'It is decidedly so.',
                'Without a doubt.',
                'Yes – definitely.',
                'You may rely on it.',
                'As I see it, yes.',
                'Most likely.',
                'Outlook good.',
                'Yes.',
                'Signs point to yes.',
                'Reply hazy, try again.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                "Don't count on it.",
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def roll(ctx, *, rollType):
    rollType = rollType.lower()
    getal = rollType[0: rollType.index('d')]        
    dice = rollType[rollType.index('d'):]
    dice = dice.replace('d','')
    dice = int(dice)
    dices = [4,6,8,10,12,20,100]
    teller = 1
    result = 0
    stringResult = ''
    tempResult = 0
    
    if isinstance(getal,int) == False:
        getal = 1

    while teller <= int(getal):
                        
        if dice in dices:
            if dice == 100:
                tempResult = random.randint(1,dice)*10
                result += tempResult           
            else:
                tempResult = random.randint(1,dice)
                result += tempResult
        else:
            result = 'Invalid dice specified!!!'
            break
                                                                                            
        if teller == int(getal):
            stringResult += str(tempResult) +' ==> dice: '
        else:
            stringResult += str(tempResult) +' + '
        
        teller += 1

    await ctx.send('*You rolled: ' + str(result) + '*\n' + '**(' + stringResult + str(dice) + ')**')

#@client.event
#async def on_member_join(member):
#   print("Welkom homo " + member)

#@client.event
#async def on_member_remove(member):
#    print(f' {member} has left the server.')

client.run('')