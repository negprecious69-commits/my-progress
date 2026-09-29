# from .models import create_model
# from config import QWEN
# from .prompt import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# model=create_model()
# parser=StrOutputParser()

# def announcement_chain():
#     chain = prompt | model | StrOutputParser()
#     return chain


import streamlit as st
# @st.cache_resources. ---> help store api calls temporarilly
from langchain_core.output_parsers import StrOutputParser
from .models import create_model
from .prompt import chat_prompt
parser = StrOutputParser()

@st.cache_resource
def get_chat_chain():
    model = create_model()
    return chat_prompt | model | parser