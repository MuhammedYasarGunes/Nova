import subprocess

from tools.base_tool import BaseTool

class TerminalTool(BaseTool):

    name = "terminal"

    description = """
    Executes terminal commands
    """

    def run(self, command):

        if not command:
            return {"stdout": "", "stderr": "Çalıştırılacak komut yok"}

        # Komutu LLM seçiyor; çalıştırmadan önce kullanıcı onayı şart.
        answer = input(f"\nÇalıştırılacak komut: {command}\nOnaylıyor musun? [e/H] ")
        if answer.strip().lower() not in ("e", "evet", "y", "yes"):
            return {"stdout": "", "stderr": "Kullanıcı komutu onaylamadı"}

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
