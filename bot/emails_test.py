from imap_tools import MailBox, AND
from bs4 import BeautifulSoup as BS
from io import StringIO
from dotenv import load_dotenv
import os

# THIS CODE REQUIRES A RULE TO BE SET IN OUTLOOK:
# If message was sent to Students Intake 2020, COPY to Bot folder


# Login to school email
load_dotenv()
user = os.environ.get("USER")
password = os.environ.get("PASSWORD")
mb = MailBox("mail.greenhead.ac.uk").login(user, password)


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
        atts.append(StringIO(att.part.get_payload()))
    # Delete the message from Bot folder
    mb.delete(msg.uid)

mb.logout()
