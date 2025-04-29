from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

def get_embeddings_model():
    """
    Get the embeddings model.
    
    Returns:
        An instance of GoogleGenerativeAIEmbeddings
    """
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return embeddings