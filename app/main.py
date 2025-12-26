import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.routes.analyze import router as analyze_router

load_dotenv()

# 1️⃣ Create app FIRST
app = FastAPI(title="Visual Product Measurement System")

# 2️⃣ Mount static folder
app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

# 3️⃣ UI route
@app.get("/ui")
def ui():
    return FileResponse("app/static/index.html")

# 4️⃣ API routes
app.include_router(analyze_router)

@app.get("/")
def root():
    return {"message": "Visual Product Measurement System is running"}

@app.get("/health")
def health():
    return {
        "status": "ok",
        "gemini_key_loaded": bool(os.getenv("GEMINI_API_KEY"))
    }
