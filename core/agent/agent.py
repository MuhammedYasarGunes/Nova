from core.planner.planner import Planner
from tools.tool_registry import TOOLS
from core.memory.memory_manager import MemoryManager
from core.llm.llm import LLM

class Agent:

    def __init__(self):
        self.planner = Planner()
        self.memory = MemoryManager()
        self.llm = LLM()

    def run(self, user_input):

        self.memory.remember(user_input)

        recalled = self.memory.recall(user_input)

        plan = self.planner.route(user_input)

        tool = plan.get("tool")

        if tool and tool != "none":

            result = TOOLS[tool].run(plan.get("input"))

            # TOOL sonucu → LLM'e yorumlat
            prompt = f"""
Aşağıdaki tool çıktısını kullanıcıya açıkla:

Tool sonucu:
{result}

Kullanıcı bağlamı:
{recalled}
"""

            return self.llm.generate(prompt)

        # normal chat
        prompt = f"""
Kullanıcı ile konuş.

Bağlam:
{recalled}

Kullanıcı:
{user_input}
"""

        return self.llm.generate(prompt)