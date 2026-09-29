from .models import create_model
from config import QWEN
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model=create_model(QWEN)
parser=StrOutputParser()

# prompt_template->model->convert_to_string

prompt=ChatPromptTemplate.from_messages([
    ("system", "you are a concise teacher assistant, answer in {max_sentence} sentences"),
    ("human", "{question}")
])
chain=prompt | model | parser
result=chain.invoke({
    "max_sentence": 5,
    "question": "what is the difference between CNN and ANN"
})
print(result)