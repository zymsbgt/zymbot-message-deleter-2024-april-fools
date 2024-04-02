import discord
from discord.ext import commands

# Define your intents
intents = discord.Intents.default()
intents.messages = True  # Enable message related events
intents.message_content = True

# Bot setup
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def send_message(ctx, server_id: int, channel_id: int, *, message: str):
    server = bot.get_guild(server_id)
    if server:
        channel = server.get_channel(channel_id)
        if channel:
            await channel.send(message)
            await ctx.send("Message sent successfully!")
        else:
            await ctx.send("Channel not found in the server.")
    else:
        await ctx.send("Server not found.")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    if "all hail zymbot" in message.content.lower():
        pass
    elif "!send_message " in message.content.lower():
        pass
    elif message.guild.id == 443253214859755522:
        try:
            await message.delete()
        except discord.Forbidden:
            print("Bot doesn't have permission to delete messages.")
        except discord.HTTPException:
            print("An error occurred while trying to delete the message.")
    else:
        pass

bot.run('YOUR_TOKEN_HERE')