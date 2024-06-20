import os
from typing import Final
from dotenv import load_dotenv
import discord
from discord.ext import commands
import responses

# step 0 Loading the token
load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")

# step 1 bot set up
intents: discord.Intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix = "#", intents=intents)
    
# step 2 commands

@client.event
async def on_ready():
    print(".........I am online!")


@client.command()
async def hello(ctx):
    await ctx.send("Hello, i am online")


# step 5 running the code
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()