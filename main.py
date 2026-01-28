from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import urllib.parse
import random
import requests
import base64
import time

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_methods=["*"],
  allow_headers=["*"],
)

class PromptRequest(BaseModel):
  prompt: str

@app.post("/generate-image")
def generate_image(data: PromptRequest):
  print("➡ Prompt received:", data.prompt)

  encoded_prompt = urllib.parse.quote(data.prompt)
  seed = random.randint(1, 999999)

  url = (
    f"https://image.pollinations.ai/prompt/{encoded_prompt}"
    f"?width=768&height=768"
    f"&seed={seed}"
    f"&nocache=true"
  )

  print("➡ Fetching image from Pollinations...")
  start = time.time()

  try: 
    response = requests.get(url, timeout=60)
    response.raise_for_status()
  except requests.exceptions.Timeout:
    print("❌ Pollinations timeout")
    raise HTTPException(status_code=504, detail="Image generation timed out")
  except Exception as e:
    print("❌ Error:", e)
    raise HTTPException(status_code=500, detail="Image generation failed")
  
  print(f"✅ Image fetched in {time.time() - start:.2f}s")

  img_base64 = base64.b64encode(response.content).decode("utf-8")

  return {
    "image_base64": img_base64
  }