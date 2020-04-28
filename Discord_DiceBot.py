""" This python file creates a Discord bot whose sole purpose is to roll dice of user specified sides."""


import discord
from random import randrange
import re

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "Hello bot":
        await message.channel.send("Hi! I am a bot and I can roll dice for you!")
        
    # Listens for any message starting with roll or Roll, extracts the digits and then picks a random
    # integer from 1 through that number
    if message.content.startswith('roll') or message.content.startswith('Roll'):
        num = re.findall(r"\d+",message.content)
        num = int(''.join(num))
        await message.channel.send(randrange(1,num+1))

#NOTE: Replace the word 'token' below with your own bot's token, also in quotes.
client.run(token)

