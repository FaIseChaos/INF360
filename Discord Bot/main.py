""" 
Main Objectives:
 - utilize Discord API to create a bot for the cybersecurity club server
 - make weekly & general announcements for club meetings and events
 - use discord to stream/record meetings & set up events
 - general form creation, submission, data storage (?), and retrieval
    - for signups, surveys, etc.
 - simple polls
 - attendance tracking for LLC members & Oktoberfest volunteers
  - resource repository
    - allow members to access club resources (such as documents, links, or guides)
 - info on club officers, members, and alumni
    - linkedin profiles
 - easter eggs
 - daily/weekly puzzels?

Future Objectives:
 - CTF (seperate bot?)
 - Website integration
 - Calender
 - Make this bot a template and sell it to other clubs?
"""

from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responces import get_response

# load bot token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# bot setup
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

# message functionality
async def send_message(message: Message, user_message: str) -> None:
   if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return
   
   if is_private := user_message[0] == '?':
         user_message = user_message[1:]      
   
   try:
      responce: str = get_response(user_message)
      await message.author.send(responce) if is_private else await message.channel.send(responce)
   except Exception as e:
         print(e)

# handle startup for bot
@client.event
async def on_ready() -> None:
      print(f'{client.user} has connected to Discord!')

# handle incoming messages
@client.event
async def on_message(message: Message) -> None:
   if message.author == client.user:
      return

   username: str = str(message.author)
   user_message: str = message.content
   channel: str = str(message.channel)
   
   print(f'{channel} said: {username}: "{user_message}"')
   await send_message(message, user_message)

# main entry point
def  main() -> None:
   client.run(token=TOKEN)

if __name__ == '__main__':
   main()