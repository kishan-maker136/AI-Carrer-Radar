from typing import List, Dict
from qdrant_db import search_jobs

def recommend_jobs(skills: List[str]) -> Dict:
    # Search for jobs based on skills query
    query = " ".join(skills)
    similar_jobs = search_jobs(query, limit=10)
    
    recommendations = []
    for job in similar_jobs:
        job_skills = set(job.get("skills", []))
        user_skills = set(skills)
        missing_skills = list(job_skills - user_skills)
        recommendations.append({
            "job": job,
            "missing_skills": missing_skills
        })
    
    return {"recommendations": recommendations}
