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
intents.members = True
intents.message_content = True

client = commands.Bot(command_prefix = "#", intents=intents)
    
# step 2 commands

@client.event
async def on_ready():
    print(".........I am online!")


@client.command()
async def hello(ctx):
    await ctx.send("Hello, i am online")

@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You are not in a voice channel!")

@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I left the voice channel")
    else:
        await ctx.send("I am not currently in a voice channel")


# Last step - Starting the bot up
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()