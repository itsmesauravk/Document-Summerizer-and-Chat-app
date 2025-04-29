import os
import streamlit as st
from src.document_loader import load_document
from src.summarizer import generate_summary
from src.chat_chain import create_chat_chain

def main():
    st.title("Chat with Document")
      
    
    # File upload
    uploaded_file = st.file_uploader("Upload Research Paper (PDF)", type="pdf")
    
    
    if uploaded_file:
        # Save uploaded file
        file_path = os.path.join("uploads", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Process document
        if "processed" not in st.session_state:
            with st.spinner("Processing your research paper..."):
                # Load document
                documents = load_document(file_path)
                
                # Generate summary
                summary = generate_summary(documents)
                
                # Create chat chain
                chat_chain = create_chat_chain(documents)
                
                # Store in session state
                st.session_state.summary = summary
                st.session_state.chat_chain = chat_chain
                st.session_state.processed = True
        
        # Display summary
        st.header("Paper Summary")
        st.write(st.session_state.summary)
        
        # Chat interface
        st.header("Chat with the Paper")
        if "messages" not in st.session_state:
            st.session_state.messages = []
            
        # Display chat history
        # for message in st.session_state.messages:
        #     with st.chat_message(message["role"]):
        #         st.write(message["content"])
        for message in st.session_state.messages:
            
            if message["role"] == "user":
                with st.chat_message(message["role"], avatar="👤"):  
                    st.write(message["content"])
            else:
                with st.chat_message(message["role"], avatar="🤖"):  
                    st.write(message["content"])
                
        # Chat input
        user_query = st.chat_input("Ask a question about the paper")
        if user_query:
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": user_query})
            with st.chat_message("user", avatar="👤"):
                st.write(user_query)
                
            # Generate AI response
            with st.chat_message("assistant", avatar="🤖"):
                with st.spinner("Thinking..."):
                    response = st.session_state.chat_chain({"question": user_query})
                    st.write(response["answer"])
                    
            # Add AI response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response["answer"]})

if __name__ == "__main__":
    # Create uploads directory if it doesn't exist
    os.makedirs("uploads", exist_ok=True)
    main()