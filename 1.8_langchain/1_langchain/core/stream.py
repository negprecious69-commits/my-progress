from .models import create_model
from config import QWEN

model=create_model(QWEN)
response=model.invoke("who is the first lady of America")

print(response.content)

#for chunk in model.stream("who is the GOAT OF FOOTBALL"):
    #print(f"{chunk.text}", end=" | ", flush=True)

message_batch=[
    "why do they call black Americans Nigros"
    "Who was the first president od cameroon"
    "who started World war 2?"
]

responses=model.batch(message_batch)

for r in responses:
    print(r.text)