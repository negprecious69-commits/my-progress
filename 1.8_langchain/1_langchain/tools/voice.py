from dotenv import load_dotenv
from httpx import request
from langchain_core.tools import tool
import requests
import os

load_dotenv()
API_KEY = os.environ["YARNGPT_API_KEY"]
API_URL = 'https://yarngpt.ai/api/vl/tts'
#  why because yangGPT is an external service not given by langchain, so we need to load the API key from the environment variables

@tool
def text_to_speech(text:str, voice:str="Emma", response_formate:str="mp3")->str:
    """
    Generate Nigerian-acented speech via yarnGPT hosted API. Returns path to audio file
    """
    headre={"Author"}
    payloads={
        "text": text,
        "voice": voice,
        "response_format": response_formate
    }
    reponse=requests.post(API_URL, header=header, json=payloads, stream=True, timeout=60)
    if reponse.status_code!=200:
        raise RuntimeError[f"yarnGPT API error: {reponse.text}"]
    # if we have something back we create a folder and store thr output there
    os.makedirs("generated_audio", exist_ok=True) 
    path=f"generated_audio/output.{response_formate}"  
    with open(path, 'wb') as f:
        for chunk in reponse.iter_content(chunk_size=8192):
            f.write(chunk)
            return path 