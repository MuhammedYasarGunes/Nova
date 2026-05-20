import ollama

class LLM:
    def __init__(self, model="qwen2.5:7b"):
        self.model = model

    def generate(self, prompt):
        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]