import discord
import string
import os
from random import choice
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):

    if message.author.id == 763474179123052544:
        return
    
    if message.author.bot:
        return

    messageString = str(message.content)
    messageString = messageString.translate(str.maketrans('', '', string.punctuation)).lower()

    if ("chat" in messageString and "dead" in messageString) or ("chat" in messageString and "ded" in messageString):

        with open('insults.txt','r') as textFile:
            insults = textFile.readlines()

        await message.channel.send(f"{message.author.mention} {choice(insults)}", delete_after=75)
        return

    else:
        return




client.run('Token Here')




