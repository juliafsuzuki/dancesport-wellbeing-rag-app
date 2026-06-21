# wellbeing-coach-rag-app

DanceSport Competition Prep Wellbeing Coach RAG.

A single-source RAG application that helps DanceSport athletes prepare for competitions and optimize performance readiness, grounded in *Dance To Your Maximum* by Maximiliaan Winkelhuis.

## Stack

- **Orchestration:** LangChain + LangGraph + LangSmith
- **LLM:** OpenAI `gpt-4.1-mini` (routing/judge temp=0, generation temp=0.1)
- **Embeddings:** OpenAI `text-embedding-3-small` (dim=1536)
- **Vector store:** Pinecone Serverless — index `wellbeing-coach-rag`, cosine, AWS `us-east-1`
- **PDF + OCR:** PyMuPDF (fitz) + Tesseract (pytesseract)
- **UI:** Streamlit (`app.py`)
- **Notebook:** `1_wellbeing_coach__rag_app_langchain.ipynb`
- **LangSmith project:** `wellbeing-coach-rag-app-langchain`

## Documentation

- [Functional & Technical Specification](docs/specification.md) — Authoritative spec: user stories, UI categories, RAG graph, routing, metadata schema, evaluation, constraints.
- [Project Design](docs/project_design.md) — Architecture, chunking, retrieval, and evaluation decisions.
- [Memory Index](docs/MEMORY.md) — Index of design and reference docs.
- [Repo Reference](docs/reference_github.md) — Canonical repository URL.

## Repository layout

```
wellbeing-coach-rag-app/
├── app.py                          # Streamlit chat UI
├── rag_chain.py                    # RAG graph, router, retriever, generator
├── 1_wellbeing_coach__rag_app_langchain.ipynb  # End-to-end pipeline + evaluation
├── data/
│   ├── e-Book_dance-to-your-maximum.pdf        # Source corpus (316 pages, image-based)
│   └── ocr_cache.json                          # OCR output cache (run-once)
├── images/                         # Diagram PNGs displayed in notebook
├── generate_diagrams.py            # Diagram generation utility
└── .venv/                          # Python virtual environment
```

## Getting started

1. Create a virtual environment: `python -m venv .venv`
2. Activate it and install dependencies.
3. Populate `.env` with `OPENAI_API_KEY`, `PINECONE_API_KEY`, and `LANGCHAIN_API_KEY`.
4. Run the notebook to ingest the PDF and build the Pinecone index.
5. Launch the UI: `streamlit run app.py`

## Evaluation

15-question fixed test set with an LLM judge (`gpt-4.1-mini`, temp=0) plus manual spot-check. Target: ≥90% faithfulness (claims fully supported by retrieved context). PASS/FAIL is printed in-notebook. See [docs/specification.md §3.10](docs/specification.md) for details.

## Constraints

- Single corpus (no multi-document upload)
- No cross-session memory (chat history clears on reload)
- No re-ranking, no streaming
- Local `.env` for secrets; single-process Streamlit deployment

See [docs/specification.md §4](docs/specification.md) for the full list.
