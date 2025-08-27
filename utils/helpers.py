import discord
from typing import Optional

class DiscordHelpers:
    @staticmethod
    def format_user_mention(user_id: int) -> str:
        return f"<@{user_id}>"
    
    @staticmethod
    def format_channel_mention(channel_id: int) -> str:
        return f"<#{channel_id}>"
    
    @staticmethod
    def format_role_mention(role_id: int) -> str:
        return f"<@&{role_id}>"
    
    @staticmethod
    def truncate_text(text: str, max_length: int = 100) -> str:
        return text[:max_length] + "..." if len(text) > max_length else text