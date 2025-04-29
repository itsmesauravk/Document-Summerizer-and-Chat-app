from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.2,
    max_tokens=1000,
    )

result = model.invoke("I am creating a project name ChatWRP where user can upload paper and chat with them. Give me simple pipline to do that.")

print(result.content)