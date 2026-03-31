# 🎯 AI Career Radar

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-14-000000?style=for-the-badge&logo=next.js&logoColor=white)
![Qdrant](https://img.shields.io/badge/Qdrant-Vector_DB-DC244C?style=for-the-badge)
![Sentence Transformers](https://img.shields.io/badge/Sentence_Transformers-AI_Embeddings-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

**An autonomous career intelligence system that doesn't just show you jobs — it understands them, remembers them, and guides you toward the right ones.**

[Features](#-features) · [Architecture](#-architecture) · [Tech Stack](#️-tech-stack) · [Setup](#-setup-instructions) · [API Endpoints](#-api-endpoints) · [Demo](#-live-demo)

</div>

---

## 🚀 Project Overview

Traditional job boards are broken. They overwhelm you with irrelevant listings, rely on keyword matching, and tell you nothing about whether you're actually qualified — or what's standing in your way.

**AI Career Radar** is built differently. It is a fully autonomous job intelligence platform that:

- 🔍 **Fetches and structures** live job data from external APIs
- 🧠 **Understands** job descriptions using AI embeddings — not keyword search
- 📦 **Remembers** jobs semantically in a vector database (Qdrant)
- 🚫 **Deduplicates** listings intelligently using similarity matching
- 🎯 **Recommends** roles personalized to your skill set
- 📊 **Identifies skill gaps** so you know exactly what to learn next

> *"Instead of just showing jobs, this system understands them, remembers them, and guides users toward the most relevant career opportunities."*

---

## ✨ Features

- **🔍 Autonomous Job Discovery** — Fetches structured job listings from backend APIs on demand, always serving fresh data
- **🧠 AI-Powered Understanding** — Uses Sentence Transformer embeddings to extract deep semantic meaning from every job description
- **📦 Vector Memory System** — Jobs are stored in Qdrant as high-dimensional vectors, enabling semantic recall far beyond keyword search
- **🚫 Smart Deduplication** — Detects and removes near-duplicate job listings using cosine similarity, so you never see the same role twice
- **🎯 Personalized Recommendation Engine** — Input your skills and get back a ranked list of roles most aligned to your profile
- **📊 Skill Gap Analysis** — For every recommended role, the system highlights missing skills and surfaces what you need to level up
- **⚡ High-Performance API** — FastAPI backend delivers fast, async responses with auto-generated interactive docs
- **🧩 Modular & Scalable Architecture** — Clean separation of concerns across ingestion, embedding, storage, and recommendation layers

---

## 🏗️ Architecture

AI Career Radar follows a clean, end-to-end intelligence pipeline:

```
User Interface (Next.js)
         │
         ▼
  API Proxy Layer (/api/career)
         │
         ▼
  FastAPI Backend
         │
         ├──► Job Fetching & Structuring
         │
         ▼
  AI Processing Layer
  (Sentence Transformers — Embedding Generation)
         │
         ▼
  Qdrant Vector Database
  (Semantic Storage & Similarity Indexing)
         │
         ├──► Duplicate Detection (Cosine Similarity)
         ├──► Skill-Based Recommendation Search
         └──► Skill Gap Computation
         │
         ▼
  Structured Response → Next.js UI
```

1. **Fetch** — The backend pulls job listings from external sources and structures the raw data
2. **Embed** — Each job description is converted into a vector using Sentence Transformers
3. **Store** — Vectors are indexed in Qdrant for fast semantic retrieval
4. **Deduplicate** — Incoming jobs are similarity-checked against existing vectors to prevent duplicates
5. **Match** — User skills are embedded and matched against the job vector space
6. **Recommend** — Top matches are returned with fit scores and skill gap insights
7. **Display** — The Next.js frontend presents everything in a clean, actionable UI

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | Next.js, React.js, Tailwind CSS |
| **Backend** | FastAPI (Python 3.11+) |
| **Vector Database** | Qdrant |
| **AI / Embeddings** | Sentence Transformers |
| **Similarity Search** | Cosine Similarity via Qdrant |
| **Data Validation** | Pydantic |
| **API Communication** | HTTPX / Requests |
| **Deployment** | architect.space |

---

## 🎥 Live Demo

> 🌐 **Live Backend (API):** [job-quest-stellar-flow-i6fl.architect.space](https://job-quest-stellar-flow-i6fl.architect.space)
>
> 📖 **Interactive API Docs:** [/docs](https://job-quest-stellar-flow-i6fl.architect.space/docs)

---

## ⚙️ Setup Instructions

### Prerequisites

- Python 3.11+
- Node.js 18+
- Docker (for Qdrant)

---

### 1. Clone the Repository

```bash
git clone https://github.com/kishan-maker136/AI-carrer.git
cd AI-carrer
```

---

### 2. Start Qdrant (Vector Database)

```bash
docker pull qdrant/qdrant
docker run -p 6333:6333 qdrant/qdrant
```

Qdrant dashboard available at `http://localhost:6333`

---

### 3. Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file in `/backend`:

```env
QDRANT_HOST=localhost
QDRANT_PORT=6333
COLLECTION_NAME=job_listings
```

Start the backend:

```bash
uvicorn main:app --reload
```

API available at `http://127.0.0.1:8000`  
Interactive docs at `http://127.0.0.1:8000/docs`

---

### 4. Frontend Setup

```bash
cd ../frontend
npm install
```

Create a `.env.local` file in `/frontend`:

```env
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

Start the development server:

```bash
npm run dev
```

Frontend available at `http://localhost:3000`

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/fetch-jobs` | Fetch and store latest job listings |
| `GET` | `/search?query=python` | Semantic job search by keyword or role |
| `POST` | `/recommend` | Get personalized job recommendations |

### `/recommend` — Example Request

```bash
POST /recommend
Content-Type: application/json

["Python", "SQL", "Machine Learning"]
```

```json
// Example Response
{
  "recommendations": [
    {
      "title": "Data Engineer",
      "company": "TechCorp",
      "match_score": 0.91,
      "missing_skills": ["Spark", "Airflow"]
    }
  ]
}
```

---

## ▶️ Usage

1. **Open the app** at `http://localhost:3000`
2. **Trigger job fetching** — The backend pulls and indexes the latest listings via `/fetch-jobs`
3. **Search semantically** — Use `/search?query=your-role` to find roles by meaning, not just keywords
4. **Get recommendations** — Submit your skill set to `/recommend` and receive ranked, personalized job matches
5. **Analyze your gaps** — Review the missing skills for each recommended role and plan your learning path

### Example Workflow

```
User inputs skills: ["Python", "SQL", "Machine Learning"]
         │
         ▼
System embeds skills → searches Qdrant vector space
         │
         ▼
Top job matches returned with similarity scores
         │
         ▼
Skill gap report: "Missing: Apache Spark, Airflow, Kubernetes"
         │
         ▼
User has a clear, focused roadmap — not just a list of jobs
```

---

## 📸 Screenshots / Demo

> 🚧 UI screenshots coming soon.

| View | Preview |
|---|---|
| 🏠 Home / Dashboard | `[ Screenshot Placeholder ]` |
| 🎯 Job Recommendations | `[ Screenshot Placeholder ]` |
| 📉 Skill Gap Report | `[ Screenshot Placeholder ]` |
| 📖 API Docs (Swagger) | `[ Screenshot Placeholder ]` |

---

## 🔮 Future Improvements

- [ ] **📄 Resume Parsing** — Upload a resume to auto-generate your skill profile using NLP
- [ ] **🔔 Real-Time Job Alerts** — Get notified instantly when a high-match role is posted
- [ ] **🤖 LLM Career Coach** — Conversational AI assistant for guided skill development and interview prep
- [ ] **📊 Dashboard Analytics** — Visualize trending skills, salary distributions, and role demand over time
- [ ] **🌐 LinkedIn Integration** — Pull live listings directly from LinkedIn
- [ ] **📱 Mobile App** — Native iOS/Android experience for on-the-go job tracking
- [ ] **🔐 User Authentication** — Secure accounts with profile persistence across sessions

---

## 🧠 What Makes This Special?

| Traditional Job Boards | AI Career Radar |
|---|---|
| Keyword-based search | ✅ Semantic embedding search |
| No memory of listings | ✅ Vector memory via Qdrant |
| Duplicate-heavy results | ✅ AI-powered deduplication |
| Generic listings for everyone | ✅ Skill-personalized recommendations |
| No feedback on qualification | ✅ Clear skill gap analysis |

This project demonstrates real-world competency in **AI/ML pipelines · vector databases · async backend APIs · full-stack development · recommendation systems**.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "feat: your feature description"`
4. Push to your branch: `git push origin feature/your-feature`
5. Open a Pull Request

Please keep PRs focused and well-described.

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

<div align="center">

### **Kishan BC**

*B.Tech CSE (Cybersecurity) · Presidency University, Bangalore*

*Full-Stack Developer · AI/ML Builder · Open Source Enthusiast*

I built AI Career Radar to solve a real problem — the frustration of job hunting without clear direction or feedback. This project reflects my ability to architect and ship full-stack, AI-powered systems end-to-end: from vector databases and embedding pipelines to intelligent APIs and modern UIs.

[![GitHub](https://img.shields.io/badge/GitHub-kishan--maker136-181717?style=for-the-badge&logo=github)](https://github.com/kishan-maker136)
[![Live Demo](https://img.shields.io/badge/Live_Demo-Visit_Now-009688?style=for-the-badge&logo=rocket)](https://job-quest-stellar-flow-i6fl.architect.space/docs)

</div>

---

<div align="center">

*If this project impressed you, drop a ⭐ — it supports the work and helps others discover it.*

</div>