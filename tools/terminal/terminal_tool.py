import subprocess

from tools.base_tool import BaseTool

class TerminalTool(BaseTool):

    name = "terminal"

    description = """
    Executes terminal commands
    """

    def run(self, command):

        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        return {
            "stdout": result.stdout,
            "stderr": result.stderr
        }