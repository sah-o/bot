from discord.ext import commands

class Guides(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.GUIDES = {}

    @commands.command(name="add_guide")
    async def add_guide(self, ctx, category: str, guide: str):
        self.GUIDES[category] = guide
        await ctx.send(f"✅ Guide added for '{category}'.")

async def setup(bot):
    await bot.add_cog(Guides(bot))
