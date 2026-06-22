import streamlit as st
from rag_chain import ask

st.set_page_config(
    page_title="DanceSport Wellbeing Coach",
    page_icon="💃",
    layout="centered",
)

st.title("💃 DanceSport Wellbeing Coach")
st.caption("Grounded in *Dance To Your Maximum* — Maximiliaan Winkelhuis")
st.markdown(
    "Ask me anything about showcase or competition preparation. "
    "I'll answer using the coaching materials in my knowledge base and "
    "cite the exact passage and page number for every response."
)

CATEGORIES = {
    "🎯 Performance Readiness": [
        "How do I know if I am ready to perform my showcase?",
        "What should I focus on during the final weeks before my showcase?",
        "How can I reduce mistakes during my performance?",
        "What should I do if I forget part of my routine on the floor?",
    ],
    "📋 Practice & Preparation": [
        "What is the best way to practice my showcase routine?",
        "How often should I practice between lessons?",
        "How do I remember my showcase routine more effectively?",
        "How can I make my practice sessions more productive?",
        "How do I transition from learning choreography to performing it?",
    ],
    "🎵 Musicality & Timing": [
        "How can I improve my timing with the music?",
        "How do I stay on time when I get nervous?",
        "How can I better connect my movements to the music?",
        "How important is breathing for timing, movement, and performance quality?",
    ],
    "✨ Confidence & Stage Presence": [
        "How can I look more confident on the dance floor?",
        "How do I manage performance anxiety or stage fright?",
        "How can I project confidence even when I feel nervous?",
        "How can I make a strong first impression when I enter the floor?",
    ],
    "💃 Expression & Storytelling": [
        "How can I make my performance more expressive?",
        "How can I better tell the story of the dance?",
        "How do I connect emotionally with the music and my audience?",
        "What makes a showcase performance memorable?",
    ],
    "🧠 Mindset & Mental Performance": [
        "Why is mental clarity important in DanceSport?",
        "How can I stay mentally focused during my performance?",
        "How do I recover mentally after making a mistake?",
        "How can visualization improve my showcase performance?",
    ],
}

if "messages" not in st.session_state:
    st.session_state.messages = []
if "pending_question" not in st.session_state:
    st.session_state.pending_question = None

# ── Categorised example questions ────────────────────────────────────────────
st.divider()
st.markdown("##### Ask me anything — or pick a question below to get started:")

categories = list(CATEGORIES.items())
col1, col2 = st.columns(2)

for i, (category, questions) in enumerate(categories):
    col = col1 if i < 3 else col2
    with col:
        st.markdown(f"**{category}**")
        for j, q in enumerate(questions):
            if st.button(q, key=f"q_{i}_{j}", use_container_width=True):
                st.session_state.pending_question = q
        st.write("")  # breathing room between categories

st.divider()

# ── Chat history ──────────────────────────────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ── Resolve prompt ────────────────────────────────────────────────────────────
prompt = None
if st.session_state.pending_question:
    prompt = st.session_state.pending_question
    st.session_state.pending_question = None

user_input = st.chat_input("Ask your question…")
if user_input:
    prompt = user_input

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Retrieving from knowledge base…"):
            response = ask(prompt)
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()
