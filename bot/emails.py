from discord.ext import commands


class Emails(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def read_messages(self):
        # This function will read messages from the inbox and return any relevant, unprocessed messages

        # The below code is the original code from run.py
        # This code will need to be adapted or completely re-written, it is simply here for reference
        # The win32com library cannot be used, as it reads the local windows user's outlook details
        # The hosted environment will not have this user set, therefore an alternative method needs to be found
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

        pass
