import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
from translationstring import TranslationString #https://translate-python.readthedocs.io/en/latest/

import webserver

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log',
                              encoding='utf-8',
                              mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
  print(f"We logged in as {bot.user}")

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  await bot.process_commands(message)


@bot.command()
async def list(ctx, *, question):
    await ctx.send(f"Please specify a list")


webserver.keep_alive()
bot.run(token, log_handler=handler, log_level=logging.DEBUG)