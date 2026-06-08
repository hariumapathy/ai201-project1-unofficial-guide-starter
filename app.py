# Gradio UI and end-to-end functions
# Used provided Gradio code in Project as template
# AI Use Attribution: Used Claude to modify the Gradio UI styling and add visual elements

import gradio as gr
from ingest_and_chunk import load_documents, chunk_documents
from embed_and_retrieve_functions import embed_and_store, retrieve
from llm_response_generation import generate_response

# -- end-to-end functions --
def run_pipeline_startup():
    '''Couples together the functions for ingesting, chunking, embedding, and storing the documents'''
    docs = load_documents()
    chunks = chunk_documents(docs)
    embed_and_store(chunks)


def chat(query) -> str:
    '''Takes in a user's question, retrieves relevant chunks, and returns the LLM-generated response'''
    if not query.strip():
        return ""
    retrieved_chunks = retrieve(query)
    llm_response = generate_response(query, retrieved_chunks)
    return llm_response


# -- Gradio UI and Styling --
theme = gr.themes.Default(
    primary_hue="blue",
    secondary_hue="slate",
    neutral_hue="slate",
    font=gr.themes.GoogleFont("IBM Plex Sans"),
)

with gr.Blocks(title="UMass CS Unofficial Course Guide", theme=theme, css="""
    .header-box {
        text-align: center;
        padding: 2rem 1rem 1rem 1rem;
    }
    .header-box h1 {
        font-size: 2rem;
        font-weight: 700;
        color: #881c1c;
        margin-bottom: 0.4rem;
    }
    .header-box p {
        font-size: 1rem;
        color: #555;
        margin: 0;
    }
""") as demo:

    gr.HTML("""
        <div class="header-box">
            <h1>🎓 UMass Unofficial CS Course Guide</h1>
            <p>Get your questions answered about common undergraduate CS courses and professors!</p>
        </div>
    """)

    inp = gr.Textbox(
        label="Your Question",
        placeholder="e.g. What do students say about Jaime Davila's teaching style?",
        lines=2,
    )
    btn = gr.Button("Ask", variant="primary")
    answer = gr.Textbox(label="Answer", lines=10)

    btn.click(chat, inputs=inp, outputs=[answer])
    inp.submit(chat, inputs=inp, outputs=[answer])

if __name__ == "__main__":
    run_pipeline_startup()
    demo.launch()