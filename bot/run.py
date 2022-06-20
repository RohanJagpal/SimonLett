import os
import discord
from discord.enums import ActivityType
from discord.ext import commands
import random
from dotenv import load_dotenv

load_dotenv()

INITIAL_EXTENTIONS = ["emails"]
UPDATE_CHANNEL = 887933735004176414

# load greetings and triggers
with open("data/triggers.txt") as f:
    GREETING_TRIGGERS = set()
    GREETING_TRIGGERS.add(i.rstrip())

with open("data/greetings.txt"):
    GREETINGS = set()
    for i in f:
        GREETINGS.add(i.rstrip())


bot = commands.Bot("gh!")

if __name__ == "__main__":
    for ext in INITIAL_EXTENTIONS:
        bot.load_extension(ext)
        print(ext + " extension loaded")

### Commands ###

### Events ###
@bot.event
async def on_ready():
    print("Simon Lett has logged in and is ready to game!")
    activity = discord.Activity(name="you learn", type=ActivityType.watching)
    await bot.change_presence(activity=activity, status=discord.Status.online)


@bot.event
async def on_message(ctx):
    if ctx.content.lower() in GREETING_TRIGGERS and random.randint(0, 4) == 0:
        await ctx.channel.send(random.choice(GREETINGS))

    await bot.process_commands(ctx)


bot.run(os.getenv("DISCORD_TOKEN"))
