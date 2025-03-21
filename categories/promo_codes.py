from discord.ext import commands
import time

class PromoCodes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cooldowns = {}
        self.COOLDOWN_TIMES = {}

    @commands.command(name="promo")
    async def promo(self, ctx, category: str):
        user_id = ctx.author.id
        current_time = time.time()

        if user_id in self.cooldowns.get(category, {}) and current_time - self.cooldowns[category][user_id] < self.COOLDOWN_TIMES.get(category, 0):
            remaining_time = int(self.COOLDOWN_TIMES[category] - (current_time - self.cooldowns[category][user_id]))
            await ctx.send(f"⏳ You must wait **{remaining_time}s** before using **{category}** again.", delete_after=10)
            return

        # Logic to fetch and send promo codes
        await ctx.send(f"🎁 Promo code for {category} sent to your DMs!", delete_after=60)

async def setup(bot):
    await bot.add_cog(PromoCodes(bot))
