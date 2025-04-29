from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

def get_llm_model():
    """
    Get the LLM model.
    
    Returns:
        An instance of ChatGoogleGenerativeAI
    """
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0.2,
        max_tokens=1000,
    )
    return llm