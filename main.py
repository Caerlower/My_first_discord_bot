import discord
import os
import json 
import requests
import re
from bot_running import run_bot

TOKEN = os.getenv('TOKEN', '')
# print(dir(discord))
intents=discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def get_quote(api='https://zenquotes.io/api/random'):
  response = requests.get(api)
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  return quote


custom_messages_start = {
  'cap':'no cap',
  'no way': 'yes way',
  'unbelievable': 'ikr!'
}

keys = '|'.join(custom_messages_start.keys())

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  # print(message)
  if message.author == client.user:
    return
  # print(message.author)
  msg = message.content

  if msg == ('quote'):
    quote = get_quote()
    await message.channel.send(quote)

  # for key in keys:
  #   if message.content.lower().startswith(key):
  string = re.findall(rf'^({keys})', msg, re.I)
  if string:
    # print(string)
    key = string[0].lower()
    # await message.channel.send(custom_messages_start[key])
    await message.reply(custom_messages_start[key])

run_bot()
client.run(TOKEN)