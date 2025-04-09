import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'Smoke Detector logged in as {bot.user.name} - {bot.user.id}')

def get_view():
    if random.randint(1, 100) != 1:
        return None

    view = discord.ui.View()
    for button in [discord.ui.Button(label='About Me', style=discord.ButtonStyle.green, url='https://eepy.io/'),
                   discord.ui.Button(label='View Source', style=discord.ButtonStyle.green, url='https://github.com/eepyfemboi/SmokeDetectorBot'),
                   discord.ui.Button(label='Add Me', style=discord.ButtonStyle.green, url='https://discord.com/oauth2/authorize?client_id=1355661405121941544')]:
        view.add_item(button)

    return view


@bot.event
async def on_message(message: discord.Message):
    if message.author.bot or message.author.system:
        return

    chance = random.randint(1, 100)
    if chance == 1:
        await message.author.send("Beep", view=get_view())
    elif chance == 2:
        await message.channel.send("Beep", view=get_view())

bot.run("")
