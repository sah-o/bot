from discord.ext import commands
from utils.barcode_generator import generate_store_barcode, generate_barcode_image
import discord

class Barcodes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="barcode")
    async def barcode(self, ctx, store: str, barcode_num: str, price: str = None):
        if store.lower() == "morrisons" and price is not None:
            await ctx.send("❌ Morrisons barcodes do not require a price.", delete_after=10)
            return
        full_code = generate_store_barcode(store, barcode_num, price)
        barcode_image = generate_barcode_image(full_code)
        await ctx.send(file=discord.File(barcode_image, 'barcode.png'))

async def setup(bot):
    await bot.add_cog(Barcodes(bot))
