from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.skill import Skill
from app.schemas.skill import SkillCreate, SkillResponse
from app.core.dependencies import get_current_admin

router = APIRouter(prefix="/api/skills", tags=["skills"])

# --- OCHIQ ---

@router.get("/", response_model=List[SkillResponse])
def get_skills(category: str | None = None, db: Session = Depends(get_db)):
    query = db.query(Skill)
    if category:
        query = query.filter(Skill.category == category)
    return query.all()

@router.get("/{skill_id}", response_model=SkillResponse)
def get_skill(skill_id: int, db: Session = Depends(get_db)):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if not skill:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ko'nikma topilmadi")
    return skill

# --- HIMOYALANGAN ---

@router.post("/", response_model=SkillResponse, status_code=status.HTTP_201_CREATED)
def create_skill(
    data: SkillCreate,
    db: Session = Depends(get_db),
    current_admin: str = Depends(get_current_admin),
):
    new_skill = Skill(**data.model_dump())
    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)
    return new_skill

@router.put("/{skill_id}", response_model=SkillResponse)
def update_skill(
    skill_id: int,
    data: SkillCreate,
    db: Session = Depends(get_db),
    current_admin: str = Depends(get_current_admin),
):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if not skill:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ko'nikma topilmadi")
    for key, value in data.model_dump().items():
        setattr(skill, key, value)
    db.commit()
    db.refresh(skill)
    return skill

@router.delete("/{skill_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_skill(
    skill_id: int,
    db: Session = Depends(get_db),
    current_admin: str = Depends(get_current_admin),
):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if not skill:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ko'nikma topilmadi")
    db.delete(skill)
    db.commit()