# AI Use Attribution: Use Claude to generate the Python code, followed up with manual edits
# Used Tinker/Lab 1 Code as a reference, due to the use of chromaDB

import chromadb
from chromadb.utils import embedding_functions
from config import COLLECTION_NAME, CHROMA_PATH, EMBEDDING_MODEL, TOP_K_RESULTS

_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=EMBEDDING_MODEL
)
_client = chromadb.PersistentClient(path=CHROMA_PATH)
_collection = _client.get_or_create_collection(
    name=COLLECTION_NAME,
    embedding_function=_ef,
    metadata={"hnsw:space": "cosine"},
)

def embed_and_store(chunks):
    """
    Embed a list of chunks and store them in the vector database.

    _collection.add() takes three parallel lists built from the chunks:
      - documents : raw text strings — the embedding function converts
                    these to vectors automatically via sentence-transformers
      - metadatas : one dict per chunk, storing the source filename
      - ids       : unique chunk_id strings to identify each entry
    """
    if _collection.count() > 0:
        print(f"Collection '{COLLECTION_NAME}' already contains {_collection.count()} entries. Skipping embedding.")
        return

    _collection.add(
        documents=[c["text"] for c in chunks],
        metadatas=[{"filename": c["filename"]} for c in chunks],
        ids=[c["chunk_id"] for c in chunks],
    )
    print(f"Stored {_collection.count()} total chunks in the vector database.")


def retrieve(query, n_results=TOP_K_RESULTS):
    """
    Find the most relevant chunks for a user's query.

    Uses _collection.query() to run a semantic search. Returns a list of
    dicts, each with:
      - "text"     : the chunk text
      - "filename" : the source document filename
      - "distance" : the cosine distance score (lower = more similar)
    """
    if _collection.count() == 0:
        return []

    results = _collection.query(
        query_texts=[query],
        n_results=n_results,
        include=["documents", "metadatas", "distances"],
    )

    retrieved = []
    for text, metadata, distance in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0],
    ):
        retrieved.append({
            "text": text,
            "filename": metadata["filename"],
            "distance": distance,
        })

    

    return retrieved


# ---------------------------------------------------------------------------
# FOR TESTING: Inspect Retrieved Chunks for a Sample Query
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    from ingest_and_chunk import load_documents, chunk_documents

    docs = load_documents()
    chunks = chunk_documents(docs)
    embed_and_store(chunks)

    print("\n--- Test retrieval ---\n")
    test_query = "What do students say about Jaime Davila's lecturing style?"
    results = retrieve(test_query)

    print(f"QUERY: {test_query}\n")
    for r in results:
        print(f"[dist: {r['distance']:.3f}] (source: {r['filename']}) {r['text']}")