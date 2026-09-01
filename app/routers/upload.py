import uuid
from fastapi import APIRouter, Depends, UploadFile, File
from supabase import create_client
from app.config import settings
from app.core.dependencies import get_current_admin

router = APIRouter(prefix="/api/upload", tags=["upload"])

supabase = create_client(settings.supabase_url, settings.supabase_key)
BUCKET = "uploads"

@router.post("/")
async def upload_file(
    file: UploadFile = File(...),
    current_admin: str = Depends(get_current_admin),
):
    ext = file.filename.split(".")[-1]
    unique_name = f"{uuid.uuid4()}.{ext}"

    content = await file.read()
    supabase.storage.from_(BUCKET).upload(unique_name, content, {"content-type": file.content_type})

    file_url = f"{settings.supabase_url}/storage/v1/object/public/{BUCKET}/{unique_name}"
    return {"url": file_url}
