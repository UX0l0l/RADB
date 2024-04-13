import discord
from discord.ext import commands, tasks
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
intents = discord.Intents.all()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents) # Could be any prefix

SCID = int(os.getenv('SCID'))
TCID = int(os.getenv('TCID'))

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await copy_previous_messages()

async def copy_previous_messages():
    source_channel = bot.get_channel(SCID)
    target_channel = bot.get_channel(TCID)
    if source_channel and target_channel:
        async for message in source_channel.history(limit=None, oldest_first=True):  # Fetch all messages from the source channel
            if message.content:  # Check if the message has text content
                await target_channel.send(message.content)
            elif message.attachments:  # Check if the message has attachments
                for attachment in message.attachments:
                    await target_channel.send(attachment.url)
    else:
        print("One or more channels were not found.")

@bot.event
async def on_message(message):
    if message.channel.id == SCID:
        target_channel = bot.get_channel(TCID)
        if target_channel and message.content != "":
            await target_channel.send(message.content)
        else:
            print("Target channel not found.")
    await bot.process_commands(message)

bot.run(TOKEN)

