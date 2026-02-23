import pdfplumber

def read_text_from_pdf(file):
    '''
    Reads text from a PDF file and returns it as a string.
    '''
    if file:
        try:
            all_text =""
            with pdfplumber.open(file) as pdf:
                for page in pdf.pages:
                    all_text+= page.extract_text() + '\n'
            print("Extracted length:", len(all_text))
            
        except Exception as e:
            print('An error occurred while reading the PDF file.')
            raise FileNotFoundError('File is not provided')
    else:
        print('No file provided. Please upload a PDF file to continue.')
        raise FileNotFoundError('File is not provided')
    if len(all_text) ==0:
            print('Not able to extract any text from file !')
    
    return all_text