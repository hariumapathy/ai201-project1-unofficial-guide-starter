# AI Use Attribution: Use Claude to generate the Python code, followed up with manual edits

import os
import re

from config import DOCS_PATH, RMP_PATH, CHUNK_SIZE, OVERLAP, MIN_LENGTH

# ---------------------------------------------------------------------------
# Ingestion
# ---------------------------------------------------------------------------

def load_documents():
    """
    Load all .txt files from documents/ and documents/Rate_My_Professor/.
    Returns a list of dicts with keys:
      - "text"     : raw file contents
      - "filename" : the filename
      - "is_rmp"   : True if the file came from the Rate_My_Professor subfolder
    """
    documents = []

    # Load Rate My Professor files
    for filename in sorted(os.listdir(RMP_PATH)):
        if filename.endswith(".txt"):
            filepath = os.path.join(RMP_PATH, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
            documents.append({
                "text": text,
                "filename": filename,
                "is_rmp": True,
            })

    # Load all other docs directly in documents/
    for filename in sorted(os.listdir(DOCS_PATH)):
        if filename.endswith(".txt"):
            filepath = os.path.join(DOCS_PATH, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
            documents.append({
                "text": text,
                "filename": filename,
                "is_rmp": False,
            })

    print(f"Loaded {len(documents)} document(s).")

    return documents


# ---------------------------------------------------------------------------
# Chunking helpers
# ---------------------------------------------------------------------------

def _extract_professor_name(text):
    """
    Pull the professor name from the metadata header at the top of an RMP file.
    Looks for a line like: Professor: David Barrington
    Returns the name as a string, or '' if not found.
    """
    match = re.search(r"Professor:\s*(.+)", text)
    if match:
        return match.group(1).strip()
    return ""


def _chunk_rmp(doc):
    """
    Chunk a Rate My Professor document by splitting on review boundaries.
    Each chunk is one complete review, prefixed with the professor's name.
    Returns a list of chunk dicts.
    """
    text = doc["text"]
    filename = doc["filename"]
    professor_name = _extract_professor_name(text)

    # Use a prefix for chunk IDs derived from the filename
    prefix = filename.replace(".txt", "").lower()

    chunks = []
    counter = 0

    # Split on the review markers; keep the content between START and END
    review_blocks = re.findall(
        r"-- REVIEW START --(.+?)-- REVIEW END --",
        text,
        flags=re.DOTALL,
    )

    for block in review_blocks:
        review_text = block.strip()

        # Prepend professor name
        chunk_text = f"Professor: {professor_name}\n{review_text}"

        chunks.append({
            "text": chunk_text,
            "filename": filename,
            "chunk_id": f"{prefix}_{counter}",
        })
        counter += 1

    return chunks


def _chunk_fixed_size(doc):
    """
    Chunk a non-RMP document using fixed-size character sliding window with overlap.
    Chunk size: 500 characters. Overlap: 70 characters. Min Length: 50 characters.
    Returns a list of chunk dicts.
    """
    text = doc["text"]
    filename = doc["filename"]
    prefix = filename.replace(".txt", "").lower()

    chunks = []
    counter = 0
    start = 0

    while start < len(text):
        end = start + CHUNK_SIZE
        chunk_text = text[start:end].strip()

        if len(chunk_text) >= MIN_LENGTH:
            chunks.append({
                "text": chunk_text,
                "filename": filename,
                "chunk_id": f"{prefix}_{counter}",
            })
            counter += 1

        start += CHUNK_SIZE - OVERLAP

    return chunks


# ---------------------------------------------------------------------------
# Main chunking entry point
# ---------------------------------------------------------------------------

def chunk_documents(documents):
    """
    Route each document to the correct chunking strategy based on is_rmp.
    Returns a flat list of all chunk dicts across all documents.
    """
    all_chunks = []

    for doc in documents:
        # a Rate My Professor doc (chunk by review)
        if doc["is_rmp"]:
            chunks = _chunk_rmp(doc)
        # all other docs (fixed size chunking)
        else:
            chunks = _chunk_fixed_size(doc)

        all_chunks.extend(chunks)

    print(f"Produced {len(all_chunks)} chunk(s) total.")
    return all_chunks


# ---------------------------------------------------------------------------
# FOR TESTING: Chunk Inspection (Write to File for Review)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    docs = load_documents()
    chunks = chunk_documents(docs)

    with open("chunks_output.txt", "w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(f"[{chunk['chunk_id']}] (source: {chunk['filename']})\n")
            f.write(chunk["text"])
            f.write("\n---\n\n")

    print(f"Written {len(chunks)} chunks to chunks_output.txt")