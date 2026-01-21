"""
Website Generator Service
Uses Gemini AI with HuggingFace fallback
"""
import logging
from .ai_service import ai_service
from ..schemas.project import WebsiteType

logger = logging.getLogger(__name__)


class WebsiteGeneratorService:
    """Service to generate website code using AI (Gemini + HF fallback)"""
    
    def __init__(self):
        """Initialize website generator"""
        self.ai_service = ai_service
    
    def generate_website(
        self,
        user_prompt: str,
        website_type: str = "landing_page",
        title: str = "My Website"
    ) -> dict:
        """
        Generate a complete website from user description
        
        Args:
            user_prompt: Natural language description of desired website
            website_type: Type of website (landing_page, portfolio, blog, ecommerce)
            title: Website title
        
        Returns:
            dict with keys:
                - html: Complete HTML5 code
                - css: CSS styles
                - js: JavaScript code
                - title: Website title
        
        Raises:
            Exception: If AI generation fails
        """
        logger.info(f"📄 Generating {website_type} website: {title}")
        
        # Enhance prompt with context
        enhanced_prompt = f"""
Website Title: {title}
Website Type: {website_type.replace('_', ' ').title()}

User Description:
{user_prompt}

Please create a complete, production-ready website based on this description.
Make it modern, responsive, and visually appealing.
"""
        
        try:
            # Call AI service (uses Gemini with HF fallback)
            result = self.ai_service.generate_website(
                prompt=enhanced_prompt,
                website_type=website_type
            )
            
            # Add metadata
            result["title"] = title
            result["website_type"] = website_type
            
            logger.info(f"✅ Successfully generated website for: {title}")
            return result
        
        except Exception as e:
            logger.error(f"❌ Failed to generate website: {str(e)}")
            raise Exception(f"Website generation failed: {str(e)}")


# Create singleton instance
website_generator = WebsiteGeneratorService()
