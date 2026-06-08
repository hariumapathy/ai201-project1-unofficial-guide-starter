# AI Use Attribution: Use Claude to generate the Python code, followed up with manual edits

from groq import Groq
from config import GROQ_MODEL

_client = Groq()

SYSTEM_PROMPT = """You are the unofficial UMass CS Course guide, with emphasis on the 200-level courses: CS/CICS 210, 220, 230, 240, and 250. You are best at answering real student questions about these courses, the professors that teach them, and the characteristics, positives, and negatives of these professors and the courses themselves. Your job is to answer user questions using ONLY the given chunks from student reviews and/or course pages and descriptions. If a user's question cannot be answered with the given chunks, tell the user that there doesn't seem to be relevant information for their question, and ask them to be more specific or provide further detail (in these cases, citations are not needed). Do not provide answers outside the scope of the given chunks. When answering, indicate the file name your answer is based on in parentheses in the form "(source: <filename>)", similar in usage to an MLA in-text citation. Don't include chunk numbers, however."""


# ---------------------------------------------------------------------------
# Context builder
# ---------------------------------------------------------------------------

def _build_chunk_string(retrieved_chunks):
    """
    Combine retrieved chunks into a single context string to be included
    in the user message. Each chunk is labelled with its index, source
    filename, distance score, and text.
    """
    lines = []
    for i, chunk in enumerate(retrieved_chunks):
        lines.append(
            f"-- CHUNK #{i + 1} --\n"
            f"Source: {chunk['filename']}\n"
            f"Distance score (lower = more relevant): {chunk['distance']:.4f}\n"
            f"Text: {chunk['text']}"
        )
    return "\n\n".join(lines)


# ---------------------------------------------------------------------------
# Generation
# ---------------------------------------------------------------------------

def generate_response(query, retrieved_chunks):
    """
    Generate a grounded response to the user's query using the retrieved chunks.

    The chunks are formatted into a context block and included in the user
    message alongside the query. The system prompt instructs the LLM to
    answer only from the provided context.

    Returns the LLM's response as a string.
    """
    total_chunk_string = _build_chunk_string(retrieved_chunks)

    user_message = (
        f"Retrieved Chunks:\n\n"
        f"{total_chunk_string}\n\n"
        f"Question: {query}"
    )

    response = _client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
    )

    return response.choices[0].message.content


# ---------------------------------------------------------------------------
# FOR TESTING - Check LLM generated response for a test query
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    from ingest_and_chunk import load_documents, chunk_documents
    from embed_and_retrieve_functions import embed_and_store, retrieve

    docs = load_documents()
    chunks = chunk_documents(docs)
    embed_and_store(chunks)

    test_query = "What do students say about Jaime's lecturing style?"
    retrieved = retrieve(test_query)

    print(f"\nQUERY: {test_query}\n")

    print("\n--- LLM Response ---\n")
    response = generate_response(test_query, retrieved)
    print(response)