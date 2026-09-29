from .models import create_model
from itertools import chain
from config import QWEN
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model=create_model(QWEN)
parser=StrOutputParser()

prompt=ChatPromptTemplate.from_messages([
    ("system", "Give one-paragraph explanation of {topic} to target audience of {audience}"),
    ("human", "{audience}")
    ])   

topic = input("Enter your topic:")
audience = input("Enter audience level:")

chain=prompt | model | parser
result=chain.invoke({
    "topic": topic,
    "audience": audience

})
print(result)