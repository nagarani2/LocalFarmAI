🌾 LocalFarm AI

Local-first AI farming assistant for farmers with unreliable internet connectivity.

LocalFarm AI helps farmers ask agricultural questions using a local farming knowledge base powered by Moss semantic retrieval. When the local-first farming flow cannot handle a question, the application falls back to Google Gemini.

---

🚜 Problem

Farmers may have limited or unreliable internet connectivity.

Cloud-only AI assistants can depend on internet connectivity and may introduce network latency.

LocalFarm AI addresses this by using a local-first retrieval approach.

---

💡 Solution

Farmer Question
       ↓
   FastAPI Backend
       ↓
   Moss Retrieval
       ↓
 Is it a farming question
 supported locally?
       ↓
   ┌───┴────┐
  YES      NO
   ↓        ↓
 LOCAL    GEMINI
  Moss     CLOUD
   ↓        ↓
   └── Answer ──┘

The system prioritizes local farming knowledge and uses cloud AI as a fallback.

---

🧠 Key Features

- 🌾 Farming question answering
- 🔎 Moss semantic retrieval
- 🟢 Local-first responses
- ☁️ Gemini cloud fallback
- ⚡ Low-latency local retrieval
- 📊 Moss relevance scores
- ⏱️ Response-time measurement
- 🌐 Simple web interface
- 🔐 Environment-based API key storage

---

🏗️ Technology Stack

Technology| Purpose
Python| Backend logic
FastAPI| API server
Moss| Semantic retrieval
Google Gemini| Cloud fallback
HTML/CSS/JavaScript| Frontend
JSON| Local farming knowledge

---

📁 Project Structure

LocalFarmAI/
│
├── backend/
│   ├── create_index.py
│   ├── main.py
│   ├── moss_retrieval.py
│   ├── requirements.txt
│   └── test_moss.py
│
├── data/
│   └── farming_knowledge.json
│
├── frontend/
│   └── index.html
│
├── file/
│   └── .env
│
├── .gitignore
└── README.md

---

🔎 Moss Retrieval

Moss is used to search the local farming knowledge base.

Example local knowledge:

For rice farming, maintain adequate water during important
growth stages and avoid unnecessary continuous flooding.

A farmer can ask:

Why are rice leaves yellow?

The application retrieves relevant farming information using Moss.

The local response path has been tested at approximately 26 ms in the development environment.

---

☁️ Cloud Fallback

When a question is not handled by the local farming flow, LocalFarm AI uses Google Gemini.

Example:

Question:
What is photosynthesis?

Source:
CLOUD

Retrieval:
Moss

Cloud responses depend on network and API latency and can therefore take longer than local retrieval.

---

⚙️ Installation

1. Install dependencies

py -m pip install -r backend/requirements.txt

2. Configure environment variables

Create:

file/.env

Add your own credentials:

MOSS_PROJECT_ID=your_moss_project_id
MOSS_PROJECT_KEY=your_moss_project_key
GEMINI_API_KEY=your_gemini_api_key

Never commit ".env" or API keys to GitHub.

---

🔎 Create the Moss Index

Run from the project root:

py backend/create_index.py

---

🚀 Run the Backend

py -m uvicorn backend.main:app

Backend:

http://127.0.0.1:8000

Health check:

http://127.0.0.1:8000/health

---

🌐 Run the Frontend

Open another terminal:

py -m http.server 5500 --directory frontend

Then open:

http://localhost:5500/

---

🧪 Example

Local question

Why are rice leaves yellow?

Expected:

Source: LOCAL
Retrieval: Moss

Cloud fallback question

What is photosynthesis?

Expected:

Source: CLOUD
Retrieval: Moss

---

🔐 Security

API credentials are stored in:

file/.env

The environment file is excluded from Git using ".gitignore".

API keys should never be placed directly inside source code or committed to the public repository.

---

🎯 Project Goal

LocalFarm AI demonstrates a local-first AI architecture for agricultural assistance.

The project focuses on:

- Local-first AI
- Fast local semantic retrieval
- Cloud fallback
- Low-connectivity use cases
- Practical agricultural assistance

---

🏆 Hackathon

Built for the Moss Zero Latency Builder Sprint.

Project: LocalFarm AI