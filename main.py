
import discord
import random
import os
import youtube_dl
from discord.ext import commands
from discord.utils import get

#Créer le bot
jeton = "NzExNzUzNTUxNTcxMDU4NzY4.XsLWuQ.wCEJKawsNuT0k5eUUgXOInjBicE"
bot = commands.Bot(command_prefix='!!')

players = {}

#Détecter quand le bot est pret
@bot.event
async def on_ready():
    print("bot pret")
    await bot.change_presence(status=discord.Status.idle, activity = discord.Game("MaxBot est en dev"))

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound) :
        await ctx.send('Commande inconnu ! Faite !!help pour les voir les commandes  ')


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


@bot.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.chanel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected() :
        await voice.move_to(channel)
    else :
        voice = await channel.connect()


@bot.command(pass_context=True)
async def leave(ctx):
    channel = ctx.message.author.voice.chanel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected() :
        await voice.disconnect()
        print("Bot leave")
        await ctx.send(f'botMax leave {channel}')
    else :
        await ctx.send('Pas dans un chanel')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=2):
    if amount < 21 :
        await ctx.channel.purge(limit=amount)


#Lance le bot
print("lancement du bot ...")
bot.run(jeton)



@bot.command(aliases=['8ball'])
async def _8ball(ctx,*,question):
    responses = ['Max est le meilleur', 'Max is best']
    await ctx.send(f'Question : {question}\nRéponse : {random.choice(responses)}')


