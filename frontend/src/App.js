import React, { useState } from "react";

function App() {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    if (!prompt) return;
    setLoading(true);
    try {
      const res = await fetch("http://localhost:8000/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt, max_tokens: 128 }),
      });
      const data = await res.json();
      setResponse(data.generated_text);
    } catch (err) {
      setResponse("Error connecting to LLM backend service.");
    }
    setLoading(false);
  };

  return (
    <div
      style={{
        padding: "40px",
        fontFamily: "sans-serif",
        maxWidth: "600px",
        margin: "auto",
      }}
    >
      <h2>⚡ Quantized LLM Playground</h2>
      <textarea
        rows="4"
        style={{ width: "100%", padding: "10px" }}
        placeholder="Enter your prompt here..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />
      <button
        onClick={handleGenerate}
        style={{ padding: "10px 20px", marginTop: "10px", cursor: "pointer" }}
      >
        {loading ? "Generating..." : "Submit Prompt"}
      </button>
      {response && (
        <div
          style={{
            marginTop: "20px",
            padding: "15px",
            background: "#f4f4f4",
            borderRadius: "5px",
          }}
        >
          <strong>Model Output:</strong>
          <p>{response}</p>
        </div>
      )}
    </div>
  );
}

export default App;
