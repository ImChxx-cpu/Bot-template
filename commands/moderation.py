import discord
from discord.ext import commands
from discord import app_commands
from services.embed_service import EmbedService
from services.user_service import UserService

class ModerationCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_service = EmbedService()
        self.user_service = UserService()
    
    @app_commands.command(name="kick", description="Expulsa a un usuario del servidor")
    @app_commands.describe(
        usuario="Usuario a expulsar",
        razon="Razón de la expulsión"
    )
    @app_commands.default_permissions(kick_members=True)
    async def kick_command(
        self, 
        interaction: discord.Interaction, 
        usuario: discord.Member,
        razon: str = "No especificada"
    ):
        try:
            if not await self.user_service.validate_permissions(interaction.user, "kick_members"):
                embed = self.embed_service.create_error_embed(
                    "Sin permisos",
                    "No tienes permisos para expulsar usuarios"
                )
                await interaction.response.send_message(embed=embed, ephemeral=True)
                return
            
            if usuario.top_role >= interaction.user.top_role:
                embed = self.embed_service.create_error_embed(
                    "Error de jerarquía",
                    "No puedes expulsar a alguien con rol igual o superior"
                )
                await interaction.response.send_message(embed=embed, ephemeral=True)
                return
            
            await usuario.kick(reason=f"{interaction.user}: {razon}")
            
            embed = self.embed_service.create_success_embed(
                "✅ Usuario expulsado",
                f"**{usuario.mention}** ha sido expulsado\n**Razón:** {razon}"
            )
            await interaction.response.send_message(embed=embed)
            
        except discord.Forbidden:
            embed = self.embed_service.create_error_embed(
                "Sin permisos",
                "El bot no tiene permisos para expulsar a este usuario"
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except Exception as error:
            await self.handle_moderation_error(interaction, error)
    
    @app_commands.command(name="ban", description="Banea a un usuario del servidor")
    @app_commands.describe(
        usuario="Usuario a banear",
        razon="Razón del baneo",
        dias_eliminar="Días de mensajes a eliminar (0-7)"
    )
    @app_commands.default_permissions(ban_members=True)
    async def ban_command(
        self,
        interaction: discord.Interaction,
        usuario: discord.Member,
        razon: str = "No especificada",
        dias_eliminar: int = 0
    ):
        try:
            if not await self.user_service.validate_permissions(interaction.user, "ban_members"):
                embed = self.embed_service.create_error_embed(
                    "Sin permisos",
                    "No tienes permisos para banear usuarios"
                )
                await interaction.response.send_message(embed=embed, ephemeral=True)
                return
            
            if usuario.top_role >= interaction.user.top_role:
                embed = self.embed_service.create_error_embed(
                    "Error de jerarquía",
                    "No puedes banear a alguien con rol igual o superior"
                )
                await interaction.response.send_message(embed=embed, ephemeral=True)
                return
                
            if not 0 <= dias_eliminar <= 7:
                embed = self.embed_service.create_error_embed(
                    "Parámetro inválido",
                    "Los días deben estar entre 0 y 7"
                )
                await interaction.response.send_message(embed=embed, ephemeral=True)
                return
            
            await usuario.ban(
                reason=f"{interaction.user}: {razon}",
                delete_message_days=dias_eliminar
            )
            
            embed = self.embed_service.create_success_embed(
                "✅ Usuario baneado",
                f"**{usuario.mention}** ha sido baneado\n**Razón:** {razon}"
            )
            await interaction.response.send_message(embed=embed)
            
        except discord.Forbidden:
            embed = self.embed_service.create_error_embed(
                "Sin permisos",
                "El bot no tiene permisos para banear a este usuario"
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except Exception as error:
            await self.handle_moderation_error(interaction, error)
    
    async def handle_moderation_error(self, interaction: discord.Interaction, error: Exception):
        embed = self.embed_service.create_error_embed(
            "Error de moderación",
            "No se pudo completar la acción de moderación"
        )
        
        if interaction.response.is_done():
            await interaction.followup.send(embed=embed, ephemeral=True)
        else:
            await interaction.response.send_message(embed=embed, ephemeral=True)