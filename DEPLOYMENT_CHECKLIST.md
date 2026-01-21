# 📋 DEPLOYMENT CHECKLIST - DevOps Quick Reference

## 🎯 Pre-Deployment (5 min)

- [ ] Gemini API key obtained
- [ ] HuggingFace token obtained (optional)
- [ ] GitHub account created
- [ ] Render account created (via GitHub)
- [ ] Vercel account created (via GitHub)
- [ ] Code committed locally
- [ ] `.env` NOT in git (verify with `git status`)

---

## 🚀 GitHub Deployment (5 min)

```bash
cd d:\generative-AI-project

# Add remote
git remote add origin https://github.com/YOUR_USERNAME/ai-website-generator.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Verify**: https://github.com/YOUR_USERNAME/ai-website-generator
- [ ] Repository is public
- [ ] All files present (backend/, frontend/, render.yaml, etc.)
- [ ] No `.env` file visible

---

## 📦 Backend Deployment on Render (5 min)

### 1. Create Service
- [ ] Go to https://render.com
- [ ] Login with GitHub
- [ ] Click "New +" → "Web Service"
- [ ] Select your repository
- [ ] Click "Connect"

### 2. Configure
- [ ] Name: `ai-website-generator-backend`
- [ ] Environment: Python 3
- [ ] Build: `pip install -r backend/requirements.txt`
- [ ] Start: `uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT`
- [ ] Plan: Free

### 3. Environment Variables
```
GEMINI_API_KEY = [your key]
HF_API_TOKEN = [your token]
DATABASE_URL = sqlite:///./website_generator.db
DEBUG = false
```

- [ ] All variables entered
- [ ] Secrets marked as "Sync"

### 4. Deploy & Verify
- [ ] Click "Deploy Service"
- [ ] Wait for "Live" status (2-3 min)
- [ ] Copy your URL: `https://ai-website-generator-backend.onrender.com`

### 5. Health Check
```bash
curl https://your-backend-url/api/health
# Should return: {"status": "healthy", ...}
```

- [ ] Health endpoint responds
- [ ] Status is "healthy"

---

## 🎨 Frontend Deployment on Vercel (5 min)

### 1. Import Project
- [ ] Go to https://vercel.com
- [ ] Login with GitHub
- [ ] Click "Import Project"
- [ ] Select `ai-website-generator` repo
- [ ] Click "Import"

### 2. Configure
- [ ] Project name: `ai-website-generator-frontend`
- [ ] Framework: Next.js (auto-detected)
- [ ] Root directory: `./frontend`
- [ ] Build command: `npm run build`
- [ ] Output: `.next`

### 3. Environment Variables
```
NEXT_PUBLIC_API_URL = https://your-backend-url.onrender.com
```

- [ ] Variable entered (use your actual backend URL)
- [ ] No typos in URL

### 4. Deploy & Verify
- [ ] Click "Deploy"
- [ ] Wait for success (1-2 min)
- [ ] Copy your URL: `https://your-app-name.vercel.app`

### 5. Frontend Check
- [ ] Open frontend URL in browser
- [ ] Page loads without errors
- [ ] Form is visible
- [ ] Browser console has no errors (F12)

---

## 🧪 End-to-End Testing (5 min)

### Test Backend
```bash
# Health check
curl https://your-backend-url/api/health

# API docs
curl https://your-backend-url/docs
```

- [ ] Health endpoint works
- [ ] API docs accessible

### Test Frontend
- [ ] Frontend loads cleanly
- [ ] Form elements visible
- [ ] No CORS errors in console

### Test Full Flow
1. [ ] Go to frontend URL
2. [ ] Enter prompt: "Create a professional website"
3. [ ] Select website type
4. [ ] Click "Generate"
5. [ ] Wait 5-15 seconds
6. [ ] Website preview appears
7. [ ] No errors in console

---

## 📊 Post-Deployment (Ongoing)

### Daily
- [ ] Check health endpoint: `https://your-backend-url/api/health`
- [ ] Verify frontend loads
- [ ] Monitor error logs

### Weekly
- [ ] Review Render logs for errors
- [ ] Review Vercel build logs
- [ ] Check API usage metrics

### Monthly
- [ ] Update dependencies
- [ ] Check for security updates
- [ ] Review performance metrics

---

## 🔗 Your Production URLs

```
Frontend:  https://your-app-name.vercel.app
Backend:   https://your-app-name-backend.onrender.com
API Docs:  https://your-app-name-backend.onrender.com/docs
Health:    https://your-app-name-backend.onrender.com/api/health
```

---

## 🚨 Common Issues & Quick Fixes

| Issue | Fix |
|-------|-----|
| CORS errors | Check `NEXT_PUBLIC_API_URL` in Vercel |
| Gemini fails | Verify `GEMINI_API_KEY` in Render environment |
| Slow generation | Normal (5-15 sec) - HuggingFace may be slow |
| 502 error | Render cold start - wait 30 sec and retry |
| Build fails | Check environment variables are set |
| Database error | First request auto-creates DB - retry |

---

## ✅ Success Criteria

Your deployment is successful when:

- ✅ Backend shows "Live" status on Render
- ✅ Frontend deployment successful on Vercel
- ✅ Health endpoint returns 200 OK
- ✅ Frontend loads without errors
- ✅ Website generation works end-to-end
- ✅ No CORS errors in browser
- ✅ Generated previews display correctly

---

## 🎉 You're Done!

All requirements met:
- ✅ Backend deployed
- ✅ Frontend deployed  
- ✅ Accessible from anywhere
- ✅ Production ready
- ✅ Free tier (no costs)
- ✅ Zero secrets exposed

**Your app is live! Share the frontend URL with anyone!** 🚀

---

## 📞 Support Checklist

If something goes wrong:

- [ ] Check Render logs (Dashboard → Logs)
- [ ] Check Vercel logs (Dashboard → Deployments)
- [ ] Verify environment variables are set
- [ ] Check GitHub code is up to date
- [ ] Try redeploying (Render: Restart → Vercel: Redeploy)
- [ ] Wait for cold start (first request may be slow)
- [ ] Verify API keys are valid
- [ ] Check CORS configuration

---

**Last Updated**: January 20, 2026  
**Status**: Ready for Production Deployment  
**Estimated Time**: 15-20 minutes  
