import json
import os
import re
import sys
from typing import Any

import streamlit as st
from google import genai

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from app.config import generate_with_retry, get_settings
from app.models import SimulationResult
from app.prompts import build_master_counterfactual_prompt


st.set_page_config(page_title="Counterfactual Reality Engine", layout="wide")


@st.cache_resource
def get_client():
    settings = get_settings()
    client = genai.Client(api_key=settings["gemini_api_key"])
    return client, settings["gemini_model"]


def extract_json(raw_text: str) -> dict:
    raw_text = raw_text.strip()
    try:
        return json.loads(raw_text)
    except Exception:
        match = re.search(r"\{.*\}", raw_text, re.DOTALL)
        if match:
            return json.loads(match.group(0))
    raise ValueError("Invalid JSON response from model.")


def render_list(items):
    for item in items:
        st.markdown(f'<div class="mini-card">• {item}</div>', unsafe_allow_html=True)


def render_text(text):
    st.markdown(f'<div class="text-card">{text}</div>', unsafe_allow_html=True)


def render_confidence(conf):
    st.markdown(f'<div class="confidence">{conf}</div>', unsafe_allow_html=True)


st.markdown(
    """
<style>
.stApp {
    background: #f5f7fb;
}

.block-container {
    padding-top: 2.2rem !important;
    padding-bottom: 2.5rem !important;
    max-width: 1250px;
}

.hero-title {
    color: #111111;
    font-size: 2.9rem;
    font-weight: 800;
    margin-bottom: 0.45rem;
    letter-spacing: -0.02em;
}

.hero-subtitle {
    color: #374151;
    font-size: 1.08rem;
    margin-bottom: 2.3rem;
}

.section-wrap {
    margin-top: 1.8rem;
    margin-bottom: 1rem;
}

.section-title {
    color: #111111;
    font-size: 1.55rem;
    font-weight: 800;
    margin-bottom: 0.45rem;
}

.section-line {
    height: 1px;
    background: #d9e2f2;
    margin-bottom: 1.15rem;
}

div[data-testid="stTextArea"] textarea {
    background: #ffffff !important;
    color: #111111 !important;
    border-radius: 18px !important;
    border: 1px solid #dbe3f3 !important;
    min-height: 120px !important;
    font-size: 1rem !important;
    padding-top: 0.9rem !important;
}

.stButton > button {
    border-radius: 14px;
    background: #2563eb;
    color: white;
    font-weight: 700;
    height: 48px;
    padding: 0 1.2rem;
    border: none;
    box-shadow: 0 8px 18px rgba(37, 99, 235, 0.18);
    margin-top: 0.2rem;
    margin-bottom: 1.2rem;
}

.stButton > button:hover {
    background: #1d4ed8;
}

.text-card {
    background: white;
    padding: 1.1rem 1.15rem;
    border-radius: 16px;
    border: 1px solid #e3e8f2;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
    color: #111111;
    line-height: 1.75;
    margin-bottom: 0.5rem;
}

.mini-card {
    background: white;
    padding: 0.95rem 1rem;
    border-left: 4px solid #2563eb;
    border-radius: 14px;
    margin-bottom: 0.95rem;
    color: #111111;
    line-height: 1.65;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
}

.confidence {
    background: #fef3c7;
    padding: 1rem;
    border-radius: 14px;
    text-align: center;
    font-weight: 800;
    color: #111111;
    border: 1px solid #f59e0b;
    min-height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.results-top-gap {
    margin-top: 1.6rem;
}

@media (max-width: 900px) {
    .hero-title {
        font-size: 2.2rem;
    }

    .section-title {
        font-size: 1.35rem;
    }
}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown('<div class="hero-title">Counterfactual Reality Engine</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-subtitle">Analyze alternate realities with one clean, structured AI call.</div>',
    unsafe_allow_html=True,
)

st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
st.markdown('<div class="section-title"> Scenario Input</div>', unsafe_allow_html=True)
st.markdown('<div class="section-line"></div>', unsafe_allow_html=True)

user_input = st.text_area("", placeholder="What if chemistry didn’t exist?", key="input")
run = st.button("Run Simulation!")
st.markdown('</div>', unsafe_allow_html=True)

if run:
    if not user_input.strip():
        st.error("Enter a scenario.")
    else:
        try:
            client, model = get_client()
            prompt = build_master_counterfactual_prompt(user_input)

            with st.spinner("Running simulation..."):
                output = generate_with_retry(client, model, prompt)
                data = extract_json(output)
                result = SimulationResult.from_dict(data)

            st.markdown('<div class="results-top-gap"></div>', unsafe_allow_html=True)

            c1, c2 = st.columns(2, gap="large")

            with c1:
                st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
                st.markdown('<div class="section-title">📍 Scenario</div>', unsafe_allow_html=True)
                st.markdown('<div class="section-line"></div>', unsafe_allow_html=True)
                render_text(result.scenario)
                st.markdown('</div>', unsafe_allow_html=True)

            with c2:
                st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
                st.markdown('<div class="section-title">⚡ Counterfactual Change</div>', unsafe_allow_html=True)
                st.markdown('<div class="section-line"></div>', unsafe_allow_html=True)
                render_text(result.counterfactual_change)
                st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">🏛️ Baseline</div>', unsafe_allow_html=True)
            st.markdown('<div class="section-line"></div>', unsafe_allow_html=True)
            render_text(result.baseline)
            st.markdown('</div>', unsafe_allow_html=True)

            c1, c2, c3 = st.columns(3, gap="large")

            with c1:
                st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
                st.markdown('<div class="section-title">⚡ Immediate</div>', unsafe_allow_html=True)
                st.markdown('<div class="section-line"></div>', unsafe_allow_html=True)
                render_list(result.immediate_impacts)
                st.markdown('</div>', unsafe_allow_html=True)

            with c2:
                st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
                st.markdown('<div class="section-title">📈 Mid-Term</div>', unsafe_allow_html=True)
                st.markdown('<div class="section-line"></div>', unsafe_allow_html=True)
                render_list(result.mid_term_impacts)
                st.markdown('</div>', unsafe_allow_html=True)

            with c3:
                st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
                st.markdown('<div class="section-title">🎯 Long-Term</div>', unsafe_allow_html=True)
                st.markdown('<div class="section-line"></div>', unsafe_allow_html=True)
                render_list(result.long_term_impacts)
                st.markdown('</div>', unsafe_allow_html=True)

            c1, c2 = st.columns([2, 1], gap="large")

            with c1:
                st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
                st.markdown('<div class="section-title">📋 Assumptions</div>', unsafe_allow_html=True)
                st.markdown('<div class="section-line"></div>', unsafe_allow_html=True)
                render_list(result.assumptions)
                st.markdown('</div>', unsafe_allow_html=True)

            with c2:
                st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
                st.markdown('<div class="section-title">🎯 Confidence</div>', unsafe_allow_html=True)
                st.markdown('<div class="section-line"></div>', unsafe_allow_html=True)
                render_confidence(result.confidence)
                st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">📊 Summary</div>', unsafe_allow_html=True)
            st.markdown('<div class="section-line"></div>', unsafe_allow_html=True)
            render_text(result.executive_summary)
            st.markdown('</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(str(e))