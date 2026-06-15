import json
import os

ARQUIVO_DADOS = "dados.json"


def dados_padrao():
    return {
        "pet": {
            "nome": "Nunu",
            "versao": "0.4"
        },
        "usuario": {
            "nome": "",
            "apelido": "",
            "interesses": [],
            "preferencias": []
        },
        "estado": {
            "humor": 70,
            "energia": 80,
            "fome": 30,
            "apego": 50,
            "curiosidade": 60,
            "sono": 20
        },
        "personalidade": {
            "carinhoso": 85,
            "curioso": 75,
            "brincalhao": 60,
            "dramatico": 55,
            "timido": 35
        },
        "memorias": []
    }


def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    return dados_padrao()


def salvar_dados(dados):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)