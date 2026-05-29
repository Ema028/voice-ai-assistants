# Voice AI Assistants

Python-based speech AI assistants using Whisper, OpenAI, and Groq APIs.

This repository contains two independent voice-focused AI applications built around speech processing and conversational LLM pipelines.

## Projects

### 1. Telegram Audio Bot

A Telegram bot for receiving voice messages and transcribing audio.

#### Features

* Receives voice messages through Telegram Bot API
* Downloads and processes audio files
* Splits long audio into manageable chunks
* Uses Whisper API for speech-to-text transcription
* Returns transcribed text to the user

#### Stack

* Python
* Telegram Bot API
* Whisper API
* Audio processing
* Python-dotenv

---

### 2. Local Voice Assistant

A local voice assistant that continuously listens through the microphone, processes speech, and responds with synthesized audio.

#### Features

* Microphone input
* Speech-to-text transcription
* LLM response generation
* Text-to-speech playback
* Supports OpenAI and Groq models

#### Stack

* Python
* Whisper API
* OpenAI API
* Groq API
* STT / TTS

---

## Repository Structure

```bash
voice-ai-assistants/
├── telegram-bot/
├── local-assistant/
├── requirements.txt
└── README.md
```

## Workflow

### Telegram Bot

Audio Message → Processing → Whisper STT → Transcribed Text

### Local Voice Assistant

Microphone → Speech-to-Text → LLM → Text-to-Speech → Audio Response

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/voice-ai-assistants.git
cd voice-ai-assistants
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENAI_API_KEY=your_key
GROQ_API_KEY=your_key
TELEGRAM_BOT_TOKEN=your_token
```

## Purpose

This project was built to explore practical voice AI pipelines using:

* Speech-to-text
* LLM-based conversational processing
* Text-to-speech
* API integration
* Real-time interaction

## Future Improvements

* Streaming transcription
* Better conversation memory
* Voice activity detection
* Docker setup
* Improved audio pipeline performance

