Live app can be found at URL 
https://vamsi-rag-chatbot-01.streamlit.app/

Steeps for deploying on local
1.create evfile as below


OPENAI_API_KEY=<open ai api key>
HF_TOKEN_ONE=<Hugging face token>
BASE_URL=https://router.huggingface.co/v1
MODEL_NAME=meta-llama/Llama-3.1-8B-Instruct
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

2. Install Python 3.12

3.install dependencies with pip

pip install -r requirements.txt

4.Run streamlit app with using command below

stramlit run app.py



Projec Details:
Simple RAG chatbot.
1. Upload PDF doc by user
2. Read text from the PDF
3. Chunk the Text
4. Embedd the Text
5. store in vector db
6. Get Query from user
7. use lang chain to query LLM
8. Show output to user

 
