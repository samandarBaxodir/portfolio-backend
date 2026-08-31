from sqlalchemy import Column, Integer, String
from app.database import Base

class SiteSettings(Base):
    __tablename__ = "site_settings"

    id = Column(Integer, primary_key=True, default=1)
    telegram_url = Column(String, nullable=True)
    github_url = Column(String, nullable=True)
    email = Column(String, nullable=True)
    instagram_url = Column(String, nullable=True)
    linkedin_url = Column(String, nullable=True)
    cv_url = Column(String, nullable=True)
