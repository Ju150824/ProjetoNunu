from datetime import datetime

from vida import registrar_evento


FORMATO_DATA = "%Y-%m-%d %H:%M:%S"


def garantir_evolucao(dados):
    if "evolucao" not in dados:
        dados["evolucao"] = {
            "nivel": 1,
            "xp": 0,
            "xp_proximo_nivel": 100,
            "fase": "recém-adotado",
            "data_nascimento": datetime.now().strftime(FORMATO_DATA)
        }

    evolucao = dados["evolucao"]

    if "nivel" not in evolucao:
        evolucao["nivel"] = 1

    if "xp" not in evolucao:
        evolucao["xp"] = 0

    if "xp_proximo_nivel" not in evolucao:
        evolucao["xp_proximo_nivel"] = 100

    if "fase" not in evolucao:
        evolucao["fase"] = "recém-adotado"

    if "data_nascimento" not in evolucao:
        evolucao["data_nascimento"] = datetime.now().strftime(FORMATO_DATA)


def calcular_dias_de_vida(dados):
    garantir_evolucao(dados)

    data_nascimento = dados["evolucao"].get("data_nascimento", "")

    try:
        nascimento = datetime.strptime(data_nascimento, FORMATO_DATA)
    except ValueError:
        return 0

    diferenca = datetime.now() - nascimento

    return max(diferenca.days, 0)


def definir_fase(dados):
    garantir_evolucao(dados)

    nivel = dados["evolucao"]["nivel"]
    apego = dados["estado"].get("apego", 0)
    curiosidade = dados["estado"].get("curiosidade", 0)
    personalidade = dados.get("personalidade", {})

    carinhoso = personalidade.get("carinhoso", 0)
    brincalhao = personalidade.get("brincalhao", 0)
    dramatico = personalidade.get("dramatico", 0)
    carente = personalidade.get("carente", 0)

    if nivel <= 1:
        fase = "recém-adotado"
    elif nivel <= 3:
        fase = "aprendiz de companheiro"
    elif nivel <= 5 and curiosidade >= 70:
        fase = "companheiro curioso"
    elif nivel <= 5 and carinhoso >= 80:
        fase = "companheiro carinhoso"
    elif nivel <= 7 and brincalhao >= 75:
        fase = "amiguinho brincalhão"
    elif nivel <= 7 and carente >= 75:
        fase = "amiguinho apegado"
    elif dramatico >= 80:
        fase = "pequeno dramático"
    elif apego >= 85 and nivel >= 8:
        fase = "melhor amigo virtual"
    elif nivel >= 10:
        fase = "companheiro evoluído"
    else:
        fase = "companheiro em crescimento"

    dados["evolucao"]["fase"] = fase


def ganhar_xp(dados, quantidade, motivo="interação"):
    garantir_evolucao(dados)

    if quantidade <= 0:
        return

    evolucao = dados["evolucao"]

    evolucao["xp"] += quantidade

    subiu_nivel = False

    while evolucao["xp"] >= evolucao["xp_proximo_nivel"]:
        evolucao["xp"] -= evolucao["xp_proximo_nivel"]
        evolucao["nivel"] += 1
        evolucao["xp_proximo_nivel"] += 25
        subiu_nivel = True

    definir_fase(dados)

    if subiu_nivel:
        nome = dados["pet"]["nome"]
        registrar_evento(
            dados,
            f"{nome} subiu para o nível {evolucao['nivel']}."
        )

        print(f"{nome}: Eu senti algo mudando aqui dentro...")
        print(f"{nome}: Acho que evoluí para o nível {evolucao['nivel']}!")
        print(f"{nome}: Minha fase agora é: {evolucao['fase']}.")


def mostrar_evolucao(dados):
    garantir_evolucao(dados)
    definir_fase(dados)

    nome = dados["pet"]["nome"]
    evolucao = dados["evolucao"]
    dias_de_vida = calcular_dias_de_vida(dados)

    print(f"\n--- Evolução do {nome} ---")
    print(f"Nível: {evolucao['nivel']}")
    print(f"XP: {evolucao['xp']}/{evolucao['xp_proximo_nivel']}")
    print(f"Fase: {evolucao['fase']}")
    print(f"Dias de vida: {dias_de_vida}")
    print("--------------------------\n")