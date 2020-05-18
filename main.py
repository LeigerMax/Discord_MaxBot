
import discord
import random
import os
import youtube_dl
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from discord.utils import get
import asyncio
from discord import opus


#Créer le bot
jeton = ""
bot = commands.Bot(command_prefix='!!')

players = {}

#Event
@bot.event
async def on_ready():
    print("bot pret")
    await bot.change_presence(status=discord.Status.idle, activity = discord.Game("MaxBot est en dev"))

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound) :
        await ctx.send('Commande inconnu ! Faite !!help pour les voir les commandes  ')


#Command

@bot.command(brief="Le bot rejoint le vocal")
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
@bot.command(brief="Le bot quitte le vocal")
async def leave(ctx):
    await ctx.voice_client.disconnect()


@bot.command()
async def invite(ctx):
    link = await ctx.channel.create_invite (max_age=1)
    await ctx.send(link)



@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs') :
    if filename.endswith('.py') :
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.command(brief="Donne les informations sur le bot")
@commands.has_permissions(manage_messages=True)
async def infoBot(message):
    embed = discord.Embed(title="BotMax", description="Information", color=0x00ff00)
    embed.add_field(name="Version", value="0.0", inline=False)
    embed.add_field(name="Create by", value="Maxou 💗💗💗#9733", inline=False)
    embed.set_image(url="https://media.discordapp.net/attachments/484714777675956230/712033636828053554/Logo_v3_500px.png")
    await message.channel.send(embed=embed)


@bot.command(brief="Donne un nombre au hasard entre 0 et 100")
async  def roll(ctx):
    n = random.randrange(1,100)
    await ctx.send(n)



@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=2):
    if amount < 20:
        await ctx.channel.purge(limit=amount)


#Lance le bot
print("lancement du bot ...")
bot.run(jeton)





@bot.command(aliases=['8ball'])
async def _8ball(ctx,*,question):
    responses = ['Max est le meilleur', 'Max is best']
    await ctx.send(f'Question : {question}\nRéponse : {random.choice(responses)}')

