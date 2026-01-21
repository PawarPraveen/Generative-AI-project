"""
AI Service: Gemini with HuggingFace Fallback
Primary: Google Gemini API
Fallback: HuggingFace Inference API
"""
import logging
import json
import time
import google.generativeai as genai
import requests
from typing import Optional
from ..config import get_settings

logger = logging.getLogger(__name__)

# Get settings
settings = get_settings()

# Fallback HTML template for when both providers fail
FALLBACK_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Website</title>
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
            </div>
            <button onclick="location.reload()" class="mt-8 px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition">
                Try Again
            </button>
        </div>
    </main>
</body>
</html>"""


class AIService:
    """AI service with Gemini primary and HuggingFace fallback"""
    
    def __init__(self):
        """Initialize AI service with both providers"""
        self.settings = settings
        self._init_gemini()
    
    def _init_gemini(self):
        """Initialize Gemini API"""
        try:
            genai.configure(api_key=self.settings.gemini_api_key)
            logger.info("✅ Gemini API initialized successfully")
        except Exception as e:
            logger.warning(f"⚠️ Gemini API initialization failed: {e}")
    
    def generate_website(self, prompt: str, website_type: str = "landing_page") -> dict:
        """
        Generate website code using Gemini or HuggingFace
        
        Args:
            prompt: User description of desired website
            website_type: Type of website (landing_page, portfolio, blog, ecommerce)
        
        Returns:
            dict with 'html', 'css', 'js' keys
        """
        logger.info(f"🔄 Starting website generation for type: {website_type}")
        
        # Build the comprehensive prompt
        system_prompt = self._build_system_prompt(website_type)
        user_prompt = self._build_user_prompt(prompt, website_type)
        
        # Try Gemini first (Primary)
        try:
            result = self._try_gemini(system_prompt, user_prompt)
            if result:
                logger.info("✅ Website generated successfully with Gemini")
                return result
        except Exception as e:
            logger.warning(f"⚠️ Gemini generation error: {str(e)}")
        
        # Fallback to HuggingFace
        logger.info("⚠️ Gemini failed, falling back to HuggingFace")
        try:
            result = self._try_huggingface(system_prompt, user_prompt)
            if result:
                logger.info("✅ Website generated successfully with HuggingFace")
                return result
        except Exception as e:
            logger.warning(f"⚠️ HuggingFace generation error: {str(e)}")
        
        # If both fail, return fallback HTML (no crash!)
        logger.error("❌ Both AI providers failed, returning fallback HTML")
        return {
            "html": FALLBACK_HTML,
            "css": "<style>/* Styles included in HTML */</style>",
            "js": "<script>/* Fallback mode */</script>",
        }
    
    def _build_system_prompt(self, website_type: str) -> str:
        """Build system prompt for consistent output"""
        return """You are a senior UI/UX designer and frontend engineer specializing in modern web design.
        
Your task is to generate a complete, responsive website using:
- Semantic HTML5
- Tailwind CSS (inline styles, no external CSS files)
- Vanilla JavaScript (no external libraries)
- Mobile-first responsive design

CRITICAL REQUIREMENTS:
1. Output ONLY valid JSON with this exact format: {"html": "...", "css": "...", "js": "..."}
2. Include Tailwind CSS CDN in HTML <head>
3. Mobile-first responsive design (md: breakpoints for tablets/desktop)
4. No external libraries, fonts, or assets
5. All CSS must be in <style> tag in <head>
6. All JavaScript must be in <script> tag before </body>
7. Use semantic HTML5 tags: <header>, <nav>, <main>, <section>, <article>, <footer>
8. Implement proper form validation in JavaScript
9. Make it visually appealing with good color schemes
10. Include animations and transitions for better UX

FORBIDDEN:
- External CDN libraries (only Tailwind CSS allowed)
- External fonts or icon libraries
- Commented-out code
- JavaScript console logs in production
- Inline event handlers (use addEventListener)

Focus on clean, maintainable, production-ready code."""
    
    def _build_user_prompt(self, user_description: str, website_type: str) -> str:
        """Build user prompt with context"""
        website_descriptions = {
            "landing_page": "a professional landing page with hero section, features, CTA, and contact info",
            "portfolio": "a developer/designer portfolio with project showcase, skills, and contact section",
            "blog": "a blog website with post listing, categories, search functionality, and article view",
            "ecommerce": "an e-commerce store with product grid, filters, shopping cart, and checkout",
        }
        
        website_desc = website_descriptions.get(website_type, "a modern website")
        
        return f"""Generate {website_desc}.

User Requirements:
{user_description}

Requirements for this website:
1. Clean, modern design with good UX
2. Responsive layout that works on mobile, tablet, and desktop
3. Professional color scheme and typography
4. Interactive elements where appropriate
5. Smooth animations and transitions
6. Accessibility considerations
7. Fast loading (no heavy assets)

