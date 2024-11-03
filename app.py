import streamlit as st
from pathlib import Path
from streamlit_chat import message
from langchain.document_loaders import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import os


#Setup chatbot
st.title("Fast Chatbot HAI DJPb")

os.environ["OPENAI_API_KEY"] = st.secrets["open_ai_api_key"]
    
loader = CSVLoader(file_path=os.path.join('content/dataTiketHAI.csv'))

# Buat index
index_creator = VectorstoreIndexCreator()
docsearch = index_creator.from_loaders([loader])

# Buat rantai tanya-jawab berdasarkan index
chain = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=docsearch.vectorstore.as_retriever(), input_key="question")

    # Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


def generate_response(user_query):
    response = chain({"question": user_query})
    return response['result']


# Ambil inputan user dengan memanggil get_text function
def get_text():
    input_text = st.text_input("You: ","Mau nanya apa hari ini?", key="input")
    return input_text
user_input = get_text()

if user_input:
    output = generate_response(user_input)
    # store the output 
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')