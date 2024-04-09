# Discord Chatbot with Llama AI Integration

This project is a Discord chatbot that integrates with the Ollama AI to provide intelligent responses to user queries.

## Requirements
- Ollama on your local machine installed.
- The model llama2:13b-chat installed with ollama.

## Features

- Responds to mentions in Discord messages
- Utilizes Ollama AI to generate responses based on user input

## Setup

1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Create a `.env` file in the project directory and add your Discord bot token as `DISCORD_TOKEN=your_token_here`.
3. Ensure you have a `AIcontext.txt` file containing Helldivers 2 context for the AI to reference (you can add more information regarding the game).
4. Run the bot by executing the Python script: `python discordbot_assistant.py`.

## Usage

Once the bot is running and connected to your Discord server, simply mention the bot followed by your query to receive a response.

## Dependencies

- discord.py: Python library for creating Discord bots
- Ollama: Python library for interacting with the Ollama AI
- python-dotenv: Python library for loading environment variables from a .env file
