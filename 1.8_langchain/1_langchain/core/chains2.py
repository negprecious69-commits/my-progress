from .models import create_model
from config import QWEN
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel, Field
from .prompt import prompt

model = create_model()
parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: str-Field(description-"overal1 sentiment of the submission ")
    key points: list[str]-Field(description-"points in the feedback ")
    sugested _ Action:str-Field(description-"actions and instructor should take base on the feedback ")
    original _ text:str-Field(description-"original feedback")

from core.chains import build_feedback_classifier

classifier = build_feedback_classifier()

feedbacks = [
    "The service was excellent and very fast.",
    "I am disappointed with the quality of the service.",
    "The experience was okay, nothing special.",
    "The instructor explained everything very clearly.",
    "The application keeps crashing and needs to be fixed."
]

results = []

for feedback in feedbacks:
    result = classifier.invoke(feedback)
    result_dict = result.model_dump()
    result_dict["original_text"] = feedback
    results.append(result_dict)

