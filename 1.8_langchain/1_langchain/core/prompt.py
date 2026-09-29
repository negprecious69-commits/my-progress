from langchain_core.prompts import ChatPromptTemplate

chat_prompt=ChatPromptTemplate.from_messages([
    ("system", "Give one-paragraph give training {announcement} to target audience of {audience} with a {tone} tone"),
    ("human", "{audience}")
    ])   