Return ONLY the JSON response in this exact format:
{{
  "html": "<html>...</html>",
  "css": "<style>...</style>",
  "js": "<script>...</script>"
}}

Do NOT add any text before or after the JSON."""
    
    def _try_gemini(self, system_prompt: str, user_prompt: str) -> Optional[dict]:
        """Try to generate website using Gemini API"""
        start_time = time.time()
        try:
            logger.info("🚀 Attempting Gemini API...")
            
            # Check if API key is set
            if not self.settings.gemini_api_key:
                logger.error("❌ GEMINI_API_KEY not set in environment")
                return None
            
            model = genai.GenerativeModel(self.settings.gemini_model)
            
            # Combined prompt for Gemini
            full_prompt = f"{system_prompt}\n\n{user_prompt}"
            
            logger.debug(f"Gemini prompt length: {len(full_prompt)} chars")
            
            # Generate with timeout and explicit safety settings
            response = model.generate_content(
                full_prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.7,
                    top_p=0.9,
                    max_output_tokens=4096,
                ),
                safety_settings=[
                    {
                        "category": genai.types.HarmCategory.HARM_CATEGORY_UNSPECIFIED,
                        "threshold": genai.types.HarmBlockThreshold.BLOCK_NONE,
                    }
                ]
            )
            
            # Safely extract text from Gemini response
            if not response:
                logger.warning("⚠️ Gemini returned None response")
                return None
            
            # Gemini SDK: use .text property safely
            response_text = None
            if hasattr(response, 'text'):
                response_text = response.text
            elif hasattr(response, 'candidates') and response.candidates:
                try:
                    response_text = response.candidates[0].content.parts[0].text
                except (IndexError, AttributeError):
                    pass
            
            if not response_text or not response_text.strip():
                logger.warning("⚠️ Gemini returned empty response")
                return None
            
            elapsed = time.time() - start_time
            logger.debug(f"Gemini response received ({elapsed:.1f}s, {len(response_text)} chars)")
            
            # Parse the response
            parsed = self._parse_ai_response(response_text)
            if parsed:
                logger.info(f"✅ Gemini succeeded in {elapsed:.1f}s")
                return parsed
            
            logger.warning("⚠️ Gemini response parsing failed")
            return None
        
        except Exception as e:
            elapsed = time.time() - start_time
            logger.error(f"❌ Gemini API error ({elapsed:.1f}s): {type(e).__name__}: {str(e)[:200]}")
            return None
    
    def _try_huggingface(self, system_prompt: str, user_prompt: str) -> Optional[dict]:
        """Try to generate website using HuggingFace Inference API"""
        start_time = time.time()
        try:
            logger.info("🚀 Attempting HuggingFace API...")
            
            # Check if API token is set
            if not self.settings.hf_api_token:
                logger.error("❌ HF_API_TOKEN not set in environment")
                return None
            
            url = f"{self.settings.hf_api_url}/{self.settings.hf_model}"
            headers = {"Authorization": f"Bearer {self.settings.hf_api_token}"}
            
            # Format prompt for instruction-following models (Mistral)
            # Don't mix system+user, just use clear instruction format
            full_prompt = f"""[INST] You are a professional web developer. Generate a complete, responsive website based on this requirement:

{user_prompt}

Return ONLY valid JSON (no preamble, no explanation) with this exact structure:
{{
  "html": "<html>...</html>",
  "css": "<style>...</style>",
  "js": "<script>...</script>"
}}

Requirements:
- Use semantic HTML5 tags
- Include Tailwind CSS CDN in <head>
- Mobile-first responsive design
- Valid JSON only [/INST]"""
            
            payload = {
                "inputs": full_prompt,
                "parameters": {
                    "max_new_tokens": 4096,
                    "temperature": 0.7,
                    "top_p": 0.9,
                    "do_sample": True,
                }
            }
            
            logger.debug(f"HF request URL: {url}")
            logger.debug(f"HF prompt length: {len(full_prompt)} chars")
            
            response = requests.post(url, json=payload, headers=headers, timeout=90)
            
            elapsed = time.time() - start_time
            logger.debug(f"HuggingFace response status: {response.status_code} (in {elapsed:.1f}s)")
            
            if response.status_code != 200:
                logger.warning(f"⚠️ HuggingFace error {response.status_code}: {response.text[:200]}")
                return None
            
            data = response.json()
            logger.debug(f"HuggingFace response type: {type(data)}, keys: {data.keys() if isinstance(data, dict) else 'N/A'}")
            
            # HuggingFace can return:
            # - list with {"generated_text": "..."}
            # - dict with {"generated_text": "..."}
            # - error responses
            generated_text = None
            
            if isinstance(data, list) and len(data) > 0:
                if isinstance(data[0], dict):
                    generated_text = data[0].get("generated_text", "")
                    logger.debug(f"HF returned list, extracted text: {len(str(generated_text))} chars")
                else:
                    logger.warning(f"⚠️ Unexpected HF response list item type: {type(data[0])}")
            elif isinstance(data, dict):
                generated_text = data.get("generated_text", "")
                logger.debug(f"HF returned dict, extracted text: {len(str(generated_text))} chars")
                # Check for error responses
                if "error" in data:
                    logger.warning(f"⚠️ HuggingFace error: {data.get('error')}")
                    return None
            else:
                logger.warning(f"⚠️ Unexpected HF response type: {type(data)}")
            
            if not generated_text or not str(generated_text).strip():
                logger.warning("⚠️ HuggingFace returned empty response")
                return None
            
            # Parse the response
            parsed = self._parse_ai_response(str(generated_text))
            if parsed:
                logger.info(f"✅ HuggingFace succeeded in {elapsed:.1f}s")
                return parsed
            
            logger.warning("⚠️ HuggingFace response parsing failed")
            return None
        
        except requests.Timeout:
            elapsed = time.time() - start_time
            logger.error(f"❌ HuggingFace timeout ({elapsed:.1f}s, >90s)")
            return None
        except requests.ConnectionError as e:
            elapsed = time.time() - start_time
            logger.error(f"❌ HuggingFace connection error ({elapsed:.1f}s): {str(e)}")
            return None
        except Exception as e:
            elapsed = time.time() - start_time
            logger.error(f"❌ HuggingFace API error ({elapsed:.1f}s): {type(e).__name__}: {str(e)[:200]}")
            return None
    
    def _parse_ai_response(self, response_text: str) -> Optional[dict]:
        """
        Parse AI response to extract HTML, CSS, and JS
        
        The AI should return JSON like:
        {
            "html": "...",
            "css": "...",
            "js": "..."
        }
        
        Handles:
        - Plain JSON
        - JSON wrapped in markdown code blocks
        - Preamble text before JSON
        """
        try:
            if not response_text or not str(response_text).strip():
                logger.warning("⚠️ Empty response text")
                return None
            
            response_text = str(response_text).strip()
            json_str = response_text
            
            # Strategy 1: Extract from markdown code blocks
            if "```json" in json_str:
                parts = json_str.split("```json")
                if len(parts) > 1:
                    json_str = parts[1].split("```")[0].strip()
                    logger.debug("Found JSON in ```json``` block")
            elif "```" in json_str:
                parts = json_str.split("```")
                if len(parts) >= 3:
                    json_str = parts[1].strip()
                    logger.debug("Found JSON in ``` ``` block")
            
            # Strategy 2: Find JSON object in text (look for { and })
            if "{" in json_str and "}" in json_str:
                start_idx = json_str.find("{")
                end_idx = json_str.rfind("}")
                if start_idx != -1 and end_idx != -1 and start_idx < end_idx:
                    json_str = json_str[start_idx:end_idx+1]
                    logger.debug(f"Extracted JSON from positions {start_idx} to {end_idx}")
            
            # Strategy 3: Try to parse as-is
            logger.debug(f"Parsing JSON string (first 200 chars): {json_str[:200]}")
            data = json.loads(json_str)
            
            # Validate required fields
            required_fields = {"html", "css", "js"}
            if not all(field in data for field in required_fields):
                logger.warning(f"⚠️ Missing required fields. Got: {list(data.keys())}")
                # Try to use what we have
                if "html" not in data:
                    logger.error("❌ HTML is missing from response")
                    return None
            
            # Extract and validate content
            html = data.get("html", "").strip() if isinstance(data.get("html"), str) else ""
            css = data.get("css", "").strip() if isinstance(data.get("css"), str) else ""
            js = data.get("js", "").strip() if isinstance(data.get("js"), str) else ""
            
            if not html or len(html) < 50:  # Sanity check: HTML should have some content
                logger.warning(f"⚠️ HTML content too short ({len(html)} chars)")
                return None
            
            logger.info(f"✅ Parsed AI response successfully (HTML: {len(html)} chars)")
            return {
                "html": html,
                "css": css,
                "js": js,
            }
        
        except json.JSONDecodeError as e:
            logger.warning(f"⚠️ JSON parse error at line {e.lineno}, col {e.colno}: {e.msg}")
            logger.debug(f"Response text (first 500 chars): {response_text[:500]}")
            return None
        except Exception as e:
            logger.warning(f"⚠️ Error parsing AI response: {type(e).__name__}: {str(e)}")
            return None


# Create singleton instance
ai_service = AIService()
