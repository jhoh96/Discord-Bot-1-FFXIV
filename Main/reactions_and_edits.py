import discord
import os
from dotenv import load_dotenv

client = discord.Client() # connection to discord / interaction with API

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


# triggered when bot comes online
@client.event 
async def on_ready(): 
    print('Bot is now online, listening for commands')


# basic event handling for practice
@client.event
async def on_message(message):
    # prevent infinite loop
    if message.author == client.user: 
        return

    # add reaction
    if message.content == 'reaction text':
        await message.add_reaction('\U0001F60E')

# tracks text edits
@client.event 
async def on_message_edit(before, after) :
    await before.channel.send(
        f'{before.author} edit a message. \n'
        f'Before: {before.content}\n'
        f'After {after.content}'
    )

# tracks user reaction to text
@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')


    


client.run(DISCORD_TOKEN) # do not hard code discord bot token
