# import os
# from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
# from dotenv import load_dotenv

# load_dotenv()

# # Make sure you have set HUGGINGFACEHUB_API_TOKEN in your .env file
# api_token = os.environ.get("HUGGINGFACEHUB_ACCESS_TOKEN")

# # HuggingFace Inference API Embeddings
# embeddings = HuggingFaceInferenceAPIEmbeddings(
#     api_key=api_token,
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )
# result = embeddings.embed_query("What is the capital of France?")
# print(result)  # This will print the embedding vector for the query

from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

try:
    # Install sentence-transformers if not already installed
    # !pip install sentence-transformers
    
    # Use local HuggingFace model instead of API
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    
    result = embeddings.embed_query("What is the capital of France?")
    print(result)  # This will print the embedding vector for the query
    print(f"Embedding successful! Vector length: {len(result)}")
    print(f"First few values: {result[:5]}")
    
except Exception as e:
    print(f"Error: {str(e)}")
    print("Make sure you have the sentence-transformers package installed:")
    print("pip install sentence-transformers")