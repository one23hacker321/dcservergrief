#Requirements:
- Python 3.8
- discord.py or a Fork of discord.py
- Bot Token

##Setup:
- Paste the Bot Token in the File `settings.json` at `token`
- Paste your User ID at in the File `settings.json` at `owner`
- Paste IDs of the Servers you dont want to be deleted at the Bot Start (only when Type is 1)

##Settings:
All the Settings you can set in the File `settings.json`

Types:

0: Deletes the current Server only when a Owner runs the !delete Command.
1: Deletes all Servers the Bot is at on start.
2: Deletes a Server where a Message is send.

Confirms:

0: Instantly deletes the Server, when the !delete Command is run
1: Waits for a Confirmation by the User, before deleting the Server

Leaves:

0: Dont leaves the Server after deleting it
1: Leaves the Server after deleting it
