import discord
import ollama
import os
import discord.ext
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Define intents
intents = discord.Intents.default()
intents.members = True  # Enable the members intent

# Initialize bot with intents
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author != bot.user:
        if bot.user.mentioned_in(message):
            # Extract the message content after the mention
            message_content = message.content.replace(f'<@!{bot.user.id}>', '').strip()
            # Checks if there's any content after the mention
            if message_content:
                # Response
                user_input = generate_response(message_content)
                #Queries llama for the user's input
                response = query_llama(user_input)
                #Adds the highlight to the response mentioning the user that asked the question
                formatted_response = f"{message.author.mention}, {response}"
                await message.channel.send(formatted_response)

#This function removes the mention prefix from the user input
def generate_response(input):
    input = input.split(maxsplit=1)[-1].strip()
    return input

def query_llama(prompt):
    try:
        with open('AIcontext.txt', 'r') as file:
            context = file.read()
        messages = [
            {"role": "system", "content": context},
            {"role": "user", "content": prompt},
        ]
        response = ollama.chat(
            model='llama2:13b-chat',
            messages=messages
        )
        message_content = response['message']['content']
        print("Answer: " + message_content)
        return message_content
    except Exception as e:
        print("Answer" + e)
        return e
    
bot.run(TOKEN)
