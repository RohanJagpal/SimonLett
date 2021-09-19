import os
import discord
from discord.enums import ActivityType
from discord.ext import commands
import random
from dotenv import load_dotenv

load_dotenv()

#INITIAL_EXTENTIONS = ["emails", "twitter"]
INITIAL_EXTENTIONS = []
UPDATE_CHANNEL = 887933735004176414
GREETING_TRIGGERS = {
    "hello", "hi", "yo"
}
GREETINGS = [
    "Stop socialising! Get back to studying :face_with_symbols_over_mouth:",
    "Hello! Hope the A-Levels are going well :D",
    "You just posted cringe",
    "ur expelled nerd"
]
bot = commands.Bot('gh!')

if __name__ == "__main__":
    for ext in INITIAL_EXTENTIONS:
        bot.load_extension(ext)

@bot.event
async def on_ready():
    print('Simon Lett has logged in and is ready to game!')
    activity = discord.Activity(
        name="you learn",
        type=ActivityType.watching
    )
    await bot.change_presence(activity=activity, status=discord.Status.online)

@bot.event
async def on_message(ctx):
    if (ctx.content.lower() in GREETING_TRIGGERS and
        random.randint(0,4) == 0):
            await ctx.channel.send(random.choice(GREETINGS))

    await bot.process_commands(ctx)
    
bot.run(os.getenv("DISCORD_TOKEN"))
