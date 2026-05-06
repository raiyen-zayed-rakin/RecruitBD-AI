import json

import numpy as np
from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from sentence_transformers import SentenceTransformer
import torch

from core.config import INDEX_DIR

from .routes import router

EMB_PATH = INDEX_DIR / "job_index_embeddings.npy"
META_PATH = INDEX_DIR / "job_index_metadata.json"


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup routine to load the SBERT model and job index into memory."""
    print("⚙️  Loading SBERT model…")

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"⚙️  Using device: {device}")

    app.state.model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2", device=device)

    print(f"⚙️  Loading job index from {INDEX_DIR}…")
    app.state.job_embeddings = np.load(EMB_PATH, mmap_mode="r")
    with open(META_PATH, "r", encoding="utf-8") as f:
        app.state.job_metadata = json.load(f)

    print(f"✅  Ready — {len(app.state.job_metadata):,} jobs indexed.")
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
