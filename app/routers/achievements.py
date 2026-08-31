from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.achievement import Achievement
from app.schemas.achievement import AchievementCreate, AchievementResponse
from app.core.dependencies import get_current_admin

router = APIRouter(prefix="/api/achievements", tags=["achievements"])

# --- OCHIQ ---

@router.get("/", response_model=List[AchievementResponse])
def get_achievements(db: Session = Depends(get_db)):
    return db.query(Achievement).order_by(Achievement.date_achieved.desc()).all()

@router.get("/{achievement_id}", response_model=AchievementResponse)
def get_achievement(achievement_id: int, db: Session = Depends(get_db)):
    achievement = db.query(Achievement).filter(Achievement.id == achievement_id).first()
    if not achievement:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Yutuq topilmadi")
    return achievement

# --- HIMOYALANGAN ---

@router.post("/", response_model=AchievementResponse, status_code=status.HTTP_201_CREATED)
def create_achievement(
    data: AchievementCreate,
    db: Session = Depends(get_db),
    current_admin: str = Depends(get_current_admin),
):
    new_achievement = Achievement(**data.model_dump())
    db.add(new_achievement)
    db.commit()
    db.refresh(new_achievement)
    return new_achievement

@router.put("/{achievement_id}", response_model=AchievementResponse)
def update_achievement(
    achievement_id: int,
    data: AchievementCreate,
    db: Session = Depends(get_db),
    current_admin: str = Depends(get_current_admin),
):
    achievement = db.query(Achievement).filter(Achievement.id == achievement_id).first()
    if not achievement:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Yutuq topilmadi")
    for key, value in data.model_dump().items():
        setattr(achievement, key, value)
    db.commit()
    db.refresh(achievement)
    return achievement

@router.delete("/{achievement_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_achievement(
    achievement_id: int,
    db: Session = Depends(get_db),
    current_admin: str = Depends(get_current_admin),
):
    achievement = db.query(Achievement).filter(Achievement.id == achievement_id).first()
    if not achievement:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Yutuq topilmadi")
    db.delete(achievement)
    db.commit()