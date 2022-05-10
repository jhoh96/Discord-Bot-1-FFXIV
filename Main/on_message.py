import discord
import os
import asyncio

from dotenv import load_dotenv




client = discord.Client() # connection to discord / interaction with API

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

@client.event 
async def on_ready(): # triggered when bot comes online
    print('Bot is now online, listening for commands')


# basic event handling for practice
@client.event
async def on_message(message): # param - message
    if message.author == client.user: # prevent infinite loop
        return


    if message.content == 'hello':
        await message.channel.send('Hi there')



client.run(DISCORD_TOKEN) # do not hard code discord bot token
