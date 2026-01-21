# 🧪 Comprehensive Testing Guide

## Server Status Check

### ✅ Backend Status
```
http://localhost:8000/api/health
```

Should return:
```json
{
  "status": "ok",
  "version": "2.0.0"
}
```

### ✅ Frontend Status
```
http://localhost:3000
```

Should show the website generator form with:
- Title input field
- Website Type dropdown (4 options)
- Description textarea
- Generate button
- Health check indicator (should be green)

---

## Test Suite

### TEST 1: Basic Generation (Gemini Path)

**Steps:**
1. Open http://localhost:3000
2. Fill form:
   - **Title:** "Tech Startup Landing Page"
   - **Type:** "Landing Page"
   - **Description:** "Create a modern tech startup landing page with hero section, features list, pricing table, and contact form. Use a professional blue and white color scheme with smooth animations."
3. Click "Generate Website"

**Expected Output:**
- Loading indicator appears
- After 5-8 seconds: Website preview appears
- HTML, CSS, and JS all populate
- Save/Download buttons become active

**Backend Logs Should Show:**
```
🔄 Starting website generation for type: landing_page
🚀 Attempting Gemini API...
✅ Website generated successfully with Gemini
✅ Parsed AI response successfully
```

**Success Criteria:**
- ✅ Website appears in preview
- ✅ Website is responsive (try mobile view)
- ✅ Website is functional (click buttons, etc.)
- ✅ HTML contains semantic tags (header, main, section, footer)
- ✅ CSS uses Tailwind classes

---

### TEST 2: Different Website Type (Portfolio)

**Steps:**
1. Clear form
2. Fill form:
   - **Title:** "John Designer Portfolio"
   - **Type:** "Portfolio"
   - **Description:** "Create a portfolio website for a UX/UI designer showcasing past projects, skills, testimonials, and contact information. Make it modern and visually impressive with a dark theme."
3. Click "Generate Website"

**Expected Output:**
- Website generates with portfolio layout
- Shows projects in grid
- Has about section and contact form

**Backend Logs:**
```
🔄 Starting website generation for type: portfolio
🚀 Attempting Gemini API...
✅ Website generated successfully with Gemini
```

**Success Criteria:**
- ✅ Portfolio structure visible
- ✅ Project cards or grid layout
- ✅ Skills section present
- ✅ Contact information included

---

### TEST 3: E-Commerce Website

**Steps:**
1. Fill form:
   - **Title:** "TechGear Shop"
   - **Type:** "E-Commerce"
   - **Description:** "Create an e-commerce store for selling tech accessories. Include product grid, filters by category, shopping cart functionality, and checkout. Use a modern design with product images (use placeholder colors)."
2. Click "Generate Website"

**Expected Output:**
- E-commerce store layout appears
- Product cards visible
- Cart functionality present
- Professional styling

**Backend Logs:**
```
🔄 Starting website generation for type: ecommerce
🚀 Attempting Gemini API...
✅ Website generated successfully with Gemini
```

**Success Criteria:**
- ✅ Product grid visible
- ✅ Cart icon or button present
- ✅ Filter/category section shown
- ✅ Responsive on mobile

---

### TEST 4: Blog Website

**Steps:**
1. Fill form:
   - **Title:** "Tech News Blog"
   - **Type:** "Blog"
   - **Description:** "Create a tech news blog with article listings, search functionality, categories, and an individual article view. Include a modern design with featured articles section."
2. Click "Generate Website"

**Expected Output:**
- Blog layout with article listings
- Category navigation
- Search functionality
- Professional typography

**Backend Logs:**
```
🔄 Starting website generation for type: blog
🚀 Attempting Gemini API...
✅ Website generated successfully with Gemini
```

**Success Criteria:**
- ✅ Article list visible
- ✅ Search bar present
- ✅ Categories or tags shown
- ✅ Article preview cards shown

---

### TEST 5: Fallback Path (Simulate Both Providers Failing)

**Manual Test (Advanced):**

1. **Temporarily disable Gemini:**
   - Edit `backend/.env`
   - Change `GEMINI_API_KEY=invalid_key_test`
   - Save file
   - Backend auto-reloads

2. **Try generation:**
   - Go to http://localhost:3000
   - Fill form and click "Generate"

3. **Observe:**
   - After ~15 seconds, fallback HTML appears
   - Fallback page shows "⚠️ Generation Partial"
   - "Try Again" button is clickable
   - **No 500 error!** Server stays healthy

**Backend Logs Should Show:**
```
🔄 Starting website generation for type: landing_page
🚀 Attempting Gemini API...
⚠️ Gemini API error: ...invalid_key...
⚠️ Gemini failed, falling back to HuggingFace
🚀 Attempting HuggingFace API...
⚠️ HuggingFace API error: ...
❌ Both AI providers failed, returning fallback HTML
✅ Returned fallback website (graceful degradation)
```

4. **Restore Gemini:**
   - Change key back to valid value
   - Backend reloads
   - Verify generation works again

**Success Criteria:**
- ✅ No 500 error appears
- ✅ Fallback HTML renders properly
- ✅ "Try Again" button works
- ✅ Backend stays running
- ✅ Logs show both providers attempted

---

### TEST 6: Save/Download Functionality

