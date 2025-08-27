import discord
from typing import Optional
from models.user_model import UserModel

class UserService:
    def __init__(self):
        self.users_cache = {}
    
    async def get_user_info(self, user: discord.Member) -> UserModel:
        """Obtiene información completa del usuario"""
        if user.id in self.users_cache:
            return self.users_cache[user.id]
            
        user_model = UserModel(
            user_id=user.id,
            username=user.name,
            display_name=user.display_name,
            joined_at=user.joined_at,
            created_at=user.created_at,
            roles=[role.name for role in user.roles if role.name != "@everyone"]
        )
        
        self.users_cache[user.id] = user_model
        return user_model
    
    async def validate_permissions(self, user: discord.Member, required_permission: str) -> bool:
        """Valida si el usuario tiene los permisos necesarios"""
        try:
            return getattr(user.guild_permissions, required_permission, False)
        except AttributeError:
            return False