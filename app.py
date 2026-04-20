import streamlit as st
from utils.llm import get_response
from utils.rag import load_pdf, create_vector_store, retrieve_docs
from utils.state import init_chat, add_user_message, add_ai_message

st.set_page_config(page_title="GenAI Chat App", layout="wide")

st.title("📄 Chat with your Documents (RAG + GenAI)")

# Initialize chat
init_chat()

# Sidebar - Upload PDF
st.sidebar.header("Upload Document")

uploaded_file = st.sidebar.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    with open("data/temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    docs = load_pdf("data/temp.pdf")
    db = create_vector_store(docs)

    st.sidebar.success("Document processed!")

    query = st.text_input("Ask something about the document")

    if st.button("Ask"):
        add_user_message(query)

        retrieved_docs = retrieve_docs(db, query)

        # Improving retrival quality

        # retrieved_docs = [
        #      doc for doc in retrieve_docs(db, query)
        #      if len(doc.page_content.strip()) > 50
        # ][:3]

        # From where answer came from
        # st.subheader(" Retrieved Context")

        # for i, doc in enumerate(retrieved_docs):
        #     st.write(f"Chunk {i+1}:")
        #     st.write(doc.page_content[:300])
        

        context = " ".join([doc.page_content for doc in retrieved_docs])

        # response = get_response([
        #     {"role": "system", "content": "Answer based on the context"},
        #     {"role": "user", "content": f"Context: {context}\nQuestion: {query}"}
        # ])

        response = get_response([
             {
                 "role": "system",
                 "content": """You are a document Q&A assistant.

                Rules:
                1. Answer ONLY from the provided context
                2. Do NOT use prior knowledge
                3. If answer is not found, say: "Not found in document"
                4. Be concise and accurate
                """
            },
             {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion:\n{query}"
             }
        ])

        add_ai_message(response)

# Display chat
st.subheader("💬 Chat")

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.write(f"🧑‍💻: {msg['content']}")
    else:
        st.write(f"🤖: {msg['content']}")