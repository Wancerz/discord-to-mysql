import discord
from discord.ext import commands, tasks
import os
import asyncio

intents = discord.Intents.all()
intents.message_content = True
TOKEN = ''
bot = commands.Bot(command_prefix='!', intents=intents)

# class Tasks:
#     pass


async def load():
    for filename in os.listdir('./COGS'):
        print(filename)
        if filename.endswith(".py"):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await load()
    await bot.start(TOKEN)

asyncio.run(main())


# for filename in os.listdir("COGS"):  # iterate over files in 'COGS' dictionary
#     print(filename)
#     if filename.endswith(".py"):
#         bot.load_extension(f"COGS.{filename[:-3]}")  # load cogs into bot
#         print("Cog Loaded!")


