# wellbeing-coach-rag-app

DanceSport Competition Prep Wellbeing Coach RAG.

A single-source RAG application that helps DanceSport athletes prepare for competitions and optimize performance readiness, grounded in *Dance To Your Maximum* by Maximiliaan Winkelhuis. Every answer is cited inline with chapter and page numbers.

![DanceSport Wellbeing Coach home page](images/home_page.jpg)

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

## Home page — question categories

The home page surfaces 6 pre-built categories with clickable example questions, arranged in a two-column grid (see [`images/home_page.jpg`](images/home_page.jpg)).

**🎯 Performance Readiness**
- How do I know if I am ready to perform my showcase?
- What should I focus on during the final weeks before my showcase?
- How can I reduce mistakes during my performance?
- What should I do if I forget part of my routine on the floor?

**📋 Practice & Preparation**
- What is the best way to practice my showcase routine?
- How often should I practice between lessons?
- How do I remember my showcase routine more effectively?
- How can I make my practice sessions more productive?
- How do I transition from learning choreography to performing it?

**🎵 Musicality & Timing**
- How can I improve my timing with the music?
- How do I stay on time when I get nervous?
- How can I better connect my movements to the music?
- How important is breathing for timing, movement, and performance quality?

**✨ Confidence & Stage Presence**
- How can I look more confident on the dance floor?
- How do I manage performance anxiety or stage fright?
- How can I project confidence even when I feel nervous?
- How can I make a strong first impression when I enter the floor?

**💃 Expression & Storytelling**
- How can I make my performance more expressive?
- How can I better tell the story of the dance?
- How do I connect emotionally with the music and my audience?
- What makes a showcase performance memorable?

**🧠 Mindset & Mental Performance**
- Why is mental clarity important in DanceSport?
- How can I stay mentally focused during my performance?
- How do I recover mentally after making a mistake?
- How can visualization improve my showcase performance?

Users can also type a free-text question in the persistent chat input at the bottom.

## Answer format

Every claim is tagged and cited:

- **Epistemic tags:** `[KNOWN]`, `[INFERRED]`, `[COMPUTED]`, `[COMMON]`, `[FRAME]`, `[GUESS]`
- **Confidence:** HIGH (≥80%) · MED (50–80%) · LOW (20–50%) · VERY LOW (<20%) · UNKNOWN
- **Citation:** `[Dance To Your Maximum, Chapter X-Y, pp. Z–W]`
- **Refusal:** When no relevant context is retrieved, the answer begins with `"I don't have that in my knowledge base."` — no fabrication.

## Repository layout

```
wellbeing-coach-rag-app/
├── app.py                          # Streamlit chat UI
├── rag_chain.py                    # RAG graph, router, retriever, generator
├── 1_wellbeing_coach__rag_app_langchain.ipynb  # End-to-end pipeline + evaluation
├── data/
│   ├── e-Book_dance-to-your-maximum.pdf        # Source corpus (316 pages, image-based)
│   └── ocr_cache.json                          # OCR output cache (run-once)
├── images/
│   └── home_page.jpg                           # Home page screenshot
├── docs/
│   ├── specification.md                        # Functional & technical specification
│   ├── project_design.md                       # Architecture & design decisions
│   ├── MEMORY.md                               # Memory index
│   └── reference_github.md                     # Repo reference
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
