import discord
import random
from discord.ext import commands

class CommandeUser(commands.Cog) :

    def __init__(self, bot):
        self.bot = bot

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')

    #Commands
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)} ms')

    @commands.command(brief=" Nombre aléatoire entre 0 et 100")
    async  def roll(self, ctx):
        n = random.randrange(0,101)
        await ctx.send(n)

    @commands.command()
    async def invite(self, ctx):
        link = await ctx.channel.create_invite(max_age=1)
        await ctx.send(link)

    @commands.command()
    async def botInfo(self, nmessage):
        self.message = nmessage
        embed = discord.Embed(title="MaxBot", description="Information sur le MaxBot", color=0x00ff00,)
        embed.add_field(name="Version", value="0.0", inline=False)
        embed.add_field(name="Create by", value="Maxou 💗💗💗#9733", inline=False)
        embed.set_image(url="https://media.discordapp.net/attachments/484714777675956230/712053801128951808/Logo_v3_500px.png")

        await self.message.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(CommandeUser(bot))