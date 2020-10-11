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
async def d6(ctx):
    options = [1,2,3,4,5,6]
    await ctx.send('You rolled: ' + str(random.choice(options)))

@client.command()
async def d8(ctx):
    options = [1,2,3,4,5,6,7,8]
    await ctx.send('You rolled: ' + str(random.choice(options)))

@client.command()
async def d10(ctx):
    options = [1,2,3,4,5,6,7,8,9,10]
    await ctx.send('You rolled: ' + str(random.choice(options)))

@client.command()
async def d100(ctx):
    options = [1,2,3,4,5,6,7,8,9,10]
    await ctx.send('You rolled: ' + str((random.choice(options)*10) + random.choice(options)))

@client.command()
async def d12(ctx):
    options = [1,2,3,4,5,6,7,8,9,10,11,12]
    await ctx.send('You rolled: ' + str(random.choice(options)))

@client.command()
async def d20(ctx):
    options = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    await ctx.send('You rolled: ' + str(random.choice(options)))

@client.command()
async def roll(ctx, *, rollType):
    rollType = rollType.lower()
    getal = rollType[0: rollType.index('d')]    
    dice = rollType[rollType.index('d'):]
    teller = 1
    result = 0
    stringResult = ''
    tempResult = 0
    while teller <= int(getal):
        
        if dice == 'd4':
            tempResult = random.randint(1,4)
            result += tempResult
            if teller == int(getal):
                stringResult += str(tempResult) +' ==> dice: '
            else:
                stringResult += str(tempResult) +' + '
            
        elif dice == 'd6':
            tempResult = random.randint(1,6)
            result += tempResult
            if teller == int(getal):
                stringResult += str(tempResult) +' ==> dice: '
            else:
                stringResult += str(tempResult) +' + '
        elif dice == 'd8':
            tempResult = random.randint(1,8)
            result += tempResult
            if teller == int(getal):
                stringResult += str(tempResult) +' ==> dice: '
            else:
                stringResult += str(tempResult) +' + '
        elif dice == 'd10':
            tempResult = random.randint(1,10)
            result += tempResult
            if teller == int(getal):
                stringResult += str(tempResult) +' ==> dice: '
            else:
                stringResult += str(tempResult) +' + '
        elif dice == 'd100':
            tempResult = random.randint(1,10)*10
            result += tempResult
            if teller == int(getal):
                stringResult += str(tempResult) +' ==> dice: '
            else:
                stringResult += str(tempResult) +' + '
        elif dice == 'd12':
            tempResult = random.randint(1,12)
            result += tempResult
            if teller == int(getal):
                stringResult += str(tempResult) +' ==> dice: '
            else:
                stringResult += str(tempResult) +' + '
        elif dice == 'd20':
            tempResult = random.randint(1,20)
            result += tempResult
            if teller == int(getal):
                stringResult += str(tempResult) +' ==> dice: '
            else:
                stringResult += str(tempResult) +' + '
        else:
            result = 'Invalid dice specified!!!'
        teller += 1        
    await ctx.send('You rolled: ' + str(result)+ '\n' + '(' + stringResult + dice + ')')
        

    
                    

#@client.event
#async def on_member_join(member):
#   print("Welkom homo " + member)

#@client.event
#async def on_member_remove(member):
#    print(f' {member} has left the server.')

client.run('token here...')