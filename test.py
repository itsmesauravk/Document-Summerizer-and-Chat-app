# ChatWRP: Chat with Research Papers
# Complete implementation using LangChain

import os
from typing import List
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationalRetrievalChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class ChatWRP:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            temperature=0.2,
            max_tokens=1000,
        )
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.conversation_chain = None
        self.vectorstore = None
    
    def load_pdf(self, pdf_file):
        """Load and process a research paper in PDF format"""
        # Create a temporary file to save the uploaded PDF
        temp_file_path = f"temp_paper_{os.path.basename(pdf_file.name)}"
        with open(temp_file_path, "wb") as f:
            f.write(pdf_file.getbuffer())
        
        # Load the PDF
        loader = PyPDFLoader(temp_file_path)
        documents = loader.load()
        
        # Remove the temporary file
        os.remove(temp_file_path)
        
        return documents
    
    def process_paper(self, documents):
        """Process the paper by splitting into chunks and creating a vector store"""
        # Split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            separators=["\n\n", "\n", " ", ""]
        )
        chunks = text_splitter.split_documents(documents)
        
        # Create vector store
        self.vectorstore = FAISS.from_documents(chunks, self.embeddings)
        
        # Initialize conversation memory
        memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        
        # Create the conversation chain
        self.conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=self.vectorstore.as_retriever(search_kwargs={"k": 3}),
            memory=memory
        )
        
        return chunks
    
    def generate_summary(self, documents):
        """Generate a summary of the research paper"""
        # Combine all document contents
        full_content = " ".join([doc.page_content for doc in documents])
        
        # Create a summarization prompt
        summarization_prompt = f"""
        Please provide a comprehensive summary of the following research paper. 
        Include key findings, methodology, results, and conclusions.
        
        PAPER CONTENT:
        {full_content[:10000]}  # Limiting to first 10k chars to avoid context limits
        
        SUMMARY:
        """
        
        # Generate summary
        summary_response = self.llm.invoke(summarization_prompt)
        
        return summary_response.content
    
    def chat_with_paper(self, query):
        """Chat with the research paper"""
        if not self.conversation_chain:
            return "Please upload a research paper first."
        
        response = self.conversation_chain.invoke({"question": query})
        return response["answer"]

# Streamlit UI
def main():
    st.title("ChatWRP: Chat with Research Papers")
    
    # Initialize the chat system
    if 'chat_system' not in st.session_state:
        st.session_state.chat_system = ChatWRP()
    
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Upload paper section
    with st.sidebar:
        st.header("Upload Research Paper")
        paper_file = st.file_uploader("Choose a PDF file", type="pdf")
        
        if paper_file is not None and 'current_paper' not in st.session_state:
            st.session_state.current_paper = paper_file.name
            with st.spinner("Processing research paper..."):
                documents = st.session_state.chat_system.load_pdf(paper_file)
                st.session_state.chunks = st.session_state.chat_system.process_paper(documents)
                st.session_state.summary = st.session_state.chat_system.generate_summary(documents)
                st.success("Paper processed successfully!")
                
                # Reset chat history for new paper
                st.session_state.chat_history = []
        
        if st.button("Clear Paper"):
            if 'current_paper' in st.session_state:
                del st.session_state.current_paper
                del st.session_state.chunks
                del st.session_state.summary
                st.session_state.chat_history = []
                st.experimental_rerun()
    
    # Display paper summary
    if 'current_paper' in st.session_state:
        st.header(f"Paper: {st.session_state.current_paper}")
        
        with st.expander("Paper Summary", expanded=True):
            st.write(st.session_state.summary)
        
        # Chat interface
        st.header("Chat with the Paper")
        
        # Display chat history
        for message in st.session_state.chat_history:
            role = "🧑‍💼 You" if message["is_user"] else "🤖 ChatWRP"
            st.write(f"{role}: {message['content']}")
        
        # User input
        user_query = st.text_input("Ask a question about the paper:")
        
        if st.button("Send"):
            if user_query:
                # Add user message to chat history
                st.session_state.chat_history.append({"is_user": True, "content": user_query})
                
                # Get response from ChatWRP
                with st.spinner("Thinking..."):
                    response = st.session_state.chat_system.chat_with_paper(user_query)
                
                # Add system response to chat history
                st.session_state.chat_history.append({"is_user": False, "content": response})
                
                # Refresh the page to show new messages
                st.experimental_rerun()
    else:
        st.info("Please upload a research paper to start chatting.")

if __name__ == "__main__":
    main()