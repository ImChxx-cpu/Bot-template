import discord
from datetime import datetime
from config.settings import BotConfig

class EmbedService:
    @staticmethod
    def create_success_embed(title: str, description: str = None) -> discord.Embed:
        embed = discord.Embed(
            title=title,
            description=description,
            color=BotConfig.SUCCESS_COLOR,
            timestamp=datetime.utcnow()
        )
        return embed
    
    @staticmethod
    def create_error_embed(title: str, description: str = None) -> discord.Embed:
        embed = discord.Embed(
            title="❌ " + title,
            description=description,
            color=BotConfig.ERROR_COLOR,
            timestamp=datetime.utcnow()
        )
        return embed
    
    @staticmethod
    def create_info_embed(title: str, description: str = None) -> discord.Embed:
        embed = discord.Embed(
            title=title,
            description=description,
            color=BotConfig.PRIMARY_COLOR,
            timestamp=datetime.utcnow()
        )
        return embed
    
    @staticmethod
    def create_user_profile_embed(user: discord.Member) -> discord.Embed:
        embed = discord.Embed(
            title=f"Perfil de {user.display_name}",
            color=BotConfig.PRIMARY_COLOR,
            timestamp=datetime.utcnow()
        )
        embed.set_thumbnail(url=user.avatar.url if user.avatar else None)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Se unió", value=user.joined_at.strftime("%d/%m/%Y"), inline=True)
        embed.add_field(name="Cuenta creada", value=user.created_at.strftime("%d/%m/%Y"), inline=True)
        embed.set_footer(text=f"Solicitado por {user.name}")
        return embed