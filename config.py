from dotenv import load_dotenv
import os

# Connect the path with your '.env' file name
load_dotenv()

# bot token from BotFather
BOT_TOKEN = os.getenv("BOT_TOKEN")