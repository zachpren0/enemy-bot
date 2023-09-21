# enemy-bot: A Discord Bot for Roasting Friends

## Setting Up Environment Variables and Getting Discord Access Token

### Prerequisites

Before you begin, make sure you have the following installed on your system:

- [Python](https://www.python.org/downloads/): The programming language used for creating the bot.
- [pip](https://pip.pypa.io/en/stable/installation/): The Python package manager for installing required packages.

### Install Required Packages

You will need to install the following Python packages for your bot:

- [python-dotenv](https://pypi.org/project/python-dotenv/): This package is used to securely manage environment variables.
- [discord.py](https://pypi.org/project/discord.py/): A Python library that provides a wrapper for the Discord API.

You can easily install these packages using `pip`. Open your terminal or command prompt and run the following command:

```bash
pip install python-dotenv discord.py
```

### Getting a Discord Access Token

To get a Discord access token for your bot, follow these steps:

1. **Create a Discord Application:**
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Click the "New Application" button and give your application a name (e.g., "enemy-bot").

2. **Create a Bot User:**
   - Inside your application, navigate to the "Bot" section on the left sidebar.
   - Click the "Add Bot" button to create a bot user.

3. **Enable OAuth2 Intents:**
   - In the "OAuth2" section, under "OAuth2 URL Generator," make sure to enable the necessary intents. For a bot that interacts with messages, turn on "Intents" for "Message Content" or the specific intents your bot requires.

4. **Bot Permissions:**
   - In the "Bot Permissions" section, give your bot the permissions it needs. For a roasting bot, you might want to grant permissions like "Read Messages" and "Send Messages."

5. **Copy Your Bot Token:**
   - In the "Token" section of your bot settings, click the "Copy" button to copy your bot's token to the clipboard.

   **Important:** Treat your bot token like a secret password and never share it publicly.

### Store Your Access Token Securely

To securely store your Discord access token, create a `.env` file in the root directory of your project (if it doesn't already exist) and open it in a text editor.

Example `.env` file:

```env
DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
```

Replace `YOUR_DISCORD_BOT_TOKEN` with the bot token you copied earlier.

Save the `.env` file. This file will securely store your Discord access token and should never be shared or committed to version control systems like GitHub.

### Loading Environment Variables in Python

To access your Discord token in your Python code, use the `python-dotenv` library. Create a Python script (e.g., `bot.py`) and add the following code at the top to load the variables from the `.env` file:

```python
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

# Access your variables like this:
discord_token = os.getenv("DISCORD_TOKEN")
```

Now, you can use the `discord_token` variable in your code to authenticate with the Discord API securely.

That's it! You've successfully set up environment variables and obtained an access token from Discord for your "enemy-bot" project. Remember to keep your access token in the `.env` file to prevent accidental exposure on GitHub.



