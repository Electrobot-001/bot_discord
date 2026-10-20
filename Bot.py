import discord
import random
from discord.ext import commands


# la variabile intents contiene i permessi al bot
intents = discord.Intents.default()
# abilita il permesso a leggere i contenuti dei messaggi
intents.message_content = True
# crea un bot e passa gli indents
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {bot.user}')

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def name(ctx, name: str):
    await ctx.send(f'Ciao! Sono '+ name + "!")

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def subtract(ctx, left: int, right: int):
    """Subtracts two numbers."""
    await ctx.send(left - right)

@bot.command()
async def multiply(ctx, left: int, right: int):
    """Multiplies two numbers together."""
    await ctx.send(left * right)

@bot.command()
async def divide(ctx, left: int, right: int):
    """Divides two numbers."""
    await ctx.send(left / right)

@bot.command()
async def repeat(ctx, times: int, content: str):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def randomize(ctx, left: int, right: int):
    """Picks a random number"""
    await ctx.send(random.randint(left, right))



bot.run("token")
