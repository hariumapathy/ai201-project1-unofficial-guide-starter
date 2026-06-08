import os
from dotenv import load_dotenv

load_dotenv()

# -- ingest_and_chunk --
DOCS_PATH = "documents"
RMP_PATH = os.path.join(DOCS_PATH, "Rate_My_Professor")

CHUNK_SIZE = 500
OVERLAP = 70
MIN_LENGTH = 50

# -- embed_and_retrieve_functions --
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
COLLECTION_NAME = "umass_cs_200_level_courses_guide"
CHROMA_PATH = "./chroma_db"

TOP_K_RESULTS = 5

# -- llm_response_generation --
GROQ_MODEL = "llama-3.3-70b-versatile"
