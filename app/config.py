from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    jwt_secret: str
    cloudinary_cloud_name: str = ""
    cloudinary_api_key: str = ""
    cloudinary_api_secret: str = ""
    supabase_url: str = ""
    supabase_key: str = ""

    class Config:
        env_file = ".env"

settings = Settings()