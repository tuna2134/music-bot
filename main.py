from discord.ext import commands
from os import listdir
from ujson import load


class MusicBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="m!", intents=discord.Intents.all())
        with open("secret.json", "r") as f:
            self.secret = load(f)

    async def setup_hook(self):
        for name in listdir("cogs"):
            try:
                await self.load_extension(f'cogs.{name.replace(".py", "")}')
            except:
                pass
            else:
                print(f"loaded: {name}")
        await self.tree.sync()
        
bot = MusicBot()

bot.run("Token")
