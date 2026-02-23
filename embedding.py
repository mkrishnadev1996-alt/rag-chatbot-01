
#from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_community.vectorstores import FAISS
import os
from dotenv import load_dotenv

def create_embedding(chunks):
    '''
    This function takes the chunks of text and creates an embedding using HuggingFaceEndpointEmbeddings.
    It then creates a vector store using FAISS and returns it.'''

    load_dotenv()
    embeddings = HuggingFaceEndpointEmbeddings(
        repo_id="sentence-transformers/all-MiniLM-L6-v2",
        huggingfacehub_api_token=os.getenv("HF_TOKEN_ONE"),
        task="feature-extraction"
    )

    # embeddings = HuggingFaceEmbeddings(
    #     model = 'google/embeddinggemma-300m',
    #     api_key= os.getenv('HF_TOKEN_ONE')
    # )

    # embeddings =OpenAIEmbeddings(
    #     base_url= os.getenv('BASE_URL'),
    #     model = 'google/embeddinggemma-300m',
    #     api_key= os.getenv('HF_TOKEN_ONE')
    # ) 
    if not chunks:
        raise ValueError("Chunks list is empty. Cannot create embeddings.")
    vector_store = FAISS.from_texts(chunks,embedding=embeddings)
    
    print('vector store created')
    print("Number of vectors:", vector_store.index.ntotal)


    return vector_store