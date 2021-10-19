import discord

client = discord.Client(command_prefix="$")

@client.event
async def on_ready():
  print("Bot is Working!")


@client.event
async def on_message(message):
  if discord.message.author== client.user:
    return 

  context = message.content.strip().lower()
  if context.startswith('$hello'):
    await message.channel.send('Hello')

client.run("TOKEN")