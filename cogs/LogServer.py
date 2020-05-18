import discord
from discord.ext import commands

class LogServer(commands.Cog) :

    def __init__(self, bot):
        self.bot = bot

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')

    @commands.Cog.listener()
    async def on_member_join(self,member):
        print(f'{member} a rejoint le serveur.')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        print(f'{member} a quitter le serveur.')


    #Commands



def setup(bot):
    bot.add_cog(LogServer(bot))