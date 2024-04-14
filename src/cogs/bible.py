import discord
from discord.ext import commands
from api.bible_api import call_bible_api


class Bible(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="verse", description="Look up any verse. (KJV)")
    async def verse(self, ctx, book: discord.Option(str), chapter: discord.Option(int), verse: discord.Option(int)):
        endpoint = f"bibles/de4e12af7f28f599-02/verses/{
            book}.{chapter}.{verse}?content-type=text&include-notes=false&include-titles=false&include-chapter-numbers=false&include-verse-numbers=false&include-verse-spans=false&use-org-id=false"

        verse_data = call_bible_api(endpoint)

        if verse_data:
            await ctx.respond(f"{verse_data['data']['content']} ({verse_data['data']['reference']})")
        else:
            await ctx.respond("Verse not found.")


def setup(bot):
    bot.add_cog(Bible(bot))
