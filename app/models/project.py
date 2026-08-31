from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    category = Column(String, nullable=False)  # "software" yoki "3d_cad"
    tech_stack = Column(String, nullable=True)  # masalan: "Python, FastAPI"
    media_url = Column(String, nullable=True)   # Cloudinary rasm/video link
    github_url = Column(String, nullable=True)
    demo_url = Column(String, nullable=True)