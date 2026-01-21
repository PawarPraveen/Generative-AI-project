"""
Database models for website projects
"""
from sqlalchemy import Column, String, Text, DateTime, Integer
from sqlalchemy.sql import func
from datetime import datetime
from ..database import Base


class Project(Base):
    """
    Represents a generated website project
    
    Attributes:
        id: Unique project identifier
        title: Project title/name
        website_type: Type of website (portfolio, ecommerce, blog, landing_page)
        user_prompt: Original user requirements/prompt
        html: Generated HTML content
        css: Generated CSS content
        javascript: Generated JavaScript content
        project_metadata: Additional project metadata (JSON format)
        created_at: Project creation timestamp
        updated_at: Last update timestamp
    """
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    website_type = Column(
        String(50),
        nullable=False,
        index=True,
        comment="portfolio, ecommerce, blog, landing_page"
    )
    user_prompt = Column(Text, nullable=False)
    html = Column(Text, nullable=False)
    css = Column(Text, nullable=False)
    javascript = Column(Text, nullable=True)
    project_metadata = Column(Text, nullable=True, comment="JSON metadata")
    created_at = Column(DateTime, default=func.now(), nullable=False, index=True)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    def __repr__(self) -> str:
        return f"<Project(id={self.id}, title={self.title}, type={self.website_type})>"
