import discord
from discord.ext import commands
from discord import app_commands
from services.embed_service import EmbedService
from services.user_service import UserService

class GeneralCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_service = EmbedService()
        self.user_service = UserService()
    
    @app_commands.command(name="ping", description="Muestra la latencia del bot")
    async def ping_command(self, interaction: discord.Interaction):
        try:
            latency = round(self.bot.latency * 1000)
            embed = self.embed_service.create_success_embed(
                "🏓 Pong!",
                f"Latencia: {latency}ms"
            )
            await interaction.response.send_message(embed=embed)
        except Exception as error:
            await self.handle_command_error(interaction, error)
    
    @app_commands.command(name="perfil", description="Muestra información del usuario")
    @app_commands.describe(usuario="Usuario del que quieres ver el perfil")
    async def profile_command(
        self, 
        interaction: discord.Interaction, 
        usuario: discord.Member = None
    ):
        try:
            target_user = usuario or interaction.user
            
            if not isinstance(target_user, discord.Member):
                embed = self.embed_service.create_error_embed(
                    "Error",
                    "No se pudo obtener información del usuario"
                )
                await interaction.response.send_message(embed=embed, ephemeral=True)
                return
            
            embed = self.embed_service.create_user_profile_embed(target_user)
            await interaction.response.send_message(embed=embed)
            
        except Exception as error:
            await self.handle_command_error(interaction, error)
    
    @app_commands.command(name="servidor", description="Información del servidor")
    async def server_info_command(self, interaction: discord.Interaction):
        try:
            guild = interaction.guild
            embed = self.embed_service.create_info_embed(
                f"📊 Información de {guild.name}"
            )
            
            embed.add_field(name="Miembros", value=guild.member_count, inline=True)
            embed.add_field(name="Canales", value=len(guild.channels), inline=True)
            embed.add_field(name="Roles", value=len(guild.roles), inline=True)
            embed.add_field(name="Creado", value=guild.created_at.strftime("%d/%m/%Y"), inline=True)
            
            if guild.icon:
                embed.set_thumbnail(url=guild.icon.url)
                
            await interaction.response.send_message(embed=embed)
            
        except Exception as error:
            await self.handle_command_error(interaction, error)
    
    async def handle_command_error(self, interaction: discord.Interaction, error: Exception):
        embed = self.embed_service.create_error_embed(
            "Error en el comando",
            "Ocurrió un error inesperado. Inténtalo de nuevo."
        )
        
        if interaction.response.is_done():
            await interaction.followup.send(embed=embed, ephemeral=True)
        else:
            await interaction.response.send_message(embed=embed, ephemeral=True)
