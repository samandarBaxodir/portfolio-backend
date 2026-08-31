from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.routers import auth, projects, skills, blog, achievements, upload, settings
app = FastAPI(title="Portfolio API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth.router)
app.include_router(projects.router)
app.include_router(skills.router)
app.include_router(blog.router)
app.include_router(achievements.router)
app.include_router(upload.router)
app.include_router(settings.router)

@app.get("/")
def root():
    return {"message": "Portfolio backend ishlayapti"}