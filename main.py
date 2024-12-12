import os
from typing import Final
from dotenv import load_dotenv
import discord
from discord import app_commands
from discord.ext import commands
import responses

# step 0 Loading the token
load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")

class MyBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        print(f"Logged in as {self.user}")
        # Sync commands with Discord

        guild_id = 551029699900473347  # Replace with your guild ID
        guild = discord.utils.get(self.guilds, id=guild_id)
        if guild:
            # Sync commands for a specific guild immediately
            await self.tree.sync(guild=guild)
            print("Slash commands synced for the guild!")
        else:
            print("Guild not found!")

# Instantiate the bot
client = MyBot()

# Define the slash command
@client.tree.command(name="hello", description="Say hello!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello!")

@client.tree.command(name="voice_info", description="Get the number of members in a voice channel")
@app_commands.describe(channel="Select a voice channel to query")
async def voice_info(interaction: discord.Interaction, channel: discord.VoiceChannel):
    # Get members in the voice channel
    members_in_channel = channel.members

    # Count members
    num_members = len(members_in_channel)

    # Create a list of member names
    member_names = []
    for member in members_in_channel:
        # Get the nickname if it exists, otherwise fall back to the username
        nickname = member.nick if member.nick else member.name
        member_names.append(nickname)

    # Prepare the response message
    response = f"There are a total of {num_members} members in {channel.name}:\n"
    if num_members > 0:
        response += "\n" + "\n".join(member_names)  # List member names
    else:
        response += "No members in this channel."

    # Send the response
    await interaction.response.send_message(response)



#@client.command()
#async def hello(ctx):
#    await ctx.send("Hello, i am online")
#
#@client.command(pass_context = True)
#async def join(ctx):
#    if (ctx.author.voice):
#        channel = ctx.message.author.voice.channel
#        await channel.connect()
#    else:
#        await ctx.send("You are not in a voice channel!")
#
#@client.command(pass_context = True)
#async def leave(ctx):
#    if (ctx.voice_client):
#        await ctx.guild.voice_client.disconnect()
#        await ctx.send("I left the voice channel")
#    else:
#        await ctx.send("I am not currently in a voice channel")


# Last step - Starting the bot up
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()