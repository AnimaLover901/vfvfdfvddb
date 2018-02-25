python -m pip install -U https://github.com/Rapptz/discord.py/archive/master.zip#egg=discord.py[voice] pillow psutil requests  
import discord
from discord.ext.commands import bot 
from discord.ext import commands
import asyncio
import time 

Client = discord.Client()
client=command.bot(command_prefix = "!")

@client.event 
async def on_ready() :
print("Bot is ready")

@client.event
async def on_message(message) :
if message.content == "cookie":
await client.send_message(message.channel, ":cookie:")


client.run("NDE3MTE3Mzk0NTc4NzAyMzM3.DXSRYw.z3UOUQcV-v3KKX3oUTrMnfKlmVI")
