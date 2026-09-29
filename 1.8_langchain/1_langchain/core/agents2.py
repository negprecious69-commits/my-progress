from langgraph.prebuilt import create_react_agent
from core.models import create_model
from tools.image_gen import generate_image
from tools.search import web_search
from tools.voice import text_to_speech

SYSTEM_PROMPT = """You are a helpful multimodal assistant with tools for
image generation, web search, and text-to-speech.

only call a tool when the request genuinely needs it:
- generate_image: only when the user ask you to create, draw, or visualise something.
- web_search: only for current event, recent news and facts you wouldn't reliably know.
- text_to_speech: only when the user explicitly asks for audio or spoken output.

For everything else, greetings, general knowledge, conversations, explanations, answer directly without calling a tool.
"""

def build_multimodal_agents():
    model = create_model()
    tools = [generate_image, web_search, text_to_speech]
    return create_react_agent(model, tools, prompt=SYSTEM_PROMPT)

agent = build_multimodal_agents()

result = agent.invoke({
    "messages": [{"user", "generate an image of alan walker"}]
})

print(result["messages"][-1].content)