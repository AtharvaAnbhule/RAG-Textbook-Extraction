import os
import tempfile
import streamlit as st

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_chroma import Chroma

from langchain_cohere import CohereEmbeddings
from langchain_cohere import ChatCohere


# ============================================
# SET COHERE API KEY
# ============================================

os.environ["COHERE_API_KEY"] = "rI8PURz0a6JliOwgrLiILRJNHdNgXlFQzZfrShhi"


# ============================================
# EXTRACT TEXT FROM PDF
# ============================================

def extract_text_from_pdf(file_path):

    loader = PyPDFLoader(file_path)

    documents = loader.load()

    text = ""

    for doc in documents:
        text += doc.page_content

    return text


# ============================================
# SPLIT TEXT INTO CHUNKS
# ============================================

def split_text_into_chunks(
    text,
    chunk_size=1000,
    chunk_overlap=200
):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = text_splitter.create_documents([text])

    return chunks


# ============================================
# COHERE EMBEDDINGS
# ============================================

embeddings = CohereEmbeddings(
    model="embed-english-v3.0"
)


# ============================================
# CREATE VECTOR STORE
# ============================================

def create_vector_store(chunks):

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    return vector_store


# ============================================
# GENERATE RESPONSE
# ============================================

def generate_response(vector_store, query):

    # LLM
    llm = ChatCohere(
        model="command-a-03-2025",
        temperature=0.3
    )

    # Retrieve similar chunks
    matching_docs = vector_store.similarity_search(
        query,
        k=3
    )

    # Create context
    context = "\n\n".join(
        [doc.page_content for doc in matching_docs]
    )

    # Prompt
    prompt = f"""
    Answer the question ONLY using the context below.

    Context:
    {context}

    Question:
    {query}

    If answer is not found in context,
    say "Answer not found in document."
    """

    # Generate answer
    response = llm.invoke(prompt)

    return response.content


# ============================================
# STREAMLIT UI
# ============================================

st.set_page_config(
    page_title="PDF RAG Chatbot",
    layout="wide"
)

st.title("📄 PDF Question Answering App")

st.write(
    "Upload a PDF and ask questions from it."
)

# Upload PDF
uploaded_file = st.file_uploader(
    "Upload a PDF file",
    type="pdf"
)

if uploaded_file is not None:

    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:

        temp_file.write(
            uploaded_file.getbuffer()
        )

        temp_file_path = temp_file.name

    # Extract text
    with st.spinner("Extracting text from PDF..."):

        raw_text = extract_text_from_pdf(
            temp_file_path
        )

    if raw_text:

        # Split text
        with st.spinner("Splitting text into chunks..."):

            chunks = split_text_into_chunks(
                raw_text
            )

        # Create vector DB
        with st.spinner("Creating vector store..."):

            vector_store = create_vector_store(
                chunks
            )

        st.success("PDF processed successfully!")

        # Query input
        query = st.text_input(
            "Enter your question:"
        )

        if query:

            with st.spinner("Generating answer..."):

                answer = generate_response(
                    vector_store,
                    query
                )

            st.subheader("Answer")

            st.write(answer)

    # Delete temp file
    os.unlink(temp_file_path)

else:

    st.warning(
        "Please upload a PDF file."
    )