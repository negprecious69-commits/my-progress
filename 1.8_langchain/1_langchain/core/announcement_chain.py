from core.chain import announcement_chain
from .models import create_model
from config import QWEN
from .promts import prompt
from pydantic import BaseModel, Field

model=create_model()

result = announcement_chain.invoke({
        "audience": "low tone",
        "tone": "developers",
        "announcement_details": "details"
    })
class announcement(BaseModel):
        tone:str=Field(description="{results}")
        announcement_details:str=Field(description="{result}")

structured_model = model.with_structured_output(announcement)
results = structured_model.invoke("{prompt}")
print(result.model_dump())