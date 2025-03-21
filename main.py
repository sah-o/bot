import discord
from discord.ext import commands
import os
import threading
from flask import Flask, render_template

# Load configurations
with open('code.txt', 'r') as f:
    TOKEN = f.read().strip()

with open('id.txt', 'r') as f:
    ADMIN_ID = int(f.read().strip())

# Initialize bot with intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Load commands from category files
for filename in os.listdir("./categories"):
    if filename.endswith(".py"):
        bot.load_extension(f"categories.{filename[:-3]}")

# Flask app for web interface
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def run_bot():
    bot.run(TOKEN)

def run_flask():
    app.run(port=5000)

if __name__ == '__main__':
    # Run the bot in a separate thread
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()

    # Run the Flask app
    run_flask()
