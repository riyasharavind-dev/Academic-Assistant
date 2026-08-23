Yes bro. ✅ The **`Academic-Assistant` GitHub repository exists and is currently empty**, so it's ready for this project.

Because you want it in the **same local `Chat-Bot` folder but as a different GitHub repo**, we should not change the project files again. We just need a separate Git history/remote for Academic Assistant.

Your local folder currently has the Banking Assistant Git history, so the cleanest approach is to create the Academic repo from the same files with a **separate Git directory**.

### First, create the Academic README

Save this as:

```text
README.md
```

inside the `Chat-Bot` folder, replacing the Banking README.

````markdown
# Academic Assistant

An AI-powered academic learning assistant designed to help students understand concepts, solve problems, prepare for examinations, revise topics, and improve programming skills through natural conversation.

## Overview

**Academic Assistant** is a domain-specific educational chatbot powered by Google Gemini and a FastAPI backend.

The system is designed around a learning-first approach. Instead of focusing only on giving answers, it helps students understand concepts, reasoning, problem-solving methods, and study strategies.

## Features

### 📚 Academic Learning

- Explain difficult concepts in simple language
- Subject and topic explanations
- Definitions and terminology
- Concept comparisons
- Real-world examples

### 📝 Exam Preparation

- Exam revision support
- Study planning
- Important topic explanations
- Practice questions
- Step-by-step problem solving

### 💻 Programming Support

- Programming concept explanations
- Code debugging
- Error identification
- Step-by-step programming explanations
- AI, Data Science, and Computer Science fundamentals

### 📋 Study Support

- Revision notes
- Topic summaries
- Practice questions
- Learning strategies
- Structured explanations

### 🧠 Context-Aware Conversations

The assistant receives the conversation history from the frontend, allowing follow-up questions and continuous discussion around the same academic topic.

## Architecture

```text
                    Academic Assistant
                           │
                           ▼
                 ┌─────────────────────┐
                 │      Frontend       │
                 │    HTML / CSS / JS  │
                 │      Port 5000      │
                 └──────────┬──────────┘
                            │
                         POST /chat
                            │
                            ▼
                 ┌─────────────────────┐
                 │       FastAPI       │
                 │       Backend       │
                 │      Port 8000      │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │    Google Gemini   │
                 │        API          │
                 └─────────────────────┘
````

## Technology Stack

| Component              | Technology            |
| ---------------------- | --------------------- |
| Frontend               | HTML, CSS, JavaScript |
| Backend                | Python                |
| API Framework          | FastAPI               |
| Server                 | Uvicorn               |
| AI                     | Google Gemini         |
| Data Validation        | Pydantic              |
| Environment Management | python-dotenv         |

## Project Structure

```text
Academic-Assistant/
│
├── index.html
├── main.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── .env              # Local only
└── .venv/            # Local only
```

## How It Works

1. The student opens the Academic Assistant frontend.
2. The student enters an academic question.
3. The frontend stores the conversation history.
4. The frontend sends the conversation to the FastAPI backend.
5. FastAPI validates the request.
6. The backend sends the conversation together with the academic system prompt to Gemini.
7. Gemini generates an academic-focused response.
8. FastAPI returns the response.
9. The frontend displays the response in the conversation.

## Running the Project

### Backend

The backend runs on port `8000`.

```powershell
.\.venv\Scripts\Activate.ps1
python main.py
```

Backend URL:

```text
http://127.0.0.1:8000
```

Health check:

```text
http://127.0.0.1:8000/health
```

### Frontend

The frontend runs on port `5000`.

```powershell
python -m http.server 5000
```

Frontend URL:

```text
http://127.0.0.1:5000
```

## API Endpoints

### `GET /`

Returns basic information about the Academic Assistant backend.

### `GET /health`

Returns the health status of the service.

### `POST /chat`

Accepts the current conversation and returns an AI-generated academic response.

Example request:

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Explain artificial intelligence in simple terms."
    }
  ]
}
```

Example response:

```json
{
  "response": "Artificial intelligence is..."
}
```

## Environment Variables

Create a local `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=your_gemini_model
```

Never publish `.env` to GitHub.

## Academic Safety

Academic Assistant follows a learning-focused approach.

It should:

* Explain reasoning and concepts
* Avoid deliberately encouraging plagiarism
* Encourage independent understanding
* Clearly state uncertainty when necessary
* Avoid inventing academic facts
* Never claim that code was executed unless it was actually executed
* Keep explanations appropriate to the student's question

## Privacy

The application should not request sensitive authentication information such as:

* Passwords
* OTPs
* API keys
* Authentication tokens

The Gemini API key must remain in the local `.env` file.

## Future Improvements

Possible future features include:

* Persistent study history
* Subject-specific AI modes
* Voice-based learning
* Quiz and assessment mode
* Automatic study-plan generation
* PDF and document learning
* Multi-language support
* Progress tracking
* Personalized revision
* Educational resource integration


## Project

**Academic Assistant**

A focused AI learning companion designed to help students understand more, practice better, and study smarter.

```

