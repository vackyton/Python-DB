import discord
from discord.ext import commands

client = commands.Bot(command_prefix=",")


# when bot is online
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game('Bot is online :)'))


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def clear(ctx ,amount = 50):
    await ctx.purge(amount)

client.run("Token")
