from utils.tool_ex import student_count_lookup, prereguisite, module_deadline_lookup, session_module_lookup
from .models import create_model
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

tools = [module_deadline_lookup, student_count_lookup, prereguisite, session_module_lookup]

llm= create_model().bind_tools(tools)
#print(llm)

tools_by_name = {t.name: t for t in tools}
