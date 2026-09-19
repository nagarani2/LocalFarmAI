import json
import os
from pathlib import Path

from dotenv import load_dotenv
from moss import MossClient, QueryOptions, DocumentInfo

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / "file" / ".env")

MOSS_PROJECT_ID = os.getenv("MOSS_PROJECT_ID")
MOSS_PROJECT_KEY = os.getenv("MOSS_PROJECT_KEY")

INDEX_NAME = "localfarm-farming-knowledge-v2"

client = MossClient(
    MOSS_PROJECT_ID,
    MOSS_PROJECT_KEY
)


async def create_farming_index():
    data_path = Path(__file__).parent.parent / "data" / "farming_knowledge.json"

    with open(data_path, "r", encoding="utf-8") as file:
        documents = json.load(file)

    documents = [
        DocumentInfo(
            id=doc["id"],
            text=doc["text"]
        )
        for doc in documents
    ]

    await client.create_index(INDEX_NAME, documents)

    print("Farming knowledge index created successfully.")


async def load_farming_index():
    await client.load_index(INDEX_NAME)
    print("Farming knowledge index loaded.")


async def search_farming_knowledge(question: str):
    results = await client.query(
        INDEX_NAME,
        question,
        QueryOptions(top_k=3)
    )

    return [
        {
            "text": doc.text,
            "score": doc.score
        }
        for doc in results.docs
    ]