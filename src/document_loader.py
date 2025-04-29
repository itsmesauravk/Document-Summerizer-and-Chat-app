from langchain_community.document_loaders import PyPDFLoader
from typing import List
from langchain.schema import Document

def load_document(file_path: str) -> List[Document]:
    """
    Load a research paper from a PDF file.
    
    Args:
        file_path: Path to the PDF file
        
    Returns:
        List of Document objects containing the paper content
    """
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    
    print(f"Loaded {len(documents)} pages from {file_path}")
    return documents