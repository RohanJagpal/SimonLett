from discord.ext import commands


class Twitter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def read_tweets(self):
        # This function will use Twitter API to read GH tweets
        # Tweets will be posted to a Discord channel
        pass
