# get the model in and make sure it works
from .models import create_model
from config import QWEN

# we are goinh to be using something called chatprompttemplate to create a prompt template
from langchain_core.prompts import ChatPromptTemplate
# a good example of s pt

# describe thi {football_player} in one sentence
# given this {data} about this school answer related questions asked by the  user

model = create_model(QWEN)
prompt_template=ChatPromptTemplate.from_messages(
    [
        # system message: "a message given to the model inorder for it to determine how to respond to users"
        # human message : a message give to the model by the human of the app
        ("system", "please in one sentence describe this {football_player} and give a brief history of his career, and also provide a list of his achievements in football."),
        ("human", "{question}")
    ]
)

football_player=input("Enter the name of the football player: ")
question=input("Enter the question you want to ask the football player:")

chain=prompt_template | model
result=chain.invoke({
    "football_player": football_player,
    "question": question
})

print(result)

# to use this pt we use the invoke method
#prompt_template.invoke({
 #   "football_player":"Lionel Messi",
  #  "question": "What are the achievements of Lionel Messi in football"
#})