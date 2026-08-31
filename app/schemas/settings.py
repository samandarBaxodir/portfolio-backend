from pydantic import BaseModel
from typing import Optional

class SettingsSchema(BaseModel):
    telegram_url: Optional[str] = None
    github_url: Optional[str] = None
    email: Optional[str] = None
    instagram_url: Optional[str] = None
    linkedin_url: Optional[str] = None
    cv_url: Optional[str] = None

    class Config:
        from_attributes = True
