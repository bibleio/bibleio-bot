import discord
from discord.ext import commands


class Bible(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="verse", description="Look up any verse.")
    async def verse(self, ctx, book: discord.Option(str)):
        await ctx.respond('test')


def setup(bot):
    bot.add_cog(Bible(bot))
