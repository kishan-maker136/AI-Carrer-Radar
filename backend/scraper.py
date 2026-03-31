import requests
from typing import List, Dict

def fetch_jobs() -> List[Dict]:
    # Mock fetching jobs from an API
    # In real scenario, replace with actual job site API
    jobs = [
        {
            "title": "Software Engineer",
            "description": "Develop software using Python, FastAPI, and machine learning.",
            "skills": ["Python", "FastAPI", "Machine Learning"]
        },
        {
            "title": "Data Scientist",
            "description": "Analyze data with Python, pandas, and scikit-learn.",
            "skills": ["Python", "Pandas", "Scikit-learn"]
        },
        {
            "title": "Backend Developer",
            "description": "Build APIs with FastAPI and handle databases.",
            "skills": ["FastAPI", "Databases", "Python"]
        }
    ]
    return jobs
