from tools .image_gen import generate_image
from tools .voice import text_to_speech
# from tools.websearch import TavilySearch

# result = text_to_speech.invoke({"text":"advice a young boy to study Ai"})
# print(result)

result=generate_image("a blue bird")
print(result)