import discord
from discord.ext import commands

#Initialize
default_intents = discord.Intents.default()
default_intents.members = True  # You must activate intents in bot paremeters(on discord)
bot = commands.Bot(command_prefix="!", intents=default_intents)
TOKEN = " " ##### Insert token here

#Basics commands
@bot.event
async def on_ready():
    print("Bot is ready!")

@bot.event
async def on_member_join(member):
    print(f"User {member.display_name} joined server!") 
    

#Commands of Bot
@bot.event
async def on_message(message):
    if message.content.startswith("!help"):
        await message.channel.send("All commands: ...")

    # elif message.content.startswith("!other command")
        # await message.channel.send("write something here")

    # elif ...    


bot.run(TOKEN)   # activate bot 