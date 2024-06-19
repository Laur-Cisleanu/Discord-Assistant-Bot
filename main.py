import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
import responses

# step 0
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# step 1
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

# step 2 message functionality

async def send_message(message: Message, user_message):
    if not user_message:
        print("Message was empty because intents were not enabled, probably")
        return
    if is_private := user_message[0] == "?":
        user_message = user_message[1:]

    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# step 3 start up

@client.event
async def on_ready():
    print(f"{client.user} is running!")


# step 4 incoming messages

@client.event
async def on_message(message: Message):
    if message.author == client.user:
        return
    
    username = str(message.author)
    user_message = message.content
    channel = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


# step 5 running the code
def main():
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()