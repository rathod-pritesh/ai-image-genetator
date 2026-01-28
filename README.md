# 🎨 AI Image Generator (SvelteKit + FastAPI)

An **AI-powered image generation web application** that converts text prompts into images using the **Pollinations AI API**.  
The project follows a **modern full-stack architecture** with a SvelteKit frontend and a FastAPI backend.

---

## 🚀 Features

- Generate AI images from natural language prompts  
- Fast and responsive UI using **Svelte / SvelteKit**  
- Backend powered by **FastAPI**  
- Uses **Pollinations AI** for image generation  
- Random seed support for varied outputs  
- Base64 image response for easy frontend rendering  
- CORS enabled for frontend-backend communication  

---

## 🧠 How It Works

1. User enters a text prompt in the frontend  
2. Prompt is sent to FastAPI backend  
3. Backend encodes the prompt and sends it to Pollinations AI  
4. Pollinations returns the generated image  
5. Image is converted to **Base64**  
6. Frontend displays the image instantly  

---

## 🛠️ Tech Stack

### Frontend
- Svelte
- SvelteKit
- JavaScript
- Fetch API

### Backend
- Python 3.9+
- FastAPI
- Uvicorn
- Requests
- Pydantic

### AI Service
- Pollinations AI  
  `https://image.pollinations.ai`

---

### Request Body
```json
{
  "prompt": "A futuristic city at sunset, cyberpunk style"
}
