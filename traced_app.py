from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

prompts = [
    "What is LangChain?",
    "Why is LangChain useful in AI applications?",
    "Give me a simple real-world example of LangChain."
    "Who is the CM of tamil nadu?"
]

for p in prompts:
    response = llm.invoke(p)
    print(response.content)