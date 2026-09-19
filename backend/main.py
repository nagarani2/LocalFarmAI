import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai

from backend.moss_retrieval import (
    load_farming_index,
    search_farming_knowledge
)


# Load environment variables
load_dotenv("file/.env")


# Gemini client
gemini_client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


app = FastAPI(
    title="LocalFarm AI",
    description="Local-first AI farming assistant",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Question(BaseModel):
    question: str


@app.on_event("startup")
async def startup_event():

    print("Loading Moss farming knowledge index...")

    await load_farming_index()

    print("Moss index ready.")


@app.get("/")
def home():
    return {
        "project": "LocalFarm AI",
        "status": "running",
        "retrieval": "Moss"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "retrieval": "Moss"
    }


async def ask_gemini(question: str):

    prompt = f"""
You are LocalFarm AI, a helpful farming assistant.

Answer the farmer's question clearly and practically.

Question:
{question}

Give a concise answer suitable for a farmer.

Do not invent specific pesticide or fertilizer dosages.

Recommend local agricultural guidance when appropriate.
"""

    response = gemini_client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text


@app.post("/ask")
async def ask_farmer(question: Question):

    # Search local Moss knowledge first
    results = await search_farming_knowledge(
        question.question
    )

    # Debug information
    print()
    print("QUESTION:", question.question)
    print("MOSS RESULTS:", results)
    print()

    # Farming-related words
    farming_words = [
        "farm",
        "farmer",
        "farming",
        "crop",
        "rice",
        "wheat",
        "tomato",
        "cotton",
        "groundnut",
        "plant",
        "plants",
        "soil",
        "water",
        "irrigation",
        "fertilizer",
        "fertiliser",
        "pest",
        "pests",
        "disease",
        "leaf",
        "leaves",
        "agriculture",
        "agricultural",
        "field",
        "seed",
        "seeds",
        "harvest"
    ]

    question_lower = question.question.lower()

    is_farming_question = any(
        word in question_lower
        for word in farming_words
    )


    # LOCAL-FIRST PATH
    if (
        results
        and results[0]["score"] >= 0.75
        and is_farming_question
    ):

        relevant_points = []

        for item in results[:3]:
            relevant_points.append(item["text"])

        answer = (
            "Based on local farming knowledge: "
            + " ".join(relevant_points)
        )

        source = "LOCAL"


    # CLOUD FALLBACK PATH
    else:

        answer = await ask_gemini(
            question.question
        )

        source = "CLOUD"


    return {
        "question": question.question,
        "answer": answer,
        "source": source,
        "retrieval": "Moss",
        "results": results
    }