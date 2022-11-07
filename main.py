import discord
import random
import os
from discord.ext import commands
from rps import rps
from dotenv import load_dotenv

load_dotenv()

colors = ['🔴','🟠','🟡','🟢',
          '🔵','🟣','🟤','⚫','⚪']

# client = commands.Bot(intents=discord.Intents.default(), command_prefix='!')

intents = discord.Intents.default()
# ** need this, if not have this Rabbot will not response your command **
intents.message_content = True
client = discord.Client(intents=intents)

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print("The Rabbot is now ready!")

@client.command()
async def color(ctx):
    a = random.randrange(0, 10)
    await ctx.send("สีนำโชคประจำวันของคุณคือ {}".format(colors[a]))

@client.command()
async def command(ctx):
    text = "You can use these commands\n !hello = say hello to Rabbot.\n !dice = roll your dice.\n "
    text += "!rps = play rock paper scissor (still in progess)"
    await ctx.send(text)

@client.command()
async def hello(ctx):  # when u type !hello in discord, it run hello function
    await ctx.send("สวัสดีเราคือ Rabbot")

@client.command()
async def dice(ctx):
    await ctx.send("แต้ม 🎲 ของคุณคือ: {} ".format(random.randrange(0, 7)))

@client.command()
async def rps(ctx, values: int):
    await ctx.send("0 = rock, 1 = scissor, 2 = paper")
    await ctx.send(rps(int(values)))

client.run(os.getenv("TOKEN"))
