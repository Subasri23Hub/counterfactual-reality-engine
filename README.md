# 🚀 Counterfactual Reality Engine

An AI-powered system that simulates **alternate realities ("what-if" scenarios)** using structured reasoning and a **single optimized LLM call**.

---

## 🧠 What This Project Does

This application takes a hypothetical scenario like:

> *"What if chemistry didn’t exist?"*

…and generates a **complete structured analysis** including:

- 📍 Scenario interpretation  
- ⚡ Counterfactual change  
- 🏛️ Baseline reality  
- ⚡ Immediate impacts  
- 📈 Mid-term impacts  
- 🎯 Long-term impacts  
- 📋 Key assumptions  
- 🎯 Confidence level  
- 📊 Executive summary  

All in **one API call** → fast, efficient, production-ready.

---

## ⚙️ Architecture (FAANG-Level)


User Input → Prompt Builder → Gemini API (1 Call) → JSON Output → UI Rendering


### 🔥 Key Design Highlights

- ✅ **Single-call architecture** (cost-efficient & fast)
- ✅ **Structured JSON output parsing**
- ✅ **Retry handling for API limits**
- ✅ **Separation of concerns (modular design)**
- ✅ **Production-style UI with Streamlit**

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Google Gemini API**
- **Pydantic-style structured models**
- **Custom prompt engineering**

---

## 📁 Project Structure


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

## 🔑 Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/counterfactual-reality-engine.git
cd counterfactual-reality-engine
2️⃣ Create virtual environment
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Add your Gemini API Key

Create this file:

.streamlit/secrets.toml

Add:

gemini_api_key = "YOUR_API_KEY"
5️⃣ Run the app
streamlit run app/frontend/streamlit_app.py
⚠️ Known Issues

Free Gemini API tier has rate limits (429 errors)

If you see:

RESOURCE_EXHAUSTED

👉 Wait ~60 seconds OR upgrade API plan

💡 Example Input
What if electricity never existed?
🧪 Example Output

No electrical infrastructure

Slower technological advancement

Alternative energy evolution (mechanical, steam)

Reduced digital revolution impact

Lower global connectivity

🎯 Why This Project Stands Out

Not a basic chatbot ❌

Uses structured reasoning pipeline ✅

Optimized LLM usage (1-call design) ✅

Clean UI + production architecture ✅

Demonstrates real-world AI system design ✅

🚀 Future Improvements

Chat-style interface

Multi-scenario comparison

Visualization of impact timelines

Memory-based simulations

Offline fallback logic

👨‍💻 Author

Subasri B | Gen AI Intern @Sourcesys

⭐ If you like this project

Give it a ⭐ on GitHub — it helps a lot!
