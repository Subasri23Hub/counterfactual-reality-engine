# Counterfactual Reality Engine

An AI-powered system that simulates alternate realities ("what-if" scenarios) using structured reasoning and a single optimized LLM call.

---

## Overview

This application takes a hypothetical scenario and generates a structured analysis including:

• Scenario interpretation  
• Counterfactual change  
• Baseline reality  
• Immediate impacts  
• Mid-term impacts  
• Long-term impacts  
• Key assumptions  
• Confidence level  
• Executive summary  

All outputs are generated in a single API call for efficiency, consistency, and performance.

---

## Architecture

User Input → Prompt Builder → LLM (Single Call) → Structured JSON → UI Rendering

### Design Highlights

• Single-call architecture for low latency and cost efficiency  
• Structured JSON output parsing  
• Retry handling for API rate limits  
• Modular and maintainable code structure  
• Clean and professional UI using Streamlit  

---

## Tech Stack

• Python  
• Streamlit  
• Google Gemini API  
• Structured data modeling  
• Prompt engineering  

---

## Project Structure


counterfactual-reality-engine/
│
├── app/
│ ├── frontend/
│ │ └── streamlit_app.py
│ │
│ ├── config.py
│ ├── models.py
│ ├── prompts.py
│ └── main.py
│
├── .streamlit/
│ └── secrets.toml
│
├── requirements.txt
├── README.md
└── .gitignore


---

## Setup Instructions

### 1. Clone the repository

git clone https://github.com/YOUR_USERNAME/counterfactual-reality-engine.git  
cd counterfactual-reality-engine

---

### 2. Create virtual environment

python -m venv .venv

Activate:

Windows:  
.venv\Scripts\activate  

Mac/Linux:  
source .venv/bin/activate  

---

### 3. Install dependencies

pip install -r requirements.txt

---

### 4. Add API Key

Create the file:

.streamlit/secrets.toml

Add:

gemini_api_key = "YOUR_API_KEY"

---

### 5. Run the application

streamlit run app/frontend/streamlit_app.py

---

## Known Issues

• Free Gemini API tier has strict rate limits  
• You may encounter 429 (RESOURCE_EXHAUSTED) errors  
• Wait before retrying or upgrade your API plan  

---

## Example Input

What if electricity never existed?

---

## Example Output (Summary)

• No electrical infrastructure  
• Slower technological development  
• Alternative energy systems may evolve  
• Reduced global connectivity  
• Limited digital transformation  

---

## Why This Project

• Demonstrates structured AI system design  
• Uses optimized single-call LLM architecture  
• Shows real-world prompt engineering  
• Clean separation of backend and UI  
• Suitable for production-level extension  

---

## Future Improvements

• Chat-based interface  
• Multi-scenario comparison  
• Timeline visualization  
• Memory-based simulations  
• Offline fallback handling  

---

## Author

Subasri B

---

## License

This project is intended for educational and portfolio use.
