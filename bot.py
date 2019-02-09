import asyncio
import discord
import random

from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Bot is ready to use!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("/gather"):
        await client.send_message(message.channel, random.choice([ "Oh wow, what a cute snail! It's not worth anything, but I'm sure... someone wants it...?",
                                                                     "",
                                                                     "Without a doubt",
                                                                     "Yes, definitely",
                                                                     "You may rely on it",
                                                                     "As I see it, yes",
                                                                     "Most likely",
                                                                     "Outlook good",
                                                                     "Yes",
                                                                     "Signs point to yes",
                                                                     "Reply hazy try again",
                                                                     "Ask again later",
                                                                     "Better not tell you now",
                                                                     "Cannot predict now",
                                                                     "Don't count on it",
                                                                     "My reply is no",
                                                                     "My sources say no",
                                                                     "Outlook not so good",
                                                                     "Very doubtful"]))

client.run("NTQzNTYyNzU0MjIxNDA4MjU3.Dz-35A.lUkwQbrbyg0nhm6j75aGMWjIGhA")
client.login(process.env.BOT_TOKEN);
