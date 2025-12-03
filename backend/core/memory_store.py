# backend/core/memory_store.py
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
import os

EMBED_MODEL = os.getenv("EMBED_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
CHROMA_DIR = os.getenv("CHROMA_DIR", "./backend/data/chroma")

os.makedirs(CHROMA_DIR, exist_ok=True)

client = chromadb.PersistentClient(
    path=CHROMA_DIR, settings=Settings(allow_reset=True)
)

embedder = SentenceTransformer(EMBED_MODEL)

def embed_texts(texts):
    return embedder.encode(texts, normalize_embeddings=True).tolist()

def get_collection(name="dept_docs"):
    return client.get_or_create_collection(name=name)
