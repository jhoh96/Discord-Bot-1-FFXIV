import discord
import os, os.path
from dotenv import load_dotenv


load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


class discordClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """
        to be changed to bot message ID
        """
        self.target_message_id = 971753720931049504 

    async def on_ready(self):
        print('Bot is now online, listening for commands')

    async def on_raw_reaction_add(self, payload):
        """
        roles added based on comment reaction
        """
        if payload.message_id != self.target_message_id:
            return
        
        guild = client.get_guild(payload.guild_id)
        if payload.emoji.name == '🟥':
            role = discord.utils.get(guild.roles, name='DPS')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '🟩':
            role = discord.utils.get(guild.roles, name='Healer')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '🟦':
            role = discord.utils.get(guild.roles, name='Tank')
            await payload.member.add_roles(role)

        
    async def on_raw_reaction_remove(self, payload):
        """
        roles removed based on comment reaction
        """
        if payload.message_id != self.target_message_id:
            return
        
        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)

        if payload.emoji.name == '🟥':
            role = discord.utils.get(guild.roles, name='DPS')
            await member.remove_roles(role)
        elif payload.emoji.name == '🟩':
            role = discord.utils.get(guild.roles, name='Healer')
            await member.remove_roles(role)
        elif payload.emoji.name == '🟦':
            role = discord.utils.get(guild.roles, name='Tank')
            await member.remove_roles(role)




intents = discord.Intents.default()
intents.members = True

client = discordClient(intents=intents)
client.run(DISCORD_TOKEN)