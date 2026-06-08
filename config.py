import os

# -- ingest_and_chunk --
DOCS_PATH = "documents"
RMP_PATH = os.path.join(DOCS_PATH, "Rate_My_Professor")

CHUNK_SIZE = 500
OVERLAP = 70
MIN_LENGTH = 50