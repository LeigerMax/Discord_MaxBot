import discord
from discord.ext import commands

class KickAndBan(commands.Cog) :


    def __init__(self, bot):
        self.bot = bot
        self.warnings = warnings = {}

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')

    #Commands
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)


    @commands.command()
    # @commands.has_role("Admin")
    @commands.has_permissions(administrator=True)
    async def warning(self,ctx, membre: discord.Member):
        pseudo = membre.mention
        id = membre.id

        if id not in self.warnings:
            self.warnings[id] = 0
            await ctx.send(f"Le membre  {pseudo} n'a aucun avertissement ! ")

        self.warnings[id] += 1
        print("Ajout l'avertissment", self.warnings[id], "/3")
        if self.warnings[id] == 3:
            await membre.send("Vous avez été éjecté du serveur ! Trop d'avertissements !")
            await membre.kick()


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self,ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Ban {member.mention}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self,ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unban {user.name}')
                return

    #Error
    @warning.error
    async def on_command_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Tu dois faire !!warning @pseudo")

def setup(bot):
    bot.add_cog(KickAndBan(bot))