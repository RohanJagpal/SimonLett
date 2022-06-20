import discord
from discord.ext import commands, tasks
from imap_tools import MailBox, AND
from bs4 import BeautifulSoup as BS
from io import BytesIO
from dotenv import load_dotenv
import os

load_dotenv()


# THIS CODE REQUIRES A RULE TO BE SET IN OUTLOOK:
# If message was sent to Students Intake 2020, COPY to Bot folder


class Emails(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user = os.environ.get("USER")
        self.password = os.environ.get("PASSWORD")

    async def _read_mail(self):
        mb = MailBox("outlook.office365.com").login(self.user, self.password)

        # Move to the Bot folder, creates it if not present
        if not mb.folder.exists("INBOX/Bot"):
            mb.folder.create("INBOX/Bot")

        mb.folder.set("INBOX/Bot")

        # Fetch emails in the folder
        msgs = mb.fetch()

        for msg in msgs:
            # Emails are recieved in html, so translate it into plaintext
            temp_text = BS(msg.html, "html.parser").get_text()
            # Remove unnecessary blank lines
            text = ""
            for line in temp_text.splitlines():
                if line != "":
                    text += line + "\n"

            # Deal with attachments
            atts = []
            for att in msg.attachments:
                # Convert each attatchment to a file
                atts.append(discord.File(BytesIO(att.payload), att.filename))
            # Delete the message from Bot folder
            mb.delete(msg.uid)
            yield (msg.subject, text, atts)

        mb.logout()

    @tasks.loop(minutes=5)
    async def send_main(self):
        channel = self.bot.get_channel(887933735004176414)  # college-updates
        async for sub, text, atts in self._read_mail():
            em = discord.Embed(title=sub, description=text)
            await channel.send(embed=em, files=atts)

    @commands.Cog.listener()
    async def on_ready(self):
        """Start the send_main task when the bot has connected"""
        if not self.send_main.is_running():
            self.send_main.start()


def setup(bot):
    bot.add_cog(Emails(bot))
