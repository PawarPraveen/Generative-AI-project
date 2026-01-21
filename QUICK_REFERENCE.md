# 🎯 DEPLOYMENT QUICK REFERENCE CARD

## Your URLs After Deployment

```
Frontend:  https://your-app-name.vercel.app
Backend:   https://your-app-name-backend.onrender.com
API Docs:  https://your-app-name-backend.onrender.com/docs
Health:    https://your-app-name-backend.onrender.com/api/health
```

---

## Git Push Command

```bash
cd d:\generative-AI-project
git remote add origin https://github.com/YOUR_USERNAME/ai-website-generator.git
git branch -M main
git push -u origin main
```

---

## Render Deployment

**Environment Variables to Add**:
```
GEMINI_API_KEY = [your Gemini key]
HF_API_TOKEN = [your HuggingFace token]
DATABASE_URL = sqlite:///./website_generator.db
DEBUG = false
```

**Build Command**:
```
pip install -r backend/requirements.txt
```

**Start Command**:
```
uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT
```

---

## Vercel Deployment

**Environment Variable**:
```
NEXT_PUBLIC_API_URL = https://your-backend-url.onrender.com
```

**Root Directory**: `./frontend`

---

## Testing Commands

```bash
# Test backend health
curl https://your-backend-url/api/health

# Should return:
# {"status": "healthy", "message": "AI Website Generator API is running"}
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| CORS error | Check `NEXT_PUBLIC_API_URL` in Vercel |
| Gemini fails | Verify `GEMINI_API_KEY` in Render env |
| 502 error | Wait 30 sec for cold start |
| Build fails | Check environment variables are set |
| Slow generation | Normal (5-15 sec), HF may be slow |

---

## Key URLs

- **GitHub**: https://github.com/new
- **Render**: https://render.com
- **Vercel**: https://vercel.com
- **Gemini API**: https://ai.google.dev/
- **HuggingFace Tokens**: https://huggingface.co/settings/tokens

---

## Documentation Files

1. **START_DEPLOYMENT.md** - Overview
2. **COMPLETE_DEPLOYMENT_GUIDE.md** - Step-by-step
3. **DEPLOYMENT_CHECKLIST.md** - Quick checklist
4. **DEVOPS_READY.md** - Technical details

---

## Success Criteria

- [ ] Code pushed to GitHub
- [ ] Backend deployed to Render (Live status)
- [ ] Frontend deployed to Vercel (Success)
- [ ] Health endpoint returns 200 OK
- [ ] Frontend loads without errors
- [ ] Website generation works
- [ ] No CORS errors in browser

---

## Timeline

- Prerequisites: 5 min
- GitHub Setup: 5 min
- Backend Deploy: 5 min (+ 2-3 min build)
- Frontend Deploy: 5 min (+ 1-2 min build)
- Validation: 5 min
- **TOTAL: 15-20 minutes**

---

**NEXT**: Follow COMPLETE_DEPLOYMENT_GUIDE.md step-by-step! 🚀
