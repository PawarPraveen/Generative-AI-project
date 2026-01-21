"""
Pydantic schemas for API request/response validation
"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum


class WebsiteType(str, Enum):
    """Supported website types"""
    PORTFOLIO = "portfolio"
    ECOMMERCE = "ecommerce"
    BLOG = "blog"
    LANDING_PAGE = "landing_page"


class GenerateWebsiteRequest(BaseModel):
    """
    Request schema for generating a website
    
    Attributes:
        user_prompt: Natural language description of desired website
        website_type: Type of website to generate
        title: Optional project title (auto-generated if not provided)
    """
    user_prompt: str = Field(..., min_length=10, max_length=2000)
    website_type: WebsiteType = Field(default=WebsiteType.LANDING_PAGE)
    title: Optional[str] = Field(default=None, max_length=255)


class GeneratedCode(BaseModel):
    """Generated code components"""
    html: str
    css: str
    javascript: Optional[str] = None


class GenerateWebsiteResponse(BaseModel):
    """
    Response schema for website generation
    
    Attributes:
        id: Generated project ID
        title: Project title
        website_type: Type of website
        html: Generated HTML
        css: Generated CSS
        javascript: Generated JavaScript (if applicable)
        created_at: Creation timestamp
    """
    id: int
    title: str
    website_type: WebsiteType
    html: str
    css: str
    javascript: Optional[str] = None
    created_at: datetime
    
    class Config:
        from_attributes = True


class ProjectResponse(BaseModel):
    """Response schema for retrieving a project"""
    id: int
    title: str
    website_type: WebsiteType
    user_prompt: str
    html: str
    css: str
    javascript: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class ProjectListResponse(BaseModel):
    """Response schema for listing projects"""
    id: int
    title: str
    website_type: WebsiteType
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
