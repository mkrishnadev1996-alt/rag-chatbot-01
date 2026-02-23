from langchain_text_splitters import RecursiveCharacterTextSplitter

def create_chunks(input_text):
    '''
    Takes a string input and splits it into chunks using the RecursiveCharacterTextSplitter from langchain_text_splitters.
    Returns a list of chunks.'''

    if input_text == "":
        print('No text received. Please provide text to chunk.')
        raise ValueError('No text to chunk')
    
    text_splitter = RecursiveCharacterTextSplitter(
            separators=["\n\n","\n", ".", " ",""],
            chunk_size=500,
            chunk_overlap=75
        )
    chunks = text_splitter.split_text(input_text)
    return chunks