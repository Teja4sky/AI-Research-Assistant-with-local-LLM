# AI Research Assistant (Local LLM + RAG Architecture)

A professional AI Research Assistant built using a locally running Large Language Model (Llama 3.1 via Ollama) and Streamlit framework. This system implements a Retrieval-Augmented Generation (RAG) architecture to provide accurate, contextual, and intelligent research responses.

The assistant retrieves relevant information from local documents, Wikipedia, and ArXiv, and augments the LLM with this data to generate precise and meaningful answers.

---

## Architecture: Retrieval-Augmented Generation (RAG)

This project follows the RAG pipeline:

1. User Query Input  
2. Retrieval Layer  
   - Local PDF document parsing  
   - Wikipedia retrieval  
   - ArXiv research retrieval  

3. Augmentation Layer  
   - Retrieved context is combined with the user query  

4. Generation Layer  
   - Llama 3.1 (via Ollama) generates a context-aware response  

5. Output Processing  
   - Semantic highlighting of important technical terms  
   - Structured response display  

---

## Features

• Local LLM powered by Ollama (Llama 3.1)  
• Retrieval-Augmented Generation (RAG) architecture  
• PDF document analysis support  
• Wikipedia knowledge integration  
• ArXiv research paper integration  
• Semantic highlighting of important concepts  
• Premium modern UI  
• Offline capability (no external LLM APIs required)  
• Privacy-focused system  

---

## Framework and Technologies Used

Framework:
- Streamlit (Frontend + Application Framework)

Backend:
- Python

LLM Runtime:
- Ollama
- Llama 3.1

Retrieval Sources:
- Wikipedia API
- ArXiv API
- Local PDF parsing using PyMuPDF

---
## Application Preview

<img width="1760" height="891" alt="image" src="https://github.com/user-attachments/assets/e547a831-efff-4dbd-b6bc-ccf1beba0cea" />

---

## How to Run

Install dependencies:
  pip install -r requirements.txt
 
Run the application: 
  streamlit run app.py


---

## Use Cases

• AI research assistance  
• Cybersecurity research and learning  
• Academic and technical research  
• Offline AI assistant systems  
• Document analysis and knowledge extraction  

---

## Project Highlights

• Implements real-world RAG architecture  
• Fully local LLM deployment  
• No cloud dependency  
• Designed for efficiency on 8GB RAM systems  
• Production-ready UI and architecture  

---

## Author

CH Teja Surya  
Computer Science Engineering  
Specialization: Cybersecurity, Artificial Intelligence, Retrieval-Augmented Generation (RAG), Local LLM Systems, and Cloud Computing


