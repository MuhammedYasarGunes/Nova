class BaseTool:
    name = ""
    description = ""

    def run(self, input_data):
        raise NotImplementedError