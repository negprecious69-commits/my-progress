from langchain.agents import create_agent
from .model import create_model
from utils.tools import get_module_deadline, count_students_in_module, preriquisite, session_module_lookup

model = create_model()
agent = create_agent(
    model = model,
    tools = [module_deadline, count_students_in_module, preriquisite, session_module_lookup],
    system_prompt = 'You are an operations assistant for a university. use tools to answer factual questions accuratly'
)

result = agent.invoke({"messages": [{"role": "user", "content": "can a student who has not finished physics stay?"}]})
print(result["messages"][-1].content)
