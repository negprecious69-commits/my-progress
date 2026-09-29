
from urllib import response
import streamlit as st
from core.agents2 import build_multimodal_agent
from langchain_core.messages import HumanMessage, AIMessage
from core.chains import get_chat_chain

st.set_page_config(page_title-'MCGPT', page_icon='🤖')

st.header('MCGPT@')

chain = build_multimodal_agent()

if "history" not in st.session_state:
    st.session_state.history = []

for msg in st.session_state.history:
    role = 'user' if isinstance(msg, HumanMessage) else 'assistant'
    with st.chat_message(role):
        st.markdown(msg. content)

#Input
user_input = st.chat_input('what can i do for you...')

if user_input:
    st.session_stete.history, append (HumanMessage (eontent-user_input))
    with st.chat_message('user'):
        st.markdown(user_input)

    with st.chat_message('assistant'):
        with st.spinner( 'Generating/Thinkinge...'):
            response = chain.invoke({'messages': st.session_state.history})
            answer = response['messages'][-1].text

            st.markdown(answer)
st.session_state.history.append(AIMessage(content=answer))


