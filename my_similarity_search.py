

def get_similarity_search(vector_store ,user_query ='What is the document about?'):
    '''This function takes the vector store and performs a similarity search on it. 
    It returns the results of the search.'''

    results = vector_store.similarity_search(user_query, k=4, score_threshold=0.5, include_metadata=True, include_scores=True)

    for i, doc in enumerate(results):
        print(f"\nResult {i+1}:")
        print(doc.page_content)