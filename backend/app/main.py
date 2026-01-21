"""
Main FastAPI application
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import get_settings
from .database import init_db
from .routers import projects, health

# Get settings
settings = get_settings()

# Create FastAPI app
app = FastAPI(
    title=settings.api_title,
    description=settings.api_description,
    version=settings.api_version,
    docs_url="/docs",
    redoc_url="/redoc",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.get_cors_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database
@app.on_event("startup")
def startup():
    """Initialize database on startup"""
    try:
        init_db()
        print("Database initialized successfully")
    except Exception as e:
        print(f"Database initialization warning: {e}")
        print("Note: Ensure PostgreSQL is running and DATABASE_URL is correct in .env")


# Include routers
app.include_router(health.router)
app.include_router(projects.router)


@app.get("/")
def root():
    """Root endpoint"""
    return {
        "message": "AI Website Generator API",
        "version": settings.api_version,
        "docs": "/docs",
        "redoc": "/redoc"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug
    )
