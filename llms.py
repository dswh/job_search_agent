#define LLMs
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
import os 

def load_llm(llm_name): #gpt-4-0125-preview  gpt-4-turbo-2024-04-09
    if llm_name=='openai':
        llm = ChatOpenAI(model_name="gpt-4-0125-preview", openai_api_key=os.environ["OPENAI_API_KEY"], temperature = 0.1, streaming=True) # type: ignore
    if llm_name=='groq':
        llm = ChatGroq(temperature=0.2, groq_api_key=os.environ["GROQ_API_KEY"], model_name="llama3-8b-8192" )  #temperature = 0.1 mixtral-8x7b-32768 llama3-70b-8192
    return llm