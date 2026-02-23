import hashlib
import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
import streamlit as st
from my_llm import get_llm , SYS_PROMPT
from read_pdf import read_text_from_pdf
from chunking import create_chunks
from embedding import create_embedding
from dotenv import load_dotenv



# Load .env file
load_dotenv()


st.header("My First chatbot")
st.write('Upload a PDF file and ask a question!')
with st.sidebar:
    st.title("Your docs")
    file = st.file_uploader("Upload a PDF and ask questions",type="PDF")

# Initialize session state
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "file_hash" not in st.session_state:
    st.session_state.file_hash = None

#after file upload
if file:
    # Create unique hash for uploaded file
    file_bytes = file.getvalue()
    current_file_hash = hashlib.md5(file_bytes).hexdigest()

    # Check if file is new
    if st.session_state.file_hash != current_file_hash:
        try:
            with st.spinner(text='Processing File...', show_time=True):
                
                all_text = read_text_from_pdf(file=file)
                if not all_text or not all_text.strip():
                    st.error("❌ File has no readable content!")
                    
                    raise ValueError
            
                
                chunks = create_chunks(all_text)
                if not chunks or len(chunks) == 0:
                    st.error("❌ Chunking failed. No chunks created.")
                    st.write("Extracted text preview:")
                    st.write(all_text[:500])
                    
                    raise ValueError
                st.success('Data successfully extracted!')
                st.write(f"✅ Number of chunks created: {len(chunks)}")
                #st.write(chunks)
                vector_store = create_embedding(chunks=chunks)
                # Store in session
                st.session_state.vector_store = vector_store
                st.session_state.file_hash = current_file_hash
        except:
            print('exception occurred')
            st.stop()
        
    else:
        st.info("Using existing vector store for this file.")
    vector_store = st.session_state.vector_store

    # get quesstion from user
    user_query = st.text_input(label='Type your query here...',max_chars=200)

    if vector_store and user_query:
 
        retriever = vector_store.as_retriever(
            search_type ='mmr',
            search_kwargs={"k": 3}
        )
        def format_docs(docs):
            return "\n\n".join([doc.page_content for doc in docs])
        
        llm=get_llm()

        prompt = ChatPromptTemplate.from_messages(
            [('system',SYS_PROMPT),
            ('human','{question}')
            ])

        # create chain
        chain = (
            {'context': retriever | format_docs , 'question':RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )
        
        response = chain.invoke(user_query)

        st.write("\n##Answer:")
        # print(response)
        st.write(response)
        # embed the user query
        #do similarity search

        # send to llm

        # process llm response and show output to user

        # take feedback



else:
    print('Upload file to continue')
