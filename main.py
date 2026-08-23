import os
from typing import List, Literal

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from google import genai
from google.genai import types

from config import SYSTEM_PROMPT


# ============================================================
# ENVIRONMENT
# ============================================================

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL")

if not GEMINI_API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is missing. Add it to your .env file."
    )

if not GEMINI_MODEL:
    raise RuntimeError(
        "GEMINI_MODEL is missing. Add it to your .env file."
    )


# ============================================================
# GEMINI CLIENT
# ============================================================

client = genai.Client(
    api_key=GEMINI_API_KEY
)


# ============================================================
# FASTAPI
# ============================================================

app = FastAPI(
    title="Banking Assistant",
    description="Banking and financial-service information assistant powered by Gemini.",
    version="1.0.0"
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5000",
        "http://localhost:5000"
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"]
)


# ============================================================
# DATA MODELS
# ============================================================

class ChatMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str = Field(
        ...,
        min_length=1,
        max_length=20000
    )


class ChatRequest(BaseModel):
    messages: List[ChatMessage] = Field(
        ...,
        min_length=1,
        max_length=100
    )


class ChatResponse(BaseModel):
    response: str


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/")
async def root():
    return {
        "status": "online",
        "service": "Banking Assistant",
        "model": GEMINI_MODEL
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }


# ============================================================
# CHAT
# ============================================================

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    try:

        contents = []

        for message in request.messages:

            text = message.content.strip()

            if not text:
                continue

            gemini_role = (
                "user"
                if message.role == "user"
                else "model"
            )

            contents.append(
                types.Content(
                    role=gemini_role,
                    parts=[
                        types.Part(
                            text=text
                        )
                    ]
                )
            )

        if not contents:
            raise HTTPException(
                status_code=400,
                detail="No valid messages were provided."
            )

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=0.7,
                max_output_tokens=4096
            )
        )

        generated_text = response.text

        if not generated_text:
            raise HTTPException(
                status_code=502,
                detail="Gemini returned an empty response."
            )

        return ChatResponse(
            response=generated_text.strip()
        )

    except HTTPException:
        raise

    except Exception as exc:

        print(f"Gemini API error: {exc}")

        raise HTTPException(
            status_code=500,
            detail="Unable to generate a response right now."
        )


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )