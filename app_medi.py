# Import necessary libraries
import streamlit as st  #Python library for building interactive web applications with simple Python scripts.
from langchain import HuggingFaceHub, PromptTemplate, LLMChain  #langchain library for integrating language models into applications.
# Set environment variable for authentication
import os
os.environ['API_KEY'] = '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'  #authorize access to some services

# set page title
st.set_page_config(page_title='Medicine Recommendation System')
st.title('Medicine Recommendation System')
# text input 
txt_input = st.text_area('Enter your symptoms:', height=50)

# Function to generate response from language model
def generate_response(input):
    # Initialize Hugging Face Hub with API token and model parameters
    flan_llm = HuggingFaceHub(huggingfacehub_api_token=os.environ['API_KEY'],
             repo_id='openchat/openchat-3.5-0106',
             model_kwargs={'temperature':0.6,'max_new_tokens':800})

    # Define a prompt template for the language model
    template =  '''Act as a doctor please give list of three medicines for following symptoms:{question}.don't provide any other text'''
    prompt = PromptTemplate(template=template,input_variables=['question'])

    # Initialize LLMChain with prompt and language model
    flan_chain = LLMChain(prompt=prompt, llm=flan_llm, verbose=True)

    # Generate output from user input
    output = flan_chain.run(input)
    return output
# Form to accept user's text input and response
result = []

# create a form to submit user data
with st.form('summarize_form', clear_on_submit=True):
    submitted = st.form_submit_button('Submit')
    if submitted:
        with st.spinner('AI Doctor is Thinking...'):
            # Generate response using user input
            response = generate_response(txt_input)
            result.append(response)
            print(txt_input)
# Show response if result is not empty
if len(result):
    st.info(response)