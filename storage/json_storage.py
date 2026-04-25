import json
import os


class JsonStorage:
    def __init__(self, file_path):
        self.file_path = file_path

    def carregar(self):
        if not os.path.exists(self.file_path):
            return {}

        with open(self.file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def salvar(self, dados):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4)