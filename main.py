import os
token = os.environ['token']
from keep_alive import keep_alive


import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

alyx = 632326478394032128
niko = 631364065519992852
ray = 843562664156463134

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def nick(ctx, name, *nick):
    name = name.lower()
    user = 0
    if name == "alyx": user = alyx
    elif name in ["niko", "lilia", "ace", "riddle"]: user = niko
    elif name == "ray": user = ray
    
    with open("log.txt","a") as log:
        log.write(f"""{name}'s nick was changed by {ctx.author.name} from '{bot.get_guild(929424975625080883).get_member(user).display_name}' to '{' '.join(nick)}'""")

    await bot.get_guild(929424975625080883).get_member(user).edit(nick=' '.join(nick), reason=ctx.author.name)

keep_alive()
bot.run(token)
