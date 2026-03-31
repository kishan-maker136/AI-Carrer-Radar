🚀 AI Career Radar
🧠 Intelligent Job Discovery & Recommendation System

AI Career Radar is an AI-powered career intelligence platform that goes beyond traditional job boards.
It understands job data, stores semantic memory, removes duplicates, and recommends jobs based on user skills using AI + Vector Search.

🌟 Key Highlights
🔍 Smart job fetching system (structured extraction)
🧠 AI-based skill understanding
📦 Vector memory using Qdrant
🚫 Duplicate job detection using similarity search
🎯 Personalized job recommendations
📊 Missing skill analysis for users
⚡ FastAPI high-performance backend
🧩 Modular, scalable architecture
🎥 Demo Idea (for judges)

“Instead of just showing jobs, this system understands them, remembers them, and guides users toward the most relevant career opportunities.”

🏗️ Architecture
User Interface (Next.js)
        ↓
API Layer (/api/career proxy)
        ↓
FastAPI Backend
        ↓
AI Processing (Embeddings - Sentence Transformers)
        ↓
Vector Database (Qdrant)
        ↓
Smart Recommendations + Deduplication
        ↓
Response to User
⚙️ Tech Stack
🖥️ Frontend
Next.js
React.js
Tailwind CSS (if used)
⚙️ Backend
FastAPI
Python
🧠 AI / ML
Sentence Transformers
Embedding-based similarity search
📦 Database
Qdrant (Vector Database)
🚀 Features
🔍 Job Discovery

Fetch structured job listings from backend APIs.

🧠 AI Understanding

Extract meaningful job attributes using AI embeddings.

📦 Memory System

Stores jobs in vector space for long-term semantic recall.

🚫 Duplicate Removal

Avoids repeated job listings using similarity matching.

🎯 Recommendation Engine

Matches user skills with job requirements intelligently.

📊 Skill Gap Analysis

Highlights missing skills for better career guidance.

⚙️ Setup Instructions
1. Clone Repository
git clone  https://job-quest-stellar-flow-i6fl.architect.space
cd backend
2. Install Dependencies
pip install -r requirements.txt
3. Run Backend Server
uvicorn main:app --reload
4. Open API Docs
http://127.0.0.1:8000/docs
🔗 API Endpoints
🔍 Fetch Jobs
GET /fetch-jobs
🔎 Search Jobs
GET /search?query=python
🎯 Recommend Jobs
POST /recommend
Request Body:
["Python", "SQL", "Machine Learning"]
🧠 What Makes This Special?

Unlike traditional job portals:

✔ Uses AI embeddings (not keyword search)
✔ Stores semantic memory of jobs
✔ Removes duplicate job listings intelligently
✔ Provides skill-based personalized recommendations
✔ Acts like a career intelligence assistant


This project demonstrates:

🧠 AI-driven decision making
📦 Vector database integration
🎯 Recommendation systems
⚡ Real-time backend APIs
🚀 Scalable SaaS architecture
💡 Future Enhancements
🔔 Real-time job alerts
📱 Mobile app integration
🤖 Advanced LLM-based career coach
📊 Dashboard analytics for users
🌐 Live LinkedIn Integration
👨‍💻 Author

Kishan BC
B.Tech CSE (Cybersecurity)
Presidency University, Bangalore

🏁 Final Note

AI Career Radar is not just a job scraper — it is a career intelligence system that understands, remembers, and recommends the right opportunities using AI.