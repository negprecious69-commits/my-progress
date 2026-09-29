from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def build_chat_prompt(persona: str) -> ChatPromptTemplate:
    system_message = (
        f"You are a helpful assistant with the following persona: {persona}. "
        "Stay in character while answering the user's questions."
    )
    return ChatPromptTemplate.from_messages([
        ("system", system_message),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ])

def get_chat_chain(persona: str):
    prompt = build_chat_prompt(persona)
    return prompt | model  # your existing model/parser pipeline