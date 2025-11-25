from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import uuid
app = FastAPI(title="Sortify AI Backend")

@app.get("/")
def root():
    return {"status":"ok","service":"Sortify AI backend (demo)"}

@app.post("/analyze")
async def analyze(youtube_url: str = Form(None), file: UploadFile = File(None)):
    job_id = str(uuid.uuid4())
    source = youtube_url or (file.filename if file else "unknown")
    # simulated analysis
    return JSONResponse({
        "job_id": job_id,
        "status": "completed",
        "viralScore": 78,
        "bestTitles": ["How to make X in 60s","Top 5 tips from this video"],
        "clips": [
            {"name":"clip_1.mp4","start":"0s","length":"12s"},
            {"name":"clip_2.mp4","start":"13s","length":"10s"}
        ],
        "source": source
    })
