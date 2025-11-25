Sortify AI — Full package (PWA + Backend)
========================================

What's inside:
- frontend/ (PWA files at root: index.html, manifest.json, icon.svg)
- backend/ (FastAPI demo service)
- docker-compose.yml
- README.md (this file)

Goal:
You said you want a 100% working app you can run and upload. This package includes:
- A fully working PWA frontend (runs locally in browser)
- A minimal FastAPI backend that simulates analysis (can be deployed to Railway or run in Docker)
- Instructions below to deploy backend to Railway and to build an installable Android APK from the PWA using PWABuilder

How to run locally (desktop / Termux on Android):
1) Docker (recommended on desktop)
   - Install Docker
   - From package root run:
     docker-compose up --build
   - Backend will be available at http://localhost:8000
2) Alternatively run backend with Python
   - Install Python 3.10+
   - cd backend
   - pip install -r requirements.txt
   - uvicorn main:app --host 0.0.0.0 --port 8000

Connect frontend to backend:
- Edit `index.html` and change `API_BASE` variable (if present) to point to your backend URL (e.g., https://your-service.up.railway.app)

Deploy backend to Railway (mobile-friendly)
------------------------------------------
Railway is the easiest mobile-friendly host.

1. Create GitHub repo (on mobile web):
   - Go to https://github.com and sign in
   - New repository -> name it `sortify-ai-backend` -> Create

2. Upload backend files:
   - In repo -> Add file -> Upload files
   - Upload the files inside /backend (main.py, requirements.txt, Dockerfile, start.sh)
   - Commit

3. Go to https://railway.app -> Sign in with Google
   - New Project -> Deploy from GitHub -> choose your repo
   - Railway will build and deploy. After deploy, copy the provided URL (e.g., https://xyz.up.railway.app)

4. Edit frontend:
   - In index.html find the line: const API_BASE = 'https://demo' (or similar) and replace with your Railway URL + /analyze
   - Upload edited index.html to your phone or host it (Netlify/Storage) or open locally

Build Android APK from PWA using PWABuilder (no laptop required)
--------------------------------------------------------------
1. Open Chrome on your phone and go to your live PWA (or host it on Netlify / GitHub Pages)
2. Visit https://www.pwabuilder.com
3. Paste your PWA URL and follow steps -> choose Android -> download the generated Android package (may require signing keys; PWABuilder provides options)
4. Alternatively: use https://appmaker.xyz or https://webviewwp.com to wrap PWA into APK.

Notes & Next steps
------------------
- The backend included is a demo stub; for real video processing you'll need to add FFmpeg, yt-dlp and Whisper or an API for transcription.
- I can provide full production backend code (FFmpeg + worker + S3 + OpenAI/Whisper integration) and exact Dockerfile if you want to run heavy processing on Railway or a VPS.
- I can also produce a Flutter WebView wrapper project ready for cloud build (GitHub Actions) to produce a Play Store-ready APK.

If you want, say "Deploy backend to Railway" and I'll give the exact mobile-friendly copy-paste steps for each Railway screen and the exact strings to paste into GitHub upload fields.
