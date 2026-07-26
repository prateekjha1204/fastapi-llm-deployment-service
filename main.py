from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import time

app = FastAPI(
    title="Quantized LLM Inference API",
    description="High-throughput asynchronous REST API for serving local LLMs.",
    version="1.0.0"
)

class GenerationRequest(BaseModel):
    prompt: str = Field(..., example="What is model quantization?")
    max_tokens: int = Field(default=128, ge=1, le=512)
    temperature: float = Field(default=0.7, ge=0.0, le=1.0)

class GenerationResponse(BaseModel):
    prompt: str
    generated_text: str
    tokens_generated: int
    latency_ms: float

@app.get("/")
def health_check():
    return {
        "status": "healthy",
        "service": "LLM Serving Engine",
        "model_loaded": "TinyLlama-1.1B-Quantized"
    }

@app.post("/generate", response_model=GenerationResponse)
async def generate_text(request: GenerationRequest):
    start_time = time.time()
    
    if not request.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt cannot be empty.")
    
    # Simulated model output for lightweight API demonstration
    simulated_output = (
        f"[Model Output] Response to: '{request.prompt}'. "
        f"Quantized inference executed successfully across {request.max_tokens} target tokens."
    )
    
    latency = round((time.time() - start_time) * 1000, 2)
    
    return GenerationResponse(
        prompt=request.prompt,
        generated_text=simulated_output,
        tokens_generated=request.max_tokens,
        latency_ms=latency
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)