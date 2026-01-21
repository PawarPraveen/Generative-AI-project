# AI-Powered Website Generator

An end-to-end AI application that generates responsive, production-ready websites from natural language requirements using OpenAI's GPT-4.

## 🎯 Overview

The AI Website Generator takes user requirements in plain English and automatically generates:
- **Semantic HTML5** - Clean, accessible markup
- **Tailwind CSS** - Modern responsive styling
- **JavaScript** - Interactive functionality
- **Mobile-First Design** - Works perfectly on all devices

Users can preview websites in real-time, export as ZIP files, and deploy instantly.

## 📋 Tech Stack

### Backend
- **FastAPI** - Modern Python web framework for APIs
- **OpenAI API** - GPT-4 for intelligent code generation
- **PostgreSQL** - Data persistence with SQLAlchemy ORM
- **Uvicorn** - ASGI server

### Frontend
- **Next.js** - React with App Router for modern UI
- **Tailwind CSS** - Utility-first CSS framework
- **TypeScript** - Type-safe development

### Deployment
- **Backend**: Render.com (FastAPI + PostgreSQL)
- **Frontend**: Vercel (Next.js)

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- Node.js 18+
- PostgreSQL 12+
- OpenAI API key

### 1. Setup Backend

```bash
# Clone or navigate to project
cd generative-AI-project

# Create virtual environment (Windows)
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
cd backend
pip install -r requirements.txt

# Create .env file
cp ../.env.example ../.env
# Edit .env with your OpenAI API key and PostgreSQL credentials
```

### 2. Setup Frontend

```bash
# Navigate to frontend
cd ../frontend

# Install dependencies
npm install

# Create environment file
cp .env.example .env.local
```

### 3. Run Backend

```bash
# From backend directory
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

API will be available at: `http://localhost:8000`
- API Docs: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### 4. Run Frontend

```bash
# From frontend directory
cd frontend
npm run dev
```

Frontend will be available at: `http://localhost:3000`

## 📁 Project Structure

```
generative-AI-project/
├── backend/
│   ├── app/
│   │   ├── models/           # SQLAlchemy ORM models
│   │   │   └── project.py    # Project database model
│   │   ├── routers/          # API route handlers
│   │   │   ├── projects.py   # Website generation routes
│   │   │   └── health.py     # Health check endpoint
│   │   ├── schemas/          # Pydantic validation schemas
│   │   │   └── project.py    # Request/response schemas
│   │   ├── services/         # Business logic
│   │   │   ├── website_generator.py  # AI generation logic
│   │   │   └── project_service.py    # Database operations
│   │   ├── main.py           # FastAPI application
│   │   ├── config.py         # Settings & configuration
│   │   └── database.py       # Database connection & session
│   └── requirements.txt      # Python dependencies
├── frontend/
│   ├── app/                  # Next.js app directory
│   ├── components/           # React components
│   ├── lib/                  # Utilities & helpers
│   ├── public/               # Static assets
│   ├── package.json          # Node dependencies
│   └── next.config.js        # Next.js configuration
└── .env.example              # Environment template
└── README.md                 # This file
```

## 🔌 API Endpoints

### POST /api/generate-website
Generate a new website from natural language requirements.

**Request:**
```json
{
    "user_prompt": "Create a portfolio website for a photographer with gallery and contact form",
    "website_type": "portfolio",
    "title": "Photography Portfolio"
}
```

**Response:**
```json
{
    "id": 1,
    "title": "Photography Portfolio",
    "website_type": "portfolio",
    "html": "<html>...</html>",
    "css": "<style>...</style>",
    "javascript": "// JavaScript code",
    "created_at": "2024-01-20T10:30:00"
}
```

### GET /api/projects/{id}
Retrieve a previously generated project.

**Response:**
```json
{
    "id": 1,
    "title": "Photography Portfolio",
    "website_type": "portfolio",
    "user_prompt": "Create a portfolio website...",
    "html": "<html>...</html>",
    "css": "<style>...</style>",
    "javascript": "// JavaScript code",
    "created_at": "2024-01-20T10:30:00",
    "updated_at": "2024-01-20T10:30:00"
}
```

### GET /api/projects
List all generated projects with pagination.

**Query Parameters:**
- `skip`: Number of projects to skip (default: 0)
- `limit`: Number of projects to return (default: 10, max: 100)
- `website_type`: Filter by type (portfolio, ecommerce, blog, landing_page)

### DELETE /api/projects/{id}
Delete a project.

### GET /api/health
Health check endpoint.

## 🤖 AI System Prompt

The backend uses a specialized system prompt that instructs GPT-4 to:

1. **Generate semantic HTML5** with proper accessibility
2. **Use Tailwind CSS** for all styling via CDN
3. **Implement responsive design** with mobile-first approach
4. **Create reusable components**:
   - Navigation with hamburger menu
   - Hero section with CTA
   - Feature grids
   - Contact forms with validation
   - Footer
5. **Output structured JSON** with HTML, CSS, JavaScript

**Key Design Decisions:**
- **Tailwind CSS via CDN**: Fast setup, no build step needed
- **JSON Output**: Structured data for reliable parsing
- **Mobile-first**: Ensures responsive on all devices
- **Semantic HTML**: Better SEO and accessibility
- **Form Validation**: Built-in JavaScript validation

## 🌐 Website Types Supported

- **Portfolio**: Showcase work, skills, and achievements
- **E-Commerce**: Product listings with shopping functionality
- **Blog**: Articles with navigation and categories
- **Landing Page**: High-converting sales pages

## 📦 Frontend Features

### 1. Generation Interface
- Text input for natural language requirements
- Dropdown selector for website type
- Optional custom title
- Generate button with loading state

### 2. Live Preview
- Iframe-based preview of generated website
- Real-time rendering of HTML/CSS/JS
- Responsive viewport testing

### 3. Export & Deployment
- Download generated website as ZIP
- One-click deployment to hosting (mock)
- Copy code snippets

### 4. Project History
- View previously generated projects
- Regenerate with different requirements
- Delete unused projects

## 🛠️ Environment Variables

Create a `.env` file in the root directory:

```env
# Backend Configuration
OPENAI_API_KEY=sk-your-key-here
DATABASE_URL=postgresql://user:password@localhost:5432/website_generator
DEBUG=False

# Frontend Configuration
NEXT_PUBLIC_API_URL=http://localhost:8000
```

**Notes:**
- `OPENAI_API_KEY`: Get from https://platform.openai.com/api-keys
- `DATABASE_URL`: PostgreSQL connection string
- `NEXT_PUBLIC_API_URL`: Backend API URL (public in browser)

## 📊 Database Schema

### Projects Table
```sql
CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    website_type VARCHAR(50) NOT NULL,
    user_prompt TEXT NOT NULL,
    html TEXT NOT NULL,
    css TEXT NOT NULL,
    javascript TEXT,
    metadata TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🚀 Deployment

### Backend (Render.com)

1. Push code to GitHub
2. Create new Web Service on Render
3. Connect GitHub repository
4. Set environment variables:
   - `OPENAI_API_KEY`
   - `DATABASE_URL` (Render PostgreSQL)
   - `DEBUG=False`
5. Deploy

### Frontend (Vercel)

1. Push code to GitHub
2. Import project in Vercel
3. Set environment variable:
   - `NEXT_PUBLIC_API_URL=https://your-backend.onrender.com`
4. Deploy

## 🔐 Security Considerations

- Store sensitive keys in environment variables (never in code)
- Use HTTPS in production
- Validate and sanitize user inputs
- Implement rate limiting on API endpoints
- Use CORS properly for frontend-backend communication
- Sanitize generated HTML before execution

## ⚙️ Performance Optimization

### Backend
- Database connection pooling
- Query optimization with indexes
- Caching for frequently used data

### Frontend
- Code splitting with Next.js
- Image optimization
- CSS minification via Tailwind
- Lazy loading components

## 🐛 Troubleshooting

### Database Connection Error
```
Error: psycopg2.OperationalError: could not connect to server
```
**Solution**: Ensure PostgreSQL is running and DATABASE_URL is correct

### OpenAI API Error
```
Error: AuthenticationError
```
**Solution**: Verify OPENAI_API_KEY is set correctly in .env

### CORS Error
```
Error: Cross-Origin Request Blocked
```
**Solution**: Ensure frontend URL is in CORS_ORIGINS in backend

## 📈 Future Improvements

- [ ] Authentication & user accounts
- [ ] Website analytics dashboard
- [ ] Advanced customization options
- [ ] Multi-page website generation
- [ ] SEO optimization suggestions
- [ ] Performance metrics & audits
- [ ] Team collaboration features
- [ ] Custom domain support
- [ ] SSL certificate management
- [ ] A/B testing framework

## 📝 Limitations

- Generated code requires manual refinement for complex requirements
- OpenAI API costs apply per request
- Database limits image storage (use external CDN)
- Single-page generation (multi-page coming soon)
- No real-time collaborative editing

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit changes with clear messages
4. Push to your fork
5. Create a Pull Request

## 📄 License

MIT License - feel free to use this project for personal or commercial purposes.

## 💬 Support

- GitHub Issues: Report bugs and request features
- Email: support@example.com
- Documentation: See `/docs` endpoint for API reference

---

Built with ❤️ by AI engineers. Happy generating!
