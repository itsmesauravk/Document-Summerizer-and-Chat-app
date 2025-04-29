from typing import List
from langchain.schema import Document
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from src.document_processor import split_documents
from src.vector_store import create_vector_store
from src.llm import get_llm_model

def create_chat_chain(documents: List[Document]):
    """
    Create a conversational chain for chatting with the research paper.
    
    Args:
        documents: List of Document objects containing the paper content
        
    Returns:
        A ConversationalRetrievalChain instance
    """
    # Split documents into chunks
    splits = split_documents(documents)
    
    # Create vector store
    vector_store = create_vector_store(splits)
    
    # Get LLM model
    llm = get_llm_model()
    
    # Create memory
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        output_key="answer",
        return_messages=True
    )
    
    # Create conversation chain
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(search_kwargs={"k": 4}),
        memory=memory,
        return_source_documents=True
    )
    
    return conversation_chain