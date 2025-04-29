from langchain_community.vectorstores import Chroma
from typing import List
from langchain.schema import Document
from src.embeddings import get_embeddings_model

def create_vector_store(documents: List[Document]):
    """
    Create a vector store from documents.
    
    Args:
        documents: List of Document objects
        
    Returns:
        A Chroma vector store
    """
    embeddings = get_embeddings_model()
    vector_store = Chroma.from_documents(documents, embeddings)

    # print("Number of documents:", vector_store._collection.count())
    # data = vector_store._collection.get()
    # print("Stored documents:", data['documents'])
    # print("Stored IDs:", data['ids'])

    return vector_store