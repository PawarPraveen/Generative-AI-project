"""
Project service for database operations
"""
from sqlalchemy.orm import Session
from ..models.project import Project
from ..schemas.project import WebsiteType
from typing import List, Optional
import json


class ProjectService:
    """Service for database operations on projects"""
    
    @staticmethod
    def create_project(
        db: Session,
        title: str,
        website_type: WebsiteType,
        user_prompt: str,
        html: str,
        css: str,
        javascript: Optional[str] = None,
        metadata: Optional[dict] = None
    ) -> Project:
        """Create a new project in the database"""
        
        project = Project(
            title=title,
            website_type=website_type,
            user_prompt=user_prompt,
            html=html,
            css=css,
            javascript=javascript or "",
            project_metadata=json.dumps(metadata) if metadata else None
        )
        
        db.add(project)
        db.commit()
        db.refresh(project)
        return project
    
    @staticmethod
    def get_project(db: Session, project_id: int) -> Optional[Project]:
        """Get a project by ID"""
        return db.query(Project).filter(Project.id == project_id).first()
    
    @staticmethod
    def list_projects(
        db: Session,
        skip: int = 0,
        limit: int = 10,
        website_type: Optional[WebsiteType] = None
    ) -> List[Project]:
        """List projects with optional filtering"""
        query = db.query(Project).order_by(Project.created_at.desc())
        
        if website_type:
            query = query.filter(Project.website_type == website_type)
        
        return query.offset(skip).limit(limit).all()
    
    @staticmethod
    def delete_project(db: Session, project_id: int) -> bool:
        """Delete a project by ID"""
        project = db.query(Project).filter(Project.id == project_id).first()
        if project:
            db.delete(project)
            db.commit()
            return True
        return False
    
    @staticmethod
    def update_project(
        db: Session,
        project_id: int,
        title: Optional[str] = None,
        **kwargs
    ) -> Optional[Project]:
        """Update a project"""
        project = db.query(Project).filter(Project.id == project_id).first()
        
        if not project:
            return None
        
        if title:
            project.title = title
        
        for key, value in kwargs.items():
            if hasattr(project, key) and value is not None:
                setattr(project, key, value)
        
        db.commit()
        db.refresh(project)
        return project
