from sqlalchemy import Column, Integer, String
from app.database import Base

class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)        # masalan: "Python"
    category = Column(String, nullable=False)     # masalan: "backend", "mobile", "3d_cad"
    level = Column(Integer, nullable=False)        # 1-5 orasida daraja