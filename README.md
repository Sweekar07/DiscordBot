# Discord Bot

This script initializes a multifunctional Discord bot that encompasses various features from providing inspirational quotes to playing a simple coin-toss game, and includes interactions with a MongoDB database.

## Features

### 1. MongoDB Integration
The bot connects with a MongoDB database to store and manage data related to the Discord server's users and their respective interaction scores. It updates these scores based on specific keyword interactions.

### 2. Random Inspirational Quotes
At a user's request, the bot can provide inspirational quotes. This feature is implemented using an external API that the bot calls to retrieve a quote, subsequently posting it within the channel.

### 3. Coin Toss Game
Users can engage with a simple coin-toss game. Upon command, the bot randomly returns a "heads" or "tails" response, simulating a coin toss.

### 4. Version Information
Users can query the bot for version information, which is returned as a rich embedded message detailing the current bot version and the release date.

## Event Handlers

* The bot actively listens for messages, disregarding any sent by itself, thereby preventing potential feedback loops.
* Specific keywords within user messages trigger database interactions. Depending on whether the user is new or returning, the bot either creates a new database entry or updates the existing score.
* Commands for games or quote retrieval are recognized and elicit respective responses from the bot.

## External File Usage

For security, the bot's authentication token is stored in and read from an external file. This method ensures the token isn't directly embedded within the script.

## Database Interaction

Interactions with the MongoDB database, including data persistence operations across multiple sessions, are handled using the `pymongo` library.

## Dependencies

* `discord.py` - Enables the creation and management of the bot within the Discord environment.
* `pymongo` - Facilitates interactions with MongoDB.
* `requests` - Used for HTTP requests, primarily when fetching quotes from the external API.

## Setup and Running

This bot requires a valid Discord bot token and MongoDB database access. Upon configuring the bot within a server and installing all dependencies, you can run the script. The bot then becomes active and ready to interact with users on your Discord server.

