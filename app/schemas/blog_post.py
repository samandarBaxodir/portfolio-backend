from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class BlogPostBase(BaseModel):
    title: str
    slug: str
    content: str
    tags: Optional[str] = None
    image_urls: List[str] = []

class BlogPostCreate(BlogPostBase):
    pass

class BlogPostResponse(BlogPostBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True