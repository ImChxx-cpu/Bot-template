import os
from dotenv import load_dotenv

load_dotenv()

class BotConfig:
    TOKEN = os.getenv('DISCORD_TOKEN')
    PREFIX = os.getenv('BOT_PREFIX', '!')
    GUILD_ID = int(os.getenv('GUILD_ID', 0)) if os.getenv('GUILD_ID') else None
    
    # Colores para embeds
    PRIMARY_COLOR = 0x3498db
    SUCCESS_COLOR = 0x2ecc71
    ERROR_COLOR = 0xe74c3c
    WARNING_COLOR = 0xf39c12