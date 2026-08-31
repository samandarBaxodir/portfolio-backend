import os
import shutil
import uuid
from fastapi import APIRouter, Depends, UploadFile, File
from app.core.dependencies import get_current_admin

router = APIRouter(prefix="/api/upload", tags=["upload"])

UPLOAD_DIR = "static/uploads"

@router.post("/")
def upload_file(
    file: UploadFile = File(...),
    current_admin: str = Depends(get_current_admin),
):
    ext = file.filename.split(".")[-1]
    unique_name = f"{uuid.uuid4()}.{ext}"
    file_path = os.path.join(UPLOAD_DIR, unique_name)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    file_url = f"/static/uploads/{unique_name}"
    return {"url": file_url}