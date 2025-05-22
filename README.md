# 🧠 Personal Research Assistant

An interactive AI-powered research assistant built with **Streamlit**, **LangChain**, and **Claude 3.5 (Anthropic)**. This tool allows you to input any research question and get a structured, source-backed summary with the ability to download the result as a `.txt` report.

---

## 🚀 Features

- 🔍 Accepts natural language research queries
- 🤖 Uses Claude 3.5 via LangChain for generating structured research summaries
- 🛠️ Dynamically invokes tools like:
  - DuckDuckGo search
  - Wikipedia scraping
  - Save/record tool
- 📋 Displays topic, summary, sources, and tools used
- 📄 Allows downloading results as a plain text report

---

## 📦 Tech Stack

- Python 3.11+
- Streamlit
- LangChain (OpenAI + Anthropic)
- Claude 3.5 via `langchain-anthropic`
- DuckDuckGo search tool
- Wikipedia tool
- Pydantic for schema parsing
- `.env` for secure API key management

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yaswanthkalyan/Personal_Research_Assistant.git
cd Personal_Research_Assistant
````

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: .\venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API keys to `.env`

Create a `.env` file in the root directory:

```env
ANTHROPIC_API_KEY=your_anthropic_key_here
OPENAI_API_KEY=your_openai_key_if_used
```

---

## ▶️ Run the App

```bash
streamlit run streamlit_app.py
```

Open your browser and go to: [http://localhost:8501](http://localhost:8501)

---

## 🧪 Example Output

```text
📌 Topic:
How AI is transforming clinical diagnostics

🧠 Summary:
AI is increasingly being applied in clinical diagnostics, particularly in radiology and pathology...

📚 Sources:
- https://en.wikipedia.org/wiki/Artificial_intelligence_in_healthcare
- https://duckduckgo.com/...

🛠️ Tools Used:
search_tool, wiki_tool
```

---

## 📁 Project Structure

```
.
├── tools.py                # Custom tools for search/wiki/save
├── streamlit_app.py        # Main Streamlit interface
├── requirements.txt        # All dependencies
├── .env                    # API keys (not tracked in Git)
├── .gitignore              # Excludes .env, __pycache__, venv, etc.
└── README.md               # You are here
```

---

## 🛡️ License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Author

[Yaswanth Kalyan Ponugoti](https://github.com/yaswanthkalyan)

---

> ⭐ Star this repo if you find it useful — PRs and feedback welcome!

