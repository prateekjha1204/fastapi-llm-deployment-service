# Scalable Quantized LLM Inference API

An asynchronous REST API built with **FastAPI** to serve quantized local Large Language Models with health monitoring, structured schema validation, and Docker containerization.

## Tech Stack

- **Frameworks:** Python, FastAPI, Uvicorn, Pydantic, Docker.

## Features

- **Async Endpoints:** Low-latency response handling.
- **Request Validation:** Input sanitization using Pydantic schemas.
- **Containerized:** Dockerfile included for quick container execution.

## How to Run Locally

### 1. Python Direct Run

```bash
pip install -r requirements.txt
python main.py
```
