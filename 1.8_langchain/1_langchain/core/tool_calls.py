from utils.tools import get_module_deadline, count_students_in_module
from .models import create_model
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage


tools=[get_module_deadline, count_students_in_module]

llm=create_model().bind_tools(tools)
#print(llm)
tools_by_name={t.name: t for t in tools}

#print(tools_by_name)

# we are going to be constructing a message list [HumanMessage, AiMessage, SystemMessage, ToolMessage]

messages=[HumanMessage("How many students are CNN module and when is it due")]
ai_response=llm.invoke(messages)
print(f"Ai response is: {ai_response}")

messages.append(ai_response)

# for us to be able to pass this tool info our llm, we need to run a loop:
for tool in ai_response.tool_calls:
    tool_fn=tools_by_name[tool["name"]]
    result=tool_fn.invoke(tool["args"])
    messages.append(ToolMessage(content=result, tool_call_id=tool["id"]))

    final=llm.invoke(messages)
    print(final.content)