from langchain_core.tools import tool
from langchain_tavily import TavilySearch
import os
from dotenv import load_dotenv

load_dotenv()
web_search = TavilySearch(
    max_result=5,
    topic="general"
)

result = web_search.run({"query":"What is the capital of France?"})
print(result)