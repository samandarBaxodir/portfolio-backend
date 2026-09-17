from sqlalchemy import Column, Integer, String, Text, DateTime, JSON
from datetime import datetime, timezone
from app.database import Base

class BlogPost(Base):
    __tablename__ = "blog_posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False)  # URL uchun, masalan "birinchi-postim"
    content = Column(Text, nullable=False)
    tags = Column(String, nullable=True)  # vergul bilan ajratilgan: "python,ai"
    image_urls = Column(JSON, default=list)  # Rasmlar ro'yxati
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))