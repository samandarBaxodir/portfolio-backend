from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.database import Base

class BlogPost(Base):
    __tablename__ = "blog_posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False)  # URL uchun, masalan "birinchi-postim"
    content = Column(Text, nullable=False)
    tags = Column(String, nullable=True)  # vergul bilan ajratilgan: "python,ai"
    created_at = Column(DateTime, default=datetime.utcnow)