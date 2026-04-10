import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from search import query_quran
from dotenv import load_dotenv

load_dotenv()

# 1. Initialize the LLM (Using Llama 3 via Groq for speed)
llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-8b-instant")

def generate_answer(user_query):
    # Step A: Retrieve relevant verses from your ChromaDB
    search_results = query_quran(user_query)
    
    # FIX: Access the inner lists using [0]
    docs = search_results['documents'][0]
    metas = search_results['metadatas'][0]
    
    # Step B: Format the context (The verses)
    context_list = []
    for d, m in zip(docs, metas):
        context_list.append(f"Surah {m['surah_name']} (No. {m['surah_no']}), Ayah {m['ayah_no']}: {d}")
    
    context_text = "\n\n".join(context_list)

    # Step C: The Professional Prompt
    prompt_template = ChatPromptTemplate.from_template("""
    You are Bayyan AI, a specialized Quranic scholar assistant. 
    Your goal is to answer questions using ONLY the verses provided in the Context below.
    
    Rules:
    1. Always cite the Surah and Ayah number for every claim you make.
    2. If the context contains multiple perspectives (e.g., helping others vs helping oneself), explain both.
    3. If the context does not contain enough information to answer the question accurately, explain what the provided verses DO cover regarding the topic.
    
    Context:
    {context}
    
    Question: 
    {question}
    
    Answer:
""")


    # Step D: Chain and Invoke
    chain = prompt_template | llm
    response = chain.invoke({"context": context_text, "question": user_query})
    
    return response.content

if __name__ == "__main__":
    q = "What does the Quran say about helping others?"
    print(f"User: {q}\n")
    print(f"Bayyan AI: {generate_answer(q)}")
