# 📄 GenAI RAG Chat Application (Streamlit)

## 🚀 Overview

This project is a **Streamlit-based GenAI application** that allows users to upload a PDF and ask questions about its content using a **Retrieval-Augmented Generation (RAG)** pipeline.

The system retrieves relevant document chunks and generates **grounded, context-aware responses** using a Large Language Model (LLM).

---

## 🎯 Features

* 📂 Upload PDF documents
* 🔍 Semantic search using vector embeddings (FAISS)
* 🤖 LLM-powered question answering
* 🧠 Context-aware responses (RAG)
* 💬 Chat interface with session memory

---

## 🧠 Architecture

User Query → Embeddings → Vector DB (FAISS) → Relevant Chunks → LLM → Response

---

## 🛠️ Tech Stack

* **Frontend/UI**: Streamlit
* **LLM Integration**: OpenAI / Enterprise LLM Endpoint
* **RAG Framework**: LangChain
* **Vector Store**: FAISS
* **PDF Parsing**: PyMuPDF
* **Environment Management**: python-dotenv

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd streamlit-genai-app
```

### 2. Create virtual environment

```bash
python -m venv streamlit_env
```

### 3. Activate environment

```bash
# Windows
streamlit_env\Scripts\activate

# Mac/Linux
source streamlit_env/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_api_key
OPENAI_BASE_URL=your_base_url   # Required for enterprise/Azure setups
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🧪 How to Use

1. Upload a PDF file
2. Enter a question related to the document
3. View:

   * Retrieved context chunks
   * AI-generated answer

---

## ⚠️ Notes

* Ensure the PDF contains selectable text (not scanned images)
* For enterprise setups, configure correct `base_url` and model name
* Responses are restricted to document context (no hallucination)

---

## 📌 Future Enhancements

* Multi-document support
* Source citation UI
* Streaming responses
* Agent-based workflows

---

## 👨‍🏫 Session Context

This project was built as part of a hands-on session on:

**“Building GenAI Applications with Streamlit and RAG Systems”**

---

## 📄 License

For educational purposes only.