**Steps:**
1. Generate a website successfully
2. Click "Save Project" button
3. Go to "Project History" or reload page
4. Verify project appears in list
5. Click project to view
6. Click "Download as ZIP"
7. Verify ZIP file downloads

**Expected Output:**
- Project saved to database
- Appears in project history
- Can download as ZIP file
- ZIP contains all HTML/CSS/JS files

**Success Criteria:**
- ✅ Project saves and retrieves
- ✅ ZIP file downloads correctly
- ✅ ZIP file contains valid files
- ✅ Downloaded HTML renders

---

### TEST 7: API Direct Testing

**Generate Website via cURL:**
```bash
curl -X POST http://localhost:8000/api/generate-website \
  -H "Content-Type: application/json" \
  -d '{
    "user_prompt": "A simple one-page portfolio with name, skills, and contact",
    "website_type": "portfolio",
    "title": "My Portfolio"
  }'
```

**Expected Response:**
```json
{
  "id": 1,
  "title": "My Portfolio",
  "website_type": "portfolio",
  "html": "<html>...</html>",
  "css": "<style>...</style>",
  "javascript": "<script>...</script>",
  "created_at": "2026-01-20T03:15:00"
}
```

**Success Criteria:**
- ✅ HTTP 200 response
- ✅ All fields present
- ✅ HTML/CSS/JS are valid
- ✅ ID is numeric
- ✅ Timestamp is current

---

### TEST 8: Multiple Generations (Stress Test)

**Steps:**
1. Generate 5 websites in succession with different types
2. Monitor backend for errors
3. Check database shows all projects
4. Verify no memory leaks or slowdowns

**Expected Output:**
- All 5 generate successfully
- Each within 5-8 seconds (Gemini)
- Backend remains responsive
- No errors in logs
- All projects saved

**Backend Logs:**
```
[Generation 1] ✅ Website generated with Gemini
[Generation 2] ✅ Website generated with Gemini
[Generation 3] ✅ Website generated with Gemini
[Generation 4] ✅ Website generated with Gemini
[Generation 5] ✅ Website generated with Gemini
```

**Success Criteria:**
- ✅ All generate successfully
- ✅ No slowdown after 5 generations
- ✅ Memory usage stable
- ✅ No connection errors
- ✅ All 5 in project history

---

## Troubleshooting

### Problem: Website doesn't generate after 30 seconds

**Check:**
1. Backend logs for errors
2. API keys in `.env` are correct
3. Network connectivity to Google/HuggingFace APIs
4. Rate limiting (>50 req/min for Gemini)

**Solution:**
```bash
# Restart backend
Get-Process python | Stop-Process -Force
.venv\Scripts\python.exe -m uvicorn backend.app.main:app --reload
```

### Problem: Fallback HTML appears immediately

**Check:**
1. Backend logs for provider errors
2. API keys validity
3. .env file is loaded (check backend startup logs)

**Solution:**
```bash
# Verify API keys work
# Try generation again
# Check logs for specific error message
```

### Problem: Downloaded ZIP file is empty

**Check:**
1. Generation actually completed
2. HTML/CSS/JS fields are populated
3. Database has project saved

**Solution:**
```bash
# Verify in database
# Check backend logs for save errors
# Try generation again
```

---

## Monitoring Checklist

- [ ] Backend running on :8000 ✅
- [ ] Frontend running on :3000 ✅
- [ ] Health check endpoint responding ✅
- [ ] Gemini API key valid ✅
- [ ] HuggingFace token valid ✅
- [ ] Database initialized ✅
- [ ] CORS configured correctly ✅
- [ ] Logs showing ✅ for generations ✅
- [ ] Fallback HTML renders ✅
- [ ] Download functionality works ✅

---

## Performance Baselines

| Operation | Expected Time | Acceptable Range |
|-----------|----------------|-----------------|
| Gemini generation | 6 seconds | 3-10 seconds |
| HF generation | 12 seconds | 5-20 seconds |
| Fallback HTML | 0.5 seconds | <1 second |
| Database save | 100ms | <500ms |
| Project retrieval | 50ms | <200ms |
| Total API response | 6-12 seconds | 5-20 seconds |

---

## Success Criteria Summary

✅ **All Tests Passing If:**
1. Gemini generates websites in 5-8 seconds
2. HuggingFace fallback works in 10-15 seconds
3. Fallback HTML renders when both fail
4. No 500 errors in any scenario
5. Backend logs are detailed and clear
6. Projects save and retrieve correctly
7. All website types generate correctly
8. Download/Save functionality works
9. UI is responsive and user-friendly
10. Multiple generations work without slowdown

---

## Final Verification

Run this command to see all backend logs:

```powershell
# Watch backend logs in real-time
# Should see: 🔄🚀✅⚠️ symbols
# No ❌ errors should appear
```

**The system is production-ready when:**
- ✅ All 8 tests pass
- ✅ No 500 errors observed
- ✅ Both providers work reliably
- ✅ Fallback catches edge cases
- ✅ Performance within baselines
- ✅ Detailed logging throughout
- ✅ User experience is smooth

---

**Test Date:** January 20, 2026  
**Backend Version:** 2.0.0 (Hardened)  
**Status:** ✅ READY FOR TESTING
