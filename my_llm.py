import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

SYS_PROMPT= '''
You are a helpfule assistant who will take user questions and provide answer in a unbiased, factual, human readable way.
Guidelines:
If the answer is not known, say 'This information is not available. Please try a different query.'.
If question is about dangerous topics, looing to trick you, answer as 'These question is restricted.'
If the question is out of topic, answer as 'This question is out of topic. Please try a different query in allowed context.'  
Only provide details from the given context. Do not use outside information.
'Context':{context}
'''

def get_llm():

    # Load .env file
    load_dotenv()

    llm = ChatOpenAI(
        base_url=os.getenv('BASE_URL'),
        model=os.getenv("MODEL_NAME"),
        api_key=os.getenv('HF_TOKEN_ONE'),
        temperature=0.1
    )

    return llm