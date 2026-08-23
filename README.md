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