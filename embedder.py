import google.generativeai as genai
from dotenv import load_dotenv
import os
from typing import List

# Load environment variables from .env file
load_dotenv()   
# Initialize OpenAI client
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
EMBEDDING_MODEL = "models/embedding-001"  #Gemini embedding model


def embed_chunks(chunks: List[str]) -> List[List[float]]:
    
    embeddings = []
    for chunk in chunks:
        response = genai.embed_content(
            content=chunk,
            model=EMBEDDING_MODEL,
            task_type="retrieval_document"
        )
        embeddings.append(response["embedding"])
    return embeddings


def embed_User_query(query: str) -> List[float]:
    response = genai.embed_content(
        model=EMBEDDING_MODEL,
        content=query,
        task_type="retrieval_query"
    )
    return response["embedding"]