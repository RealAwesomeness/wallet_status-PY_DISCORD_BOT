import discord
from discord.ext import commands
import time
import asyncio
import subprocess
print("Booting up...")
TOKEN="NDc4MjAyNDI5MjM4OTM1NTUy.DlJHlw.Fk2xb7Y8UOg1AdEbL-ftM_yJT2Y"
client = discord.Client()
channel='478200309567586316'
@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	user = discord.Server.get_member_named("RealAwesomeness#6146")
	height=[]
	coins=[]
	oldheight=[]
	oldheightcreated=False
	while True:
		height=[]
		coins=[]
		count=0
		print("Checking wallet status...")
		counter=0
		subprocess.call('bash copier.sh', shell=True)
		options=open("config.txt","r")
		time.sleep(0.5)
		for line in options:
			coins.append(line.rstrip())
			line=line.rstrip()
			f=open(line+".log")
			rawdata=f.read()
			donde=rawdata.rfind("height=")
			dondedos=rawdata.rfind("version=")
			rawdata=rawdata[donde:dondedos]
			height.append(rawdata)
		if oldheightcreated:
			for item in coins:
				if height[count]==oldheight[count]:
					await client.send_message(user,"The "+item+" wallet chain is stalled and/or the wallet is down",tts=False)
					#await client.send_message(discord.Object(id="331451617511735297"),"The "+item+" wallet chain is stalled and/or the wallet is down",tts=False)
					print("Wallet was detected as being down!")
				count+=1
		print("Finished checking wallets")
		oldheight=height
		oldheightcreated=True
		time.sleep(1)
client.run(TOKEN)
