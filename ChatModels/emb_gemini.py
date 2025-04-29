from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()


embeddings = GoogleGenerativeAIEmbeddings(model="embedding-001")
result = embeddings.embed_query("What is the capital of France?")
print(str(result))