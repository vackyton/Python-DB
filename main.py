import discord
import discord.message
import discord.channel
import discord.utils
import discord.user
import discord.message.startswith
import discord.send

client = discord.Client()
@client.event
async def on_ready():
  print("Bot is Working!")


@client.event
async def on_message():
  if discord.message.author== client.user:
    return 

  if message.content.startswith('$hello'):
    await message.channel.send('Hello')
