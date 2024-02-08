import os
import discord

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client(intents=discord.Intents.default())
 

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')
    channel = client.get_channel(1204789115204145234)
    await channel.send("Wack is online")

client.run(TOKEN)