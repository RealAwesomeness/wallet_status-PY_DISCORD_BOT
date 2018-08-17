import discord
from discord.ext import commands
import time
import asyncio
import subprocess
from discord.ext.commands import Bot
from discord.ext import commands
from io import StringIO
import hashlib
import random
import os

print("Booting up...")
client = discord.Client()
channel='478200309567586316'
TOKEN="{REDACTED}"

@client.async_event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	#user = Server.get_member_named()
	height, coins, oldheight =[], [], []
	oldheightcreated=False
	user = await client.get_user_info("331451617511735297")
	await client.send_message(user, "watch me use IDs :100:")
        
client.run(TOKEN)

"""
bot = commands.Bot(command_prefix="/asdf ", description="yeet")
@bot.event
async def on_ready():
        print('Bot', bot.user.name, 'with id', bot.user.id, 'is now online')
        print('------')

@bot.command(pass_context=True)
async def getid(ctx):
        print(ctx.message.author.id)

"""

bot.run(TOKEN)
