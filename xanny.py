from discord import Game
from discord.ext import commands, tasks
from discord.ext.commands import Bot

token = open('token.txt', 'r').readline()
xanny = commands.Bot(command_prefix='x.')

@xanny.event
async def on_ready():
    print("Bot is online")

@xanny.command()
async def ping(ctx):
    await ctx.send("pong")

xanny.run(token.strip())