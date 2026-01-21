# Quick Start: Running the Complete Application

This guide walks you through starting both the backend and frontend for the AI Website Generator.

## Prerequisites

- Python 3.12.4 (with virtual environment activated)
- Node.js 25.3.0+ (installed from Phase 2)
- PostgreSQL database running locally
- OpenAI API key

## Step 1: Prepare the Environment

### Backend Environment

1. **Activate Python Virtual Environment:**
   ```bash
   cd d:\generative-AI-project
   .venv\Scripts\activate
   ```

2. **Update .env file with your configuration:**
   ```bash
   cd backend
   cat .env  # View current configuration
   ```
   
   Edit `../.env` to add:
   ```env
   OPENAI_API_KEY=your-api-key-here
   DATABASE_URL=postgresql://user:password@localhost:5432/website_generator
   DEBUG=true
   CORS_ORIGINS=http://localhost:3000,http://localhost:8000
   ```

3. **Verify dependencies are installed:**
   ```bash
   pip list | grep -E "fastapi|sqlalchemy|openai"
   ```

### Database Setup

**Note:** If you haven't set up PostgreSQL yet:

```bash
# Using PostgreSQL command line
psql -U postgres

# In psql:
CREATE DATABASE website_generator;
CREATE USER website_gen WITH PASSWORD 'your_password';
ALTER ROLE website_gen WITH createdb;
GRANT ALL PRIVILEGES ON DATABASE website_generator TO website_gen;
\q
```

## Step 2: Start the Backend

```bash
cd d:\generative-AI-project
.venv\Scripts\activate

# Navigate to backend directory
cd backend

# Start FastAPI development server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Expected Output:**
```
Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
Application startup complete
```

**Verify Backend:**
- API Documentation: http://localhost:8000/docs (Swagger UI)
- ReDoc: http://localhost:8000/redoc
- Health Check: http://localhost:8000/api/health

## Step 3: Start the Frontend (New Terminal)

Open a new PowerShell terminal:

```bash
cd d:\generative-AI-project\frontend

# Ensure dependencies are installed
npm install

# Start development server
npm run dev
```

**Expected Output:**
```
> frontend@0.1.0 dev
> next dev

▲ Next.js 16.1.3 (Turbopack)
✓ Ready in 2s
✓ Ready in 2.1s
```

**Frontend Available At:**
- Application: http://localhost:3000
- HMR Server: http://localhost:3000 (Hot Module Reload enabled)

## Step 4: Test the Application

### 1. Verify Health Status
- Open http://localhost:3000
- Check the "API Status" indicator at the top
- Should show "Connected" in green ✅

### 2. Generate a Website

1. Fill in the form:
   - **Website Title:** "My Portfolio" (optional)
   - **Website Type:** Select "Portfolio"
   - **Description:** "A professional portfolio website for a software developer with dark theme, project showcase, testimonials, and contact form"

2. Click "Generate Website"
3. Wait for API to process (usually 15-30 seconds)
4. Preview should appear in the right panel

### 3. Test Preview Features

- **Open in New Tab:** Click to open generated website in new browser window
- **Download as ZIP:** Creates downloadable file with:
  - `index.html` - Website structure
  - `styles.css` - Styling
  - `script.js` - Interactivity (if generated)

### 4. Test Project History

- Click "Refresh" in Project History panel
- Previously generated projects should appear
- Click eye icon to view project
- Click trash icon to delete project

## Terminal Layout Recommendation

**Terminal 1: Backend**
```
cd d:\generative-AI-project
.venv\Scripts\activate
cd backend
uvicorn app.main:app --reload
```

**Terminal 2: Frontend**
```
cd d:\generative-AI-project\frontend
npm run dev
```

**Terminal 3: Optional - Database/Utilities**
```
# For PostgreSQL commands, Git, etc.
```

## Common Issues & Solutions

### Backend Won't Start

**Error:** `ModuleNotFoundError: No module named 'fastapi'`

**Solution:**
```bash
.venv\Scripts\activate
pip install -r backend/requirements.txt
```

**Error:** `Connection refused - Cannot connect to database`

**Solution:**
1. Verify PostgreSQL is running
2. Check DATABASE_URL in .env matches your setup
3. Ensure database exists: `psql -U postgres -l | grep website_generator`

**Error:** `OPENAI_API_KEY not found`

**Solution:**
1. Set API key in `.env` file
2. Get key from https://platform.openai.com/api-keys
3. Ensure `.env` is in `backend/` directory

### Frontend Won't Start

**Error:** `Port 3000 already in use`

**Solution:**
```bash
# Kill process on port 3000
npx kill-port 3000

# Or use different port
npm run dev -- -p 3001
```

Then update `.env.local`:
```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api
```

**Error:** `API Status shows "Disconnected"`

**Solution:**
1. Verify backend is running on 8000
2. Check CORS_ORIGINS in backend `.env` includes http://localhost:3000
3. Check firewall isn't blocking localhost:8000
4. Restart both servers

### Generated Website Looks Wrong

**Solution:**
1. Open http://localhost:8000/docs
2. Try POST `/api/generate-website` manually
3. Check that OpenAI API key is valid
4. View browser console for JavaScript errors (F12 → Console)

## Production Deployment

For deploying to production (Phase 4-6):

### Backend (Render)
```bash
# Create account at render.com
# Connect GitHub repository
# Set environment variables in Render dashboard
# Auto-deploys on push
```

### Frontend (Vercel)
```bash
# Create account at vercel.com
# Connect GitHub repository
# Update NEXT_PUBLIC_API_URL to production backend URL
# Auto-deploys on push
```

See `SETUP_GUIDE.md` and `ARCHITECTURE.md` for deployment details.

## Stopping Servers

**Gracefully stop servers:**

In each terminal:
```bash
# Press Ctrl+C to stop the server
^C
```

**Deactivate Python environment:**
```bash
deactivate
```

## Next Steps

1. ✅ Run the application as described above
2. ✅ Test all features with different website types
3. ✅ Generate several projects to populate history
4. ✅ Test ZIP download functionality
5. ✅ Check console (F12) for any errors
6. ✅ Review API documentation at http://localhost:8000/docs

## Useful Commands

```bash
# Backend Commands
.venv\Scripts\activate                           # Activate Python env
pip install -r backend/requirements.txt          # Install deps
uvicorn app.main:app --reload                    # Start server

# Frontend Commands
npm install                                      # Install dependencies
npm run dev                                      # Development server
npm run build                                    # Production build
npm run lint                                     # Lint code
npm start                                        # Production server

# Utility Commands
npx kill-port 8000                              # Free port 8000
npx kill-port 3000                              # Free port 3000
curl http://localhost:8000/api/health           # Check backend
curl http://localhost:3000                      # Check frontend
```

## Documentation Reference

- **[Backend Setup](SETUP_GUIDE.md)** - Detailed backend configuration
- **[Frontend Guide](FRONTEND_GUIDE.md)** - Frontend development details
- **[API Documentation](API_DOCUMENTATION.md)** - Complete API reference
- **[Architecture](ARCHITECTURE.md)** - System design and patterns
- **[Phase 1 Report](PHASE1_COMPLETION.md)** - Backend completion details
- **[Phase 2 Report](PHASE2_COMPLETION.md)** - Frontend completion details

## Support

If you encounter issues:

1. Check relevant documentation above
2. Review error messages carefully
3. Check browser console (F12 → Console tab)
4. Check server logs in terminal
5. Verify all prerequisites are installed
6. Try restarting both servers

---

**Status:** Ready to run! ✅  
**Last Updated:** January 20, 2026
