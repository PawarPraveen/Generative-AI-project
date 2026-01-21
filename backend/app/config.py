"""
Application configuration and settings
"""
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # API Configuration
    api_title: str = "AI Website Generator API"
    api_version: str = "2.0.0"
    api_description: str = "Generate responsive websites using Gemini AI with HuggingFace fallback"
    
    # Gemini API Configuration (Primary)
    gemini_api_key: str
    gemini_model: str = "gemini-1.5-flash"
    
    # Hugging Face API Configuration (Fallback)
    hf_api_token: str
    hf_model: str = "mistralai/Mistral-7B-Instruct"
    hf_api_url: str = "https://api-inference.huggingface.co/models"
    
    # Database Configuration
    database_url: str
    
    # Debug Mode
    debug: bool = False
    
    class Config:
        env_file = ".env"
        case_sensitive = False
        extra = "ignore"
    
    def get_cors_origins(self) -> list:
        """Get CORS allowed origins"""
        return ["http://localhost:3000", "http://localhost:8000", "http://127.0.0.1:3000"]


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance"""
    return Settings()
