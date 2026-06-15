import json
import os

ARQUIVO_DADOS = "dados.json"


def dados_padrao():
    return {
        "pet": {
            "nome": "Nunu",
            "versao": "0.7",
            "modo": "acordado"
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
        "memorias": [],
        "historico": [],
        "sistema": {
            "ultimo_acesso": "",
            "total_interacoes": 0
        }
    }


def mesclar_dados(padrao, dados_salvos):
    for chave, valor_padrao in padrao.items():
        if chave not in dados_salvos:
            dados_salvos[chave] = valor_padrao
        elif isinstance(valor_padrao, dict) and isinstance(dados_salvos[chave], dict):
            mesclar_dados(valor_padrao, dados_salvos[chave])

    return dados_salvos


def carregar_dados():
    padrao = dados_padrao()

    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        dados = mesclar_dados(padrao, dados)
        dados["pet"]["versao"] = "0.7"

        return dados

    return padrao


def salvar_dados(dados):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)