from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AchievementBase(BaseModel):
    title: str
    description: Optional[str] = None
    image_url: Optional[str] = None

class AchievementCreate(AchievementBase):
    pass

class AchievementResponse(AchievementBase):
    id: int
    date_achieved: datetime

    class Config:
        from_attributes = True