from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from typing import List, Dict
import numpy as np

client = QdrantClient(":memory:")

def init_collection():
    client.recreate_collection(
        collection_name="jobs",
        vectors_config=VectorParams(size=384, distance=Distance.COSINE),  # Assuming sentence-transformers
    )

def store_jobs(jobs: List[Dict]):
    points = []
    for job in jobs:
        # Simple embedding: in real, use sentence-transformers
        vector = np.random.rand(384).tolist()  # Mock vector
        point = PointStruct(
            id=job["id"],
            vector=vector,
            payload=job
        )
        points.append(point)
    client.upsert(collection_name="jobs", points=points)

def search_jobs(query: str, limit: int = 5) -> List[Dict]:
    # Mock vector for query
    query_vector = np.random.rand(384).tolist()
    results = client.search(
        collection_name="jobs",
        query_vector=query_vector,
        limit=limit
    )
    return [hit.payload for hit in results]
