from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

@dataclass
class UserModel:
    user_id: int
    username: str
    display_name: str
    joined_at: datetime
    created_at: datetime
    roles: List[str]
    warning_count: int = 0
    
    @property
    def account_age_days(self) -> int:
        return (datetime.utcnow() - self.created_at).days
    
    @property
    def server_member_days(self) -> int:
        return (datetime.utcnow() - self.joined_at).days