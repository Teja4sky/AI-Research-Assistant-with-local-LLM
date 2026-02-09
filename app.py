import streamlit as st
import ollama
import wikipedia
import arxiv
import fitz

# -------------------------
# PAGE CONFIG
# -------------------------

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="wide"
)

# -------------------------
# HIDE STREAMLIT HEADER
# -------------------------

st.markdown("""
<style>

header {visibility:hidden;}
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}

.block-container {
    padding-top: 0rem;
}

/* Premium loading rectangle */

.loading-container {

    width: 100%;
    height: 12px;
    background: rgba(0,255,156,0.1);
    border-radius: 10px;
    overflow: hidden;
    margin-top: 15px;
}

.loading-bar {

    width: 40%;
    height: 100%;
    background: linear-gradient(
        90deg,
        #00ff9c,
        #00ffaa,
        #00ffcc,
        #00ffaa,
        #00ff9c
    );

    border-radius: 10px;

    animation: loading-animation 1.2s infinite;
}

@keyframes loading-animation {

    0% { transform: translateX(-100%); }

    100% { transform: translateX(300%); }

}

/* Question box */

.question-box {

    background: rgba(0,255,156,0.08);
    padding: 15px;
    border-radius: 12px;
    margin-top: 15px;
}

/* Answer box */

.answer-box {

    background: rgba(0,255,156,0.05);
    padding: 20px;
    border-radius: 12px;
    margin-top: 10px;
}

/* Highlight important words */

.highlight {
    color: yellow;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# SESSION STATE
# -------------------------

if "answer" not in st.session_state:
    st.session_state.answer = ""

if "question" not in st.session_state:
    st.session_state.question = ""

if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = ""

# -------------------------
# FAST PDF READER
# -------------------------

def read_pdf(file):

    doc = fitz.open(stream=file.read(), filetype="pdf")

    text = ""

    for page in doc[:2]:
        text += page.get_text()

    return text[:1000]

# -------------------------
# SEARCH FUNCTIONS
# -------------------------

def wiki_search(q):
    try:
        return wikipedia.summary(q, sentences=3)
    except:
        return ""

def arxiv_search(q):
    try:
        search = arxiv.Search(query=q, max_results=1)
        for r in search.results():
            return r.summary[:500]
    except:
        return ""
    return ""

# -------------------------
# AI RESPONSE WITH SEMANTIC HIGHLIGHT
# -------------------------

def ask_llama_semantic(q, pdf):

    wiki = wiki_search(q)
    arxiv_data = arxiv_search(q)

    prompt = f"""
Explain clearly.

Highlight important technical concepts using:

<span class="highlight">important term</span>

Question:
{q}

Document:
{pdf}

Wiki:
{wiki}

Arxiv:
{arxiv_data}
"""

    res = ollama.chat(
        model="llama3.1:8b",
        messages=[{"role":"user","content":prompt}],
        options={"num_predict":500}
    )

    return res["message"]["content"]

# -------------------------
# UI
# -------------------------

st.title("AI Research Assistant")

pdf = st.file_uploader("Upload Document")

if pdf:
    st.session_state.pdf_text = read_pdf(pdf)

question = st.text_input("Enter Question")

# Loading placeholder
loading_placeholder = st.empty()

if st.button("Research"):

    st.session_state.question = question
    st.session_state.answer = ""

    # Show premium loading rectangle
    loading_placeholder.markdown("""
    <div class="loading-container">
        <div class="loading-bar"></div>
    </div>
    """, unsafe_allow_html=True)

    # Get AI answer
    answer = ask_llama_semantic(
        question,
        st.session_state.pdf_text
    )

    st.session_state.answer = answer

    # Remove loading animation
    loading_placeholder.empty()

# -------------------------
# DISPLAY OUTPUT
# -------------------------

if st.session_state.answer:

    st.markdown(
        f'<div class="question-box"><b>Question:</b> {st.session_state.question}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="answer-box">{st.session_state.answer}</div>',
        unsafe_allow_html=True
    )
