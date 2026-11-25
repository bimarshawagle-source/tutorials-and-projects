from fastapi import FastAPI
import ollama

app = FastAPI()

@app.post("/generate")
def generate(prompt:str):
    response = ollama.chat(
        model="gemma4:12",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates CadQuery code."},
            {"role": "user", "content": f"Create a 3D model for: {prompt}"},
        ],
        options={"temperature": 0.2},
    )
    content = response["message"]["content"]
    return {"cadquery_code": content}