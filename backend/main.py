from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from scraper import fetch_jobs
from processor import process_job
from qdrant_db import init_collection, store_jobs, search_jobs
from recommender import recommend_jobs

app = FastAPI(title="AI Career Radar")

# ✅ CORS FIX (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allows all frontend origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Initialize Qdrant on startup
@app.on_event("startup")
async def startup_event():
    init_collection()


# ✅ Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to AI Career Radar 🚀"}


# ✅ Fetch + Process + Store jobs
@app.get("/fetch-jobs")
async def fetch_and_store_jobs():
    jobs = fetch_jobs()
    processed_jobs = [process_job(job) for job in jobs]

    store_jobs(processed_jobs)

    return {
        "status": "success",
        "jobs_added": len(processed_jobs)
    }


# ✅ Search jobs
@app.get("/search")
async def search(query: str = Query(..., description="Search query for jobs")):
    results = search_jobs(query)

    return {
        "status": "success",
        "query": query,
        "results": results
    }


# ✅ Request model for recommendations
class RecommendRequest(BaseModel):
    skills: List[str]


# ✅ Recommend jobs
@app.post("/recommend")
async def recommend(request: RecommendRequest):
    result = recommend_jobs(request.skills)

    return {
        "status": "success",
        "input_skills": request.skills,
        "data": result
    }