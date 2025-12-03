# backend/tools/rag_tools.py
from tools.tool_shim import tool
from sentence_transformers import SentenceTransformer
import chromadb, os
from chromadb.config import Settings
from dotenv import load_dotenv
import json

load_dotenv()
EMBED_MODEL = os.getenv("EMBED_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
CHROMA_DIR = os.getenv("CHROMA_DIR", "./backend/data/chroma")
os.makedirs(CHROMA_DIR, exist_ok=True)

_client = chromadb.PersistentClient(path=CHROMA_DIR, settings=Settings(allow_reset=True))
_coll = _client.get_or_create_collection("dept_docs")
_embed = SentenceTransformer(EMBED_MODEL)

def _embed_once(texts):  # helper
    return _embed.encode(texts, normalize_embeddings=True).tolist()

@tool("rag_upsert")
def rag_upsert(doc_id: str, text: str, meta_json: str = "{}") -> str:
    """
    Upsert a passage into Chroma. meta_json is a JSON string.
    """
    try:
        meta = json.loads(meta_json) if meta_json else {}
    except Exception:
        meta = {}
    _coll.upsert(ids=[doc_id], documents=[text], metadatas=[meta], embeddings=_embed_once([text]))
    return "OK"

@tool("rag_query")
def rag_query(query: str, k: int = 4) -> str:
    """
    Query top-k passages. Returns JSON lines: {'text','score','meta'} per line.
    """
    res = _coll.query(query_embeddings=_embed_once([query]), n_results=int(k), include=["documents","metadatas","distances"])
    docs, metas, dists = res["documents"][0], res["metadatas"][0], res["distances"][0]
    out = [{"text": t, "meta": m, "score": 1.0 - d} for t, m, d in zip(docs, metas, dists)]
    return "\n".join(json.dumps(x, ensure_ascii=False) for x in out)
