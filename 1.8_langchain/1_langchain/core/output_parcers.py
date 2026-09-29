from pydantic import BaseModel, Field
from .models import create_model
from config import QWEN

model=create_model()

# create the blueprint for the output of the model

class Player(BaseModel):
    name:str=Field(description="Name of the player")
    age:int=Field(description="Age of the player")
    club:str=Field(description="Club of player")
    nationality:str=Field(description="Nationality of the player")
    national_flag:str=Field(description="National flag of the player as an emoji")

class TopTen(BaseModel):
    oppinion:str=Field(description="The option of the model about the top 10 footballers of all time")
    players:list[Player]=Field(description="list of to 10 footballers of all time")    

structured_model=model.with_structured_output(TopTen)
result=structured_model.invoke("Give me the best 10 footballers of all time")
# .model-Dump() will return the output in a dictionary format
print(result.model_dump())
