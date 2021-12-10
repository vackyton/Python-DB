import discord
from discord.ext import commands

client = discord.Client(command_prefix="$")


# when bot is online
async def on_ready():
    print('Logged in as ' + str(client.user))


@client.event
async def on_player_join(member):
    print(f'{member} has joined a server')


@client.event
async def on_player_remove(member):
    print(f'{member} has left/kicked from a server')

@client.event
async def on_message(message):
    if message.content.startswith('$ping'):
        await message.channel.send(f'Pong! {round(client.latency * 1000)}ms')
    if message.content.startswith('$hi'):
        await message.channel.send('Hello')
    if message.content.startswith('$settings prefix'):
        await message.channel.send('prefix changing mode')
    if message.content.startswith('$clear'):
        amount = 50
        await message.channel.purge(limit = amount + 1)

client.run("Token")
