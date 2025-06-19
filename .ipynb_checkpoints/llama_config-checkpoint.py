# llama_config.py
import os
from together import Together

# Recommended: use environment variable (secure)
os.environ["TOGETHER_API_KEY"] = "together_ai_api_key"

client = Together()

def ask_llama(prompt):
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",  # or Llama-3-8B-Instruct
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
