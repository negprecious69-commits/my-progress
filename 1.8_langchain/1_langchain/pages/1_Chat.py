# import streamlit as st
# from langchain_core.messages import HumanMessage, AIMessage
# from core.chains import get_chat_chain

# st.set_page_config(page_title="chat", page_icon="📈") 

# if "history" not in st.session_state:

#     st.session_state.history=[]

# chain=get_chat_chain()

# for msg in st.session_state.history:
#     role="user" if isinstance(msg, HumanMessage) else "assistant"
#     with st.chat_message(role):
#         st.markdown(msg.content)

#   # what if there is an input
# user_input = st.chat_input("Ask your question....")

# if user_input:
#     st.session_state.history.append(HumanMessage(content=user_input))
#     with st.chat_message("user"):
#         st.markdown(user_input)
#     with st.chat_message("assistant"):
#         full_reply=st.write_stream(
#             chain.stream({"input":user_input, "history":st.session_state.history[:-1]})
#         )    
#         st.session_state.history.append(AIMessage(content=full_reply))

import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from core.chains import get_chat_chain


st.set_page_config(page_title="Chat", page_icon="💬")
st.header("Football Chat Bot")
with st.sidebar:
    st.title("persona")
    persona=st.selectbox(
        "Choose a persona:",
        ["Encouraging tactician", "football medical doctor", "football player"]

    )

    chain = get_chat_chain()


# PERSONAS = ["Encouraging tactician", "Football medical doctor", "Sarcastic mentor"]
# persona = st.sidebar.selectbox("Choose a persona", PERSONAS)



if "history" not in st.session_state:
    st.session_state.history = []


# # rebuild chain if persona changes so the system prompt stays fresh
# if "persona" not in st.session_state or st.session_state.persona != persona:
#     st.session_state.persona = persona
#     st.session_state.chain = get_chat_chain()


for msg in st.session_state.history:
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.markdown(msg.content)



user_input = st.chat_input("Ask your question....")

if user_input:
    st.session_state.history.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("thinking..."):
            full_reply = st.write_stream(
                chain.stream({"input": user_input, "history": st.session_state.history[:-1], "persona": persona})
        )
        st.session_state.history.append(AIMessage(content=full_reply))