# Deploy Frontend to Vercel - Step by Step

## Prerequisites
- ✅ GitHub account (create at https://github.com/signup)
- ✅ Code pushed to GitHub
- ✅ Vercel account (free tier at https://vercel.com)

---

## Step 1: Push Code to GitHub (5 minutes)

### 1.1 Create GitHub Repository
1. Go to https://github.com/new
2. Repository name: `ai-website-generator`
3. Description: `AI-powered website generator with Gemini & HuggingFace`
4. Make it **PUBLIC**
5. Click "Create repository"

### 1.2 Push Your Code
Copy and paste these commands in PowerShell:

```powershell
cd d:\generative-AI-project

git remote add origin https://github.com/YOUR_USERNAME/ai-website-generator.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

### 1.3 Verify
- Go to https://github.com/YOUR_USERNAME/ai-website-generator
- You should see all your code there

---

## Step 2: Deploy Frontend to Vercel (10 minutes + 2-3 min build)

### 2.1 Create Vercel Account
1. Go to https://vercel.com/signup
2. Click "Continue with GitHub"
3. Authorize Vercel to access your GitHub account
4. Complete signup

### 2.2 Import Your GitHub Project
1. Go to https://vercel.com/dashboard
2. Click "Add New..." → "Project"
3. Select "Import Git Repository"
4. Search for `ai-website-generator`
5. Click "Import"

### 2.3 Configure Project
On the "Configure Project" page:

**Framework Preset:**
- Select: `Next.js`

**Root Directory:**
- Set to: `./frontend`
- This is CRITICAL - Vercel needs to know the frontend is in the `frontend` folder

**Environment Variables:**
Add these variables:

| Name | Value |
|------|-------|
| `NEXT_PUBLIC_API_URL` | `https://your-backend-url.onrender.com` |

**Note:** Leave the backend URL empty for now. You'll update it after deploying the backend to Render.

### 2.4 Deploy
1. Click "Deploy"
2. Wait 2-3 minutes for the build to complete
3. You'll see a "Congratulations" screen with your live URL

### 2.5 Get Your Frontend URL
Example: `https://ai-website-generator.vercel.app`

This is your public frontend URL! Save it.

---

## Step 3: Update Vercel with Backend URL (After Backend Deployed)

Once your backend is deployed to Render:

1. Go to https://vercel.com/dashboard
2. Click your project `ai-website-generator`
3. Go to Settings → Environment Variables
4. Find `NEXT_PUBLIC_API_URL`
5. Update it to your Render backend URL (e.g., `https://ai-website-generator-backend.onrender.com`)
6. Click "Save"
7. Click "Deployments" → Redeploy the latest deployment

---

## Troubleshooting

### Build Fails with "Module not found"
**Solution:**
- Make sure root directory is set to `./frontend`
- Verify `package.json` exists in `./frontend` folder
- Check that all dependencies in `package.json` are listed

### Build Succeeds but Site Shows Error
**Solution:**
- Check environment variable `NEXT_PUBLIC_API_URL` is set correctly
- Make sure backend API is running and accessible
- Check browser console for errors (F12)

### Site Shows "Cannot GET /"
**Solution:**
- Make sure `Next.js` framework is selected
- Verify root directory is `./frontend`
- Redeploy the project

### CORS Errors
**Solution:**
- Backend CORS is already configured
- Verify `NEXT_PUBLIC_API_URL` doesn't have trailing slash
- Try: `https://your-backend.onrender.com` (not `https://your-backend.onrender.com/`)

---

## Success Indicators

You know it worked when:
✅ Vercel shows "Deployment successful"
✅ You have a live URL (e.g., `https://ai-website-generator.vercel.app`)
✅ Website loads in browser
✅ No 404 errors
✅ (After updating backend URL) Website generation works

---

## Your Final URLs

After deployment:

```
Frontend:  https://YOUR-APP-NAME.vercel.app
Backend:   https://YOUR-APP-NAME-backend.onrender.com (deploy this separately)
```

---

## Next Steps

1. ✅ Deploy frontend to Vercel (you are here)
2. ⏳ Deploy backend to Render (NEXT)
3. ⏳ Update Vercel with backend URL
4. ⏳ Test the entire application

---

## Quick Command Reference

```bash
# Push to GitHub
git push -u origin main

# Check git status
git status

# View git log
git log --oneline -5
```

---

**Status: Ready to Deploy!** 🚀
