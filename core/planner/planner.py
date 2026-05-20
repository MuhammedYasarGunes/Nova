import json
from core.llm.llm import LLM
from core.planner.tool_schema import TOOL_SCHEMA

class Planner:

    def __init__(self):
        self.llm = LLM()

    def route(self, user_input):

        prompt = f"""
{TOOL_SCHEMA}

Kullanıcı isteği:
{user_input}
"""

        response = self.llm.generate(prompt)

        try:
            return json.loads(response)

        except Exception:
            return {
                "tool": "none",
                "input": None
            }