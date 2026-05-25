# 📖 PDF Question-Answering App (RAG-based)

> A **PDF Question-Answering App** built with **RAG (Retrieval-Augmented Generation)**, allowing users to upload PDFs and ask context-based questions.  
> Powered by **Streamlit, LangChain, Ollama, and Chroma/FAISS** for efficient and accurate answers.  

[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)  
[![LangChain](https://img.shields.io/badge/Library-LangChain-3b82f6?logo=chainlink&logoColor=white)](https://www.langchain.com/)  
[![Ollama](https://img.shields.io/badge/LLM-Ollama-00A86B?logo=ollama&logoColor=white)](https://ollama.ai/)  
[![FAISS](https://img.shields.io/badge/Vector_DB-Chroma-orange?logo=databricks&logoColor=white)](https://github.com/facebookresearch/chroma)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)  

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📌 Project Overview  
This project is a **Retrieval-Augmented Generation (RAG) based Question-Answering System** where users can upload a **PDF document** and ask questions related to its content.  

It extracts the text, splits it into chunks, stores it in a vector database, and uses a **Large Language Model (LLM)** to provide accurate, context-aware answers.  
The RAG pipeline ensures that answers are **based on real document context** to minimize hallucination.  

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## ✨ Key Features  
- 📂 **Upload PDF** and extract text automatically.  
- 🔍 **Context-aware Q/A** using RAG (retrieves relevant chunks before answering).  
- ⚡ **Efficient Vector Search** with **Chroma/FAISS** backend.  
- 🤖 **LLM-powered answers** using **Ollama + Llama 3.1**.  
- 🖥️ **Interactive GUI** built with **Streamlit** for seamless use.  
- 🔒 Handles temporary files securely during processing.  

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🛠️ Tools & Technologies  
- [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/) – Interactive web interface  
- [![LangChain](https://img.shields.io/badge/LangChain-3b82f6?logo=chainlink&logoColor=white)](https://www.langchain.com/) – RAG pipeline  
- [![Ollama](https://img.shields.io/badge/Ollama-00A86B?logo=ollama&logoColor=white)](https://ollama.ai/) – Local LLM (`llama3.1`, `nomic-embed-text`)  
- [![FAISS](https://img.shields.io/badge/Vector_DB-Chroma/FAISS-orange?logo=databricks&logoColor=white)](https://github.com/facebookresearch/faiss) – Vector similarity search  
- [![PyPDF](https://img.shields.io/badge/PDF-PyPDFLoader-blue?logo=adobeacrobatreader&logoColor=white)](https://python.langchain.com/docs/modules/data_connection/document_loaders/pdf) – Extract text from PDFs  

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📋 Prerequisites  
Before running the project, make sure you have:  
- 🐍 Python **3.9+** installed  
- 📦 **Ollama** installed and running locally → [Install Ollama](https://ollama.ai/)  or Cohere API
- 📥 Pull required models in Ollama:  
  ```bash
  ollama pull llama3.1
  ollama pull nomic-embed-text
  ```
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📂 Project Structure  

The repository is organized as follows:  

```bash
pdf-qa-rag/
│── app.py              
└── requirements.txt    
```

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🚀 Quick Start  

Follow these steps to set up and run the project locally:  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/AtharvaAnbhule/RAG-Textbook-Extraction/.git
```

2️⃣ Create a Virtual Environment (Recommended)

```bash
# For Windows
python -m venv venv
venv\Scripts\activate
```

3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

4️⃣ Install Ollama & Pull Required Models

- Download and install Ollama 

- Pull models locally:

```bash
ollama pull llama3.1
ollama pull nomic-embed-text
```

5️⃣ Run the Application

```bash
streamlit run app.py
```

6️⃣ Open in Browser

- Streamlit will provide a local URL (e.g. http://localhost:8501).
- Open it in your browser to access the PDF Question-Answering App.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📱 How to Use  

1. Start the app by running:  
   ```bash
   streamlit run app.py
   ```
2. Open the Streamlit link in your browser (default: http://localhost:8501).

3. 📂 Upload a PDF

- Use the file uploader to select any PDF (e.g., notes, research papers, or reports).

4. ⚡ Processing

- The system will extract text, split it into chunks, and store them in the vector database.

5. 📝 Ask Your Question

- Enter your query in the text box (e.g., "What is the main conclusion of this paper?").

6. 💡 Get the Answer

- The LLM (Ollama + LangChain) retrieves the most relevant context and generates an accurate, context-based answer.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## 🏗️ Architecture  

The system follows a **RAG (Retrieval-Augmented Generation)** pipeline for answering questions from PDFs.  


### Workflow:
1. 📂 **PDF Documents** → Uploaded by the user.  
2. 🔎 **LangChain Pipeline** → Handles:  
   - PDF Text Extraction  
   - Text Chunking  
   - Vector Store (Chroma/FAISS)  
3. 🤖 **Ollama LLM** → Uses `llama3.1` for generating answers.  
4. 💡 **Generated Response** → Delivered back to the user.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🖥️ GUI Preview  

The application comes with a simple and interactive **Streamlit-based UI**.  

### 📌 Home Screen  
Upload your PDF, enter your question, and get instant answers.  

<img width="1348" height="614" alt="home" src="https://github.com/user-attachments/assets/26ffe22c-98db-4fb4-b666-2a97f0096a2b" />


### 📌 PDF Upload & Processing  
After uploading, the system extracts and processes the PDF text for querying.  

<img width="1061" height="389" alt="upload" src="https://github.com/user-attachments/assets/fcffe942-f5b4-4fac-a234-134dd8f17a23" />

### 📌 Q&A Result  
Ask questions, and the system provides precise answers from the document.  

- Answer Query 1:

<img width="1290" height="630" alt="output1" src="https://github.com/user-attachments/assets/e956e0c1-067f-4ee0-819b-3cdda57648f7" />

- Answer Query 2:

<img width="1354" height="641" alt="query2" src="https://github.com/user-attachments/assets/59d7dd06-1723-4b8a-bb02-2d1cda5e6199" />


- Output:
  
<img width="1338" height="631" alt="query2_output" src="https://github.com/user-attachments/assets/ca995103-a4ef-469d-9356-9680b984cabf" />

- Wrong Query:

  <img width="1352" height="618" alt="wrong_query" src="https://github.com/user-attachments/assets/e2416423-b106-4681-9a73-9a51cdba3b18" />

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🙏 Acknowledgements  

This project is built with the help of:  
- [LangChain](https://www.langchain.com/) – for chaining components in the RAG pipeline  
- [Ollama](https://ollama.ai/) – for running **LLaMA 3.1** locally  
- [Streamlit](https://streamlit.io/) – for the user-friendly interface  
- [ChromaDB / FAISS](https://www.trychroma.com/) – as vector databases for semantic search  
- [nomic-embed-text](https://huggingface.co/nomic-ai/nomic-embed-text) – for text embeddings


