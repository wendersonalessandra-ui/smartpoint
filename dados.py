import os
import json
CAMINHO_JSON = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "funcionarios.json"
)
def carregar_json():
    if os.path.exists(CAMINHO_JSON):
        with open(CAMINHO_JSON, "r", encoding="utf-8") as ficheiro:
            try:
                return json.load(ficheiro)
            except json.JSONDecodeError:
                return []

    return []
def guardar_json(funcionarios):
    with open(CAMINHO_JSON, "w", encoding="utf-8") as ficheiro:
        json.dump(
            funcionarios,
            ficheiro,
            ensure_ascii=False,
            indent=4
        )