"""
API routes for website generation
"""
import logging
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas.project import (
    GenerateWebsiteRequest,
    GenerateWebsiteResponse,
    ProjectResponse,
    ProjectListResponse,
    WebsiteType
)
from ..services.website_generator import WebsiteGeneratorService
from ..services.project_service import ProjectService

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api", tags=["projects"])


@router.post(
    "/generate-website",
    response_model=GenerateWebsiteResponse,
    summary="Generate a website from natural language",
    description="Takes user requirements and generates HTML, CSS, and JS using AI"
)
def generate_website(
    request: GenerateWebsiteRequest,
    db: Session = Depends(get_db)
):
    """
    Generate a complete website based on user requirements.
    
    Args:
        request: GenerateWebsiteRequest with user_prompt, website_type, and optional title
        db: Database session
        
    Returns:
        GenerateWebsiteResponse with generated code and project ID
        
    Raises:
        HTTPException: If generation fails or API error occurs
    """
    try:
        # Initialize AI service
        ai_service = WebsiteGeneratorService()
        
        # Generate website code
        generated_code = ai_service.generate_website(
            request.user_prompt,
            request.website_type
        )
        
        # Generate title if not provided
        title = request.title or f"{request.website_type.value.title()} - AI Generated"
        
        # Save to database (note: ai_service returns 'js' not 'javascript')
        project = ProjectService.create_project(
            db=db,
            title=title,
            website_type=request.website_type,
            user_prompt=request.user_prompt,
            html=generated_code['html'],
            css=generated_code['css'],
            javascript=generated_code.get('js', ''),  # Map 'js' to 'javascript' field
            metadata={'source': 'gemini_api_with_hf_fallback'}
        )
        
        return GenerateWebsiteResponse(
            id=project.id,
            title=project.title,
            website_type=project.website_type,
            html=project.html,
            css=project.css,
            javascript=project.javascript,
            created_at=project.created_at
        )
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Validation error: {str(e)}")
    except Exception as e:
        # Log full error for debugging
        logger.error(f"Website generation error: {str(e)}", exc_info=True)
        # Don't crash - return graceful error response with fallback indication
        # This allows frontend to show the partial generation message
        return GenerateWebsiteResponse(
            id=0,  # Temporary/fallback ID
            title=request.title or "Temporary Result",
            website_type=request.website_type,
            html=f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Generation Error</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-white">
    <main class="flex items-center justify-center min-h-screen bg-gray-50">
        <div class="text-center px-6">
            <h1 class="text-4xl font-bold text-gray-900 mb-4">⚠️ Generation Partial</h1>
            <p class="text-xl text-gray-600 mb-8">The AI service encountered temporary issues.</p>
            <div class="bg-blue-50 border border-blue-200 rounded-lg p-6 max-w-md mx-auto">
                <p class="text-sm text-blue-700">✓ Both AI providers were attempted</p>
                <p class="text-sm text-blue-700">✓ Please try again in a moment</p>
                <p class="text-sm text-blue-700">✓ Check backend logs for details</p>
                <p class="text-xs text-gray-600 mt-4">Error: {str(e)[:100]}</p>
            </div>
            <button onclick="location.reload()" class="mt-8 px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition">
                Try Again
            </button>
        </div>
    </main>
</body>
</html>""",
            css="<style>/* Fallback CSS */</style>",
            javascript="<script>/* Fallback JS */</script>",
            created_at=None
        )


@router.get(
    "/projects/{project_id}",
    response_model=ProjectResponse,
    summary="Get a generated project",
    description="Retrieve a previously generated website project by ID"
)
def get_project(
    project_id: int,
    db: Session = Depends(get_db)
):
    """
    Retrieve a generated website project.
    
    Args:
        project_id: ID of the project to retrieve
        db: Database session
        
    Returns:
        ProjectResponse with complete project details
        
    Raises:
        HTTPException: If project not found
    """
    project = ProjectService.get_project(db, project_id)
    
    if not project:
        raise HTTPException(status_code=404, detail=f"Project {project_id} not found")
    
    return ProjectResponse.from_orm(project)


@router.get(
    "/projects",
    response_model=list[ProjectListResponse],
    summary="List all projects",
    description="Retrieve a paginated list of all generated projects"
)
def list_projects(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    website_type: WebsiteType = Query(None),
    db: Session = Depends(get_db)
):
    """
    List all generated projects with pagination.
    
    Args:
        skip: Number of projects to skip (pagination offset)
        limit: Maximum number of projects to return
        website_type: Filter by website type (optional)
        db: Database session
        
    Returns:
        List of ProjectListResponse objects
    """
    projects = ProjectService.list_projects(
        db,
        skip=skip,
        limit=limit,
        website_type=website_type
    )
    
    return [ProjectListResponse.from_orm(p) for p in projects]


@router.delete(
    "/projects/{project_id}",
    summary="Delete a project",
    description="Delete a generated website project by ID"
)
def delete_project(
    project_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete a project.
    
    Args:
        project_id: ID of the project to delete
        db: Database session
        
    Returns:
        Confirmation message
        
    Raises:
        HTTPException: If project not found
    """
    success = ProjectService.delete_project(db, project_id)
    
    if not success:
        raise HTTPException(status_code=404, detail=f"Project {project_id} not found")
    
    return {"message": f"Project {project_id} deleted successfully"}
