import os
import discord
from discord.enums import ActivityType
from discord.ext import commands#, tasks
#import win32com.client
import random
#import youtube_dl
from dotenv import load_dotenv

load_dotenv()

#initial_extensions = ["emails", "twitter"]
UPDATE_CHANNEL = 887933735004176414
initial_extensions = []
greeting_triggers = [
    "hello", "hi", "yo"
]
greetings = [
    "Stop socialising! Get back to studying :face_with_symbols_over_mouth:",
    "Hello! Hope the A-Levels are going well :D",
    "",
    "You just posted cringe",
    "ur expelled nerd"
]
bot = commands.Bot('gh!')

if __name__ == "__main__":
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    print('Simon Lett has logged in and is ready to game!')
    activity = discord.Activity(
        name="you learn",
        type=ActivityType.watching
    )
    await bot.change_presence(activity=activity, status=discord.Status.online)
    #await bot.get_channel(887930860463083564).send('im mad u r all epexelled :rage:')
    """
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)
    messages = inbox.Items
    email = None
    messageIter = 0
    while email == None:
        message = messages[messageIter]
        if str(message.Sender) == "Simon Lett":
            email = message
        messageIter += 1
    if email == None:
        return
    body_content = email.body
    print(body_content)
    upd_channel = await bot.get_channel(UPDATE_CHANNEL)
    if body_content != upd_channel.lastmessage.content:
        await upd_channel.send(body_content)"""

@bot.event
async def on_message(ctx):
    if ctx.content.lower() in greeting_triggers:
        if random.randint(1,5) == random.randint(1,5):
            await ctx.channel.send(greetings[random.randint(0,len(greetings)-1)])

    await bot.process_commands(ctx)
    
bot.run(os.getenv("DISCORD_TOKEN"))