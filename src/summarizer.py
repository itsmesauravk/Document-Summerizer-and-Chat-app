from typing import List
from langchain.schema import Document
from src.llm import get_llm_model

def generate_summary(documents: List[Document]) -> str:
    """
    Generate a summary of the research paper.
    
    Args:
        documents: List of Document objects containing the paper content
        
    Returns:
        A summary of the paper
    """
    llm = get_llm_model()
    
    # Combine document texts for summarization
    text = " ".join([doc.page_content for doc in documents])
    
    # Limit text length for the LLM
    text_for_summary = text[:10000] + "..." if len(text) > 10000 else text
    
    # Generate summary
    prompt = f"Summarize this research paper in about 2 paragraphs. Focus on the main findings,math, methodology, and significance of the research:\n\n{text_for_summary}"
    
    summary_response = llm.invoke(prompt)
    summary = summary_response.content
    
    return summary