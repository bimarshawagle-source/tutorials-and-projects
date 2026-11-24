from openai import OpenAI
client = OpenAI(api_key = "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")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
    
        {"role": "user", "content": "What is the capital of France?"}
    ],
)
print(response.choices[0].message.content)