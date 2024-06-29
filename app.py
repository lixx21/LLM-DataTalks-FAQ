from getData import getData
from elasticSearch import createIndex, elastic_search
from mistralAI import build_prompt, llm
import streamlit as st
from stqdm import stqdm

st.title("DataTalks FAQ Chatbot")
# Initialize session state for data and esclient
def initialize_data():
    if 'data_initialized' not in st.session_state:
        st.session_state.documents = getData()
        st.session_state.index_name = "course-questions"
        st.session_state.esclient = createIndex(st.session_state.index_name)

        with st.spinner('Preparing the data...'):
            for doc in stqdm(st.session_state.documents):
                # input the data to elastic search
                st.session_state.esclient.index(index=st.session_state.index_name, document=doc)

        st.session_state.data_initialized = True

# Initialize data only if not already done
if 'data_initialized' not in st.session_state:
    initialize_data()

with st.form("my_form"):
    query = st.text_input("Input Question", "tell me more about the course")
    submitted = st.form_submit_button("Submit")
    
if submitted:
    with st.spinner('Preparing the answer...'):
        search_result = elastic_search(st.session_state.esclient, query, st.session_state.index_name)
        prompt = build_prompt(query, search_result)
        response = llm(prompt)
        st.write(response)



