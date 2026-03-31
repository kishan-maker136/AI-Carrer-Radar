from typing import Dict
import os
import requests

USE_LYZR = False  # turn True if API key added

def process_with_lyzr(text: str):
    """
    Example Lyzr API call (pseudo)
    Replace API_KEY if you have one
    """

    api_key = os.getenv("LYZR_API_KEY")

    if not api_key:
        return None

    try:
        response = requests.post(
            "https://api.lyzr.ai/v1/process",
            headers={"Authorization": f"Bearer {api_key}"},
            json={
                "input": text,
                "task": "Extract role, skills, experience, salary"
            }
        )

        return response.json()

    except:
        return None


def process_job(job: Dict) -> Dict:
    processed_job = job.copy()

    text = (job.get("text") or "").lower()

    # 🔥 Try Lyzr first
    if USE_LYZR:
        lyzr_output = process_with_lyzr(text)
        if lyzr_output:
            processed_job.update(lyzr_output)
            return processed_job

    # 🔽 Fallback logic (your current working system)
    role = "AI Engineer"
    if "backend" in text:
        role = "Backend Developer"
    elif "data" in text:
        role = "Data Analyst"

    skills = []
    for skill in ["python", "sql", "react", "aws"]:
        if skill in text:
            skills.append(skill.capitalize())

    processed_job.update({
        "role": role,
        "company": job.get("author", "Unknown"),
        "skills": skills,
        "experience": "0-2 years",
        "salary": "Not mentioned",
        "hiring_intent": "High"
    })

    return processed_job