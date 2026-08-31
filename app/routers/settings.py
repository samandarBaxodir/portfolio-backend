from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.settings import SiteSettings
from app.schemas.settings import SettingsSchema
from app.core.dependencies import get_current_admin

router = APIRouter(prefix="/api/settings", tags=["settings"])

@router.get("/", response_model=SettingsSchema)
def get_settings(db: Session = Depends(get_db)):
    settings = db.query(SiteSettings).filter(SiteSettings.id == 1).first()
    if not settings:
        settings = SiteSettings(id=1)
        db.add(settings)
        db.commit()
        db.refresh(settings)
    return settings

@router.put("/", response_model=SettingsSchema)
def update_settings(
    data: SettingsSchema,
    db: Session = Depends(get_db),
    current_admin: str = Depends(get_current_admin),
):
    settings = db.query(SiteSettings).filter(SiteSettings.id == 1).first()
    if not settings:
        settings = SiteSettings(id=1)
        db.add(settings)
    for key, value in data.model_dump().items():
        setattr(settings, key, value)
    db.commit()
    db.refresh(settings)
    return settings
