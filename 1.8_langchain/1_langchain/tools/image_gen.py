from langchain_core.tools import tool
import urllib.parse
import requests
import os
#@tool
def generate_image(prompt:str)->str:
    """
    Generate an image from a text description and return the file path.
    Use this when the user ask you to create, draw, or visualise something
    Args:
    prompt: A clear descriptive prompt of the image to generate

    """
    encoded=urllib.parse.quote(prompt)
    url=f"https://image.pollinations.ai/prompt/{prompt}"
    # url=f"https://image.pollination.ai/prompt/{encoded}?width=1024&height=1024&nologo=true"
    response=requests.get(url, timeout=60)
    response.raise_for_status()
    os.makedirs("generate_image", exist_ok=True)
    path=f"generate_image/{abs(hash(prompt))}.png"
    
# write the actual image into the path
    with open(path, 'wb') as f:
        f.write(response.content)
    return path