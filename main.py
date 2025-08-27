import discord
from discord.ext import commands
import asyncio
import logging
from config.settings import BotConfig
from commands.general import GeneralCommands
from commands.moderation import ModerationCommands

class DiscordBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        
        super().__init__(
            command_prefix=BotConfig.PREFIX,
            intents=intents,
            help_command=None
        )
        
    async def setup_hook(self):
        """Configura los comandos slash al inicializar"""
        await self.add_cog(GeneralCommands(self))
        await self.add_cog(ModerationCommands(self))
        await self.tree.sync()
        print(f"Comandos slash sincronizados para {self.user}")
        
    async def on_ready(self):
        print(f'{self.user} está listo!')
        await self.change_presence(
            activity=discord.Game(name="Desarrollado por Jesús Jara S.")
        )

async def main():
    bot = DiscordBot()
    
    try:
        await bot.start(BotConfig.TOKEN)
    except Exception as error:
        logging.error(f"Error al iniciar el bot: {error}")
    finally:
        await bot.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())