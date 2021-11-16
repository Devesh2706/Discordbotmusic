import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)


client.run("OTEwMDIwNTAxNzE4NTczMTU3.YZMwog.ettGFhdIqK85DEmVHjBLLEwCv4M")
