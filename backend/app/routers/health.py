"""
Health check endpoint
"""
from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["health"])


@router.get(
    "/health",
    summary="Health check",
    description="Check if the API is running"
)
def health_check():
    """Simple health check endpoint"""
    return {
        "status": "healthy",
        "message": "AI Website Generator API is running"
    }
