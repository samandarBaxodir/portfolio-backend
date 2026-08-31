from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.blog_post import BlogPost
from app.schemas.blog_post import BlogPostCreate, BlogPostResponse
from app.core.dependencies import get_current_admin

router = APIRouter(prefix="/api/blog", tags=["blog"])

# --- OCHIQ ---

@router.get("/", response_model=List[BlogPostResponse])
def get_posts(db: Session = Depends(get_db)):
    return db.query(BlogPost).order_by(BlogPost.created_at.desc()).all()

@router.get("/{slug}", response_model=BlogPostResponse)
def get_post(slug: str, db: Session = Depends(get_db)):
    post = db.query(BlogPost).filter(BlogPost.slug == slug).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post topilmadi")
    return post

# --- HIMOYALANGAN ---

@router.post("/", response_model=BlogPostResponse, status_code=status.HTTP_201_CREATED)
def create_post(
    data: BlogPostCreate,
    db: Session = Depends(get_db),
    current_admin: str = Depends(get_current_admin),
):
    existing = db.query(BlogPost).filter(BlogPost.slug == data.slug).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bu slug allaqachon band")
    new_post = BlogPost(**data.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.put("/{post_id}", response_model=BlogPostResponse)
def update_post(
    post_id: int,
    data: BlogPostCreate,
    db: Session = Depends(get_db),
    current_admin: str = Depends(get_current_admin),
):
    post = db.query(BlogPost).filter(BlogPost.id == post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post topilmadi")
    for key, value in data.model_dump().items():
        setattr(post, key, value)
    db.commit()
    db.refresh(post)
    return post

@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
    post_id: int,
    db: Session = Depends(get_db),
    current_admin: str = Depends(get_current_admin),
):
    post = db.query(BlogPost).filter(BlogPost.id == post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post topilmadi")
    db.delete(post)
    db.commit()