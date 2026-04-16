
# from langchain_community.document_loaders import PyPDFLoader
# from langchain_community.vectorstores import FAISS
# from langchain_openai import OpenAIEmbeddings
# from dotenv import load_dotenv
# import os

# from langchain_text_splitters import RecursiveCharacterTextSplitter
# load_dotenv()

# # def load_pdf(file_path):
# #     loader = PyPDFLoader(file_path)
# #     return loader.load()

# def load_pdf(file_path):
#     loader = PyPDFLoader(file_path)
#     docs = loader.load()

#     # ✅ ADD CHUNKING (VERY IMPORTANT)
#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500,
#         chunk_overlap=50
#     )

#     split_docs = splitter.split_documents(docs)

#     return split_docs

# def create_vector_store(docs):
#     embeddings = OpenAIEmbeddings(
#         api_key=os.getenv("OPENAI_API_KEY"),
#         base_url=os.getenv("OPENAI_BASE_URL")  # ✅ THIS FIXES YOUR ERROR
#     )

#     db = FAISS.from_documents(docs, embeddings)
#     return db

# def retrieve_docs(db, query):
#     return db.similarity_search(query)

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
import os

load_dotenv()

def load_pdf(file_path):
    loader = PyMuPDFLoader(file_path)
    docs = loader.load()

    # ✅ Chunking
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    split_docs = splitter.split_documents(docs)

    return split_docs

def create_vector_store(docs):
    embeddings = OpenAIEmbeddings(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL")
    )

    db = FAISS.from_documents(docs, embeddings)
    return db

def retrieve_docs(db, query):
    return db.similarity_search(query)