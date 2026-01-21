# Deploy Backend to Render - Step by Step

## Prerequisites
- ✅ Render account (free at https://render.com)
- ✅ Gemini API Key (from https://ai.google.dev/)
- ✅ HuggingFace Token (optional, from https://huggingface.co/settings/tokens)
- ✅ Code pushed to GitHub

---

## Step 1: Get Your API Keys (5 minutes)

### 1.1 Get Gemini API Key
1. Go to https://ai.google.dev/
2. Click "Get API Key"
3. Create a new API key
4. Copy the key and save it somewhere safe

### 1.2 Get HuggingFace Token (Optional)
1. Go to https://huggingface.co/settings/tokens
2. Create a new token
3. Copy it and save it somewhere safe

---

## Step 2: Create Render Account

1. Go to https://render.com
2. Click "Sign up"
3. Sign up with GitHub (recommended)
4. Complete the setup

---

## Step 3: Deploy Backend to Render (10 minutes + 2-3 min build)

### 3.1 Create New Web Service
1. Go to https://dashboard.render.com
2. Click "New +" button
3. Select "Web Service"
4. Select "Deploy an existing repository"
5. Click "Connect"

### 3.2 Connect GitHub Repository
1. Authorize Render to access GitHub
2. Find and select: `ai-website-generator`
3. Click "Connect"

### 3.3 Configure Service

Fill in these fields:

| Field | Value |
|-------|-------|
| **Name** | `ai-website-generator-backend` |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r backend/requirements.txt` |
| **Start Command** | `uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT` |
| **Root Directory** | Leave empty |
| **Plan** | Select `Free` tier |

### 3.4 Add Environment Variables

Click "Advanced" and add these variables:

```
GEMINI_API_KEY = [your-gemini-api-key-here]
HF_API_TOKEN = [your-huggingface-token-here]  # Optional
DATABASE_URL = sqlite:///./website_generator.db
```

### 3.5 Deploy
1. Click "Create Web Service"
2. Wait 3-5 minutes for the build to complete
3. Check the logs to see deployment progress

### 3.6 Get Your Backend URL
Once deployed, you'll see a URL like:
```
https://ai-website-generator-backend.onrender.com
```

Save this URL! You'll need it for Vercel.

---

## Step 4: Update Vercel with Backend URL

Once your backend is running:

1. Go to https://vercel.com/dashboard
2. Click your project
3. Go to Settings → Environment Variables
4. Update `NEXT_PUBLIC_API_URL` to your Render URL
5. Click "Save"
6. Go to Deployments and redeploy

---

## Testing Your Deployment

### 4.1 Test Backend Health
In your browser, go to:
```
https://your-backend-url.onrender.com/api/health
```

You should see:
```json
{
  "status": "healthy",
  "message": "API is ready"
}
```

### 4.2 Test Frontend
Go to:
```
https://your-frontend-url.vercel.app
```

You should see the website generator interface.

### 4.3 Test Full Flow
1. Open the frontend URL
2. Enter a website description
3. Select a type
4. Click "Generate"
5. Wait 5-15 seconds
6. Website should be generated

---

## Troubleshooting

### Build Fails
**Check logs:**
1. Go to your Render service
2. Click "Logs"
3. Look for error messages
4. Common issues:
   - Missing `requirements.txt`
   - Wrong Python version
   - Missing environment variables

**Solution:** Re-check the build command and make sure all dependencies are in `requirements.txt`

### Website Generation Fails
**Likely causes:**
1. Gemini API key is invalid
2. HuggingFace token is invalid
3. Backend URL not set in Vercel

**Solution:**
- Verify API keys are correct
- Check Vercel environment variables
- Check Render logs for errors

### CORS Errors in Browser Console
**Solution:**
- Backend CORS is already configured
- Verify frontend is sending requests to correct backend URL
- Check `NEXT_PUBLIC_API_URL` in Vercel settings

### "Service Unavailable" Error
**Solution:**
1. Render free tier sleeps after 15 minutes of inactivity
2. Just refresh the page - it will wake up
3. First load takes 20-30 seconds while waking up
4. Subsequent requests are fast

---

## Success Indicators

You know it worked when:
✅ Render shows "Live" status
✅ Health endpoint returns `{"status": "healthy"}`
✅ Frontend loads without errors
✅ Website generation works end-to-end
✅ No CORS errors in console

---

## Your Final URLs

```
Backend:   https://ai-website-generator-backend.onrender.com
Frontend:  https://ai-website-generator.vercel.app
API Docs:  https://ai-website-generator-backend.onrender.com/docs
Health:    https://ai-website-generator-backend.onrender.com/api/health
```

---

## Deployment Summary

| Component | Platform | Status |
|-----------|----------|--------|
| Backend | Render | 🟢 Running |
| Frontend | Vercel | 🟢 Running |
| Database | SQLite | 🟢 Auto-initialized |
| API Keys | Environment | 🟢 Configured |

---

## Next Steps

1. ✅ Deploy backend to Render (you are here)
2. ✅ Deploy frontend to Vercel (follow VERCEL_DEPLOYMENT_STEPS.md)
3. ⏳ Update Vercel with backend URL
4. ⏳ Test the entire application

---

**Status: Backend Ready for Production!** 🚀
