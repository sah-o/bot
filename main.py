@bot.event
async def on_message(message):
    if message.content.startswith('!saho'):
        await show_main_menu(message)
    elif message.content.startswith('!'):
        await handle_category_command(message)
    await bot.process_commands(message)

async def show_main_menu(message):
    embed = discord.Embed(title="Main Menu", color=0x00ff00)
    embed.set_image(url="https://mega.nz/file/mBQjgYjC#cl4RZSpbsvuD5w5TcXsRQjkKYvd088nOcLeBxUS3xjo")
    embed.add_field(name="Commands", value="Select an option below:", inline=False)

    view = View()

    # Button for Generate Barcodes
    generate_button = Button(label="Generate Barcodes", style=discord.ButtonStyle.primary)
    generate_button.callback = lambda interaction: show_barcode_categories(interaction)
    view.add_item(generate_button)

    # Button for Promo Codes
    promo_button = Button(label="Promo Codes", style=discord.ButtonStyle.secondary)
    promo_button.callback = lambda interaction: show_promo_codes(interaction)
    view.add_item(promo_button)

    # Button for New Category
    new_button = Button(label="New Category", style=discord.ButtonStyle.success)
    new_button.callback = lambda interaction: handle_new_category(interaction)
    view.add_item(new_button)

    # Button for Update Category
    update_button = Button(label="Update Category", style=discord.ButtonStyle.danger)
    update_button.callback = lambda interaction: handle_update_category(interaction)
    view.add_item(update_button)

    # Button for Add Guide
    guide_button = Button(label="Add Guide", style=discord.ButtonStyle.primary)
    guide_button.callback = lambda interaction: handle_add_guide(interaction)
    view.add_item(guide_button)

    msg = await message.channel.send(embed=embed, view=view)
    await delete_after_delay(msg, 120)  # Delete bot's message after 2 minutes
