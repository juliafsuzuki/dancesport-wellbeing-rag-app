# wellbeing-coach-rag-app

DanceSport Competition Prep Wellbeing Coach RAG.

A single-source RAG application that helps DanceSport athletes prepare for competitions and optimize performance readiness, grounded in *Dance To Your Maximum* by Maximiliaan Winkelhuis.

## Stack

- **Orchestration:** LangChain + LangGraph + LangSmith
- **LLM:** OpenAI `gpt-4.1-mini`
- **Embeddings:** OpenAI `text-embedding-3-small` (dim=1536)
- **Vector store:** Pinecone (serverless, cosine similarity)
- **UI:** Streamlit (`app.py`)
- **Notebook:** `1_wellbeing_coach__rag_app_langchain.ipynb`
- **LangSmith project:** `wellbeing-coach-rag-app-langchain`

## Documentation

- [Project Design](docs/project_design.md) — Full architecture, ingestion, chunking, retrieval, routing, citations, and evaluation decisions.
- [Memory Index](docs/MEMORY.md) — Index of design and reference docs.
- [Repo Reference](docs/reference_github.md) — Canonical repository URL.

## Getting started

1. Create a virtual environment: `python -m venv .venv`
2. Activate it and install dependencies.
3. Populate `.env` with `OPENAI_API_KEY`, `PINECONE_API_KEY`, and `LANGCHAIN_API_KEY`.
4. Run the notebook to ingest the PDF and build the Pinecone index.
5. Launch the UI: `streamlit run app.py`

## Evaluation

15-question fixed test set with an LLM judge plus manual spot-check. Target: ≥90% faithfulness (claims fully supported by retrieved context). See [docs/project_design.md](docs/project_design.md) for details.
