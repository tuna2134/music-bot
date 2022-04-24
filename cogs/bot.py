from discord import app_commands


class Bot(app_commands.Group):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(name="bot", description="category of bot")
        
    @app_commands.command()
    async def ping(self, interaction):
        await interaction.response.send_message(round(self.bot.latency * 100))
        
async def setup(bot):
    bot.tree.add_command(Bot(bot))
