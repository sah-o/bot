from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="add_category")
    async def add_category(self, ctx, name: str, cooldown: int):
        # Logic to add a new category
        await ctx.send(f"✅ Category '{name}' added with a cooldown of {cooldown} hours.")

async def setup(bot):
    await bot.add_cog(Admin(bot))
