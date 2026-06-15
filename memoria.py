import json
import os

ARQUIVO_DADOS = "dados.json"


def carregar_pet():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    return {
        "nome": "Nunu",
        "humor": 70,
        "energia": 80,
        "fome": 30,
        "apego": 50
    }


def salvar_pet(pet):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(pet, arquivo, indent=4, ensure_ascii=False)