def limitar_personalidade(dados):
    for traco in dados["personalidade"]:
        if dados["personalidade"][traco] < 0:
            dados["personalidade"][traco] = 0
        elif dados["personalidade"][traco] > 100:
            dados["personalidade"][traco] = 100


def ajustar_traco(dados, traco, valor):
    if traco not in dados["personalidade"]:
        dados["personalidade"][traco] = 50

    dados["personalidade"][traco] += valor
    limitar_personalidade(dados)


def evoluir_por_evento(dados, evento):
    if evento == "carinho":
        ajustar_traco(dados, "carinhoso", 2)
        ajustar_traco(dados, "carente", 1)
        ajustar_traco(dados, "timido", -1)

    elif evento == "comer":
        ajustar_traco(dados, "carinhoso", 1)
        ajustar_traco(dados, "dramatico", -1)

    elif evento == "brincar":
        ajustar_traco(dados, "brincalhao", 2)
        ajustar_traco(dados, "curioso", 1)
        ajustar_traco(dados, "timido", -1)

    elif evento == "dormir":
        ajustar_traco(dados, "dramatico", -1)

    elif evento == "acordar":
        ajustar_traco(dados, "curioso", 1)

    elif evento == "lembrar":
        ajustar_traco(dados, "curioso", 2)
        ajustar_traco(dados, "carinhoso", 1)

    elif evento == "conversa_emocional":
        ajustar_traco(dados, "carinhoso", 2)
        ajustar_traco(dados, "carente", 1)

    elif evento == "elogio":
        ajustar_traco(dados, "carinhoso", 1)
        ajustar_traco(dados, "brincalhao", 1)

    elif evento == "ausencia":
        ajustar_traco(dados, "dramatico", 2)
        ajustar_traco(dados, "carente", 2)

    elif evento == "muita_ausencia":
        ajustar_traco(dados, "dramatico", 4)
        ajustar_traco(dados, "carente", 4)
        ajustar_traco(dados, "timido", 1)


def tracos_ordenados(dados):
    personalidade = dados["personalidade"]

    return sorted(
        personalidade.items(),
        key=lambda item: item[1],
        reverse=True
    )


def gerar_descricao_personalidade(dados):
    principais = tracos_ordenados(dados)[:3]
    nomes = [traco for traco, valor in principais]

    if "carinhoso" in nomes and "carente" in nomes:
        return "Estou ficando bem apegado e gosto quando recebo atenção."

    if "curioso" in nomes and "brincalhao" in nomes:
        return "Acho que estou me tornando curioso e brincalhão."

    if "dramatico" in nomes:
        return "Talvez eu esteja ficando um pouco dramático... mas só um pouquinho."

    if "timido" in nomes:
        return "Eu ainda sou meio tímido, mas estou tentando confiar mais."

    if "carinhoso" in nomes:
        return "Acho que estou me tornando um pet bem carinhoso."

    return "Minha personalidade ainda está se formando aos poucos."


def mostrar_personalidade(dados):
    nome = dados["pet"]["nome"]
    personalidade = dados["personalidade"]

    print(f"\n--- Personalidade do {nome} ---")
    print(f"Carinhoso: {personalidade['carinhoso']}/100")
    print(f"Curioso: {personalidade['curioso']}/100")
    print(f"Brincalhão: {personalidade['brincalhao']}/100")
    print(f"Dramático: {personalidade['dramatico']}/100")
    print(f"Tímido: {personalidade['timido']}/100")
    print(f"Carente: {personalidade['carente']}/100")
    print("-------------------------------")
    print(f"{nome}: {gerar_descricao_personalidade(dados)}\n")


def mostrar_perfil(dados):
    nome = dados["pet"]["nome"]
    usuario = dados["usuario"]["apelido"] or dados["usuario"]["nome"]
    modo = dados["pet"].get("modo", "acordado")
    personalidade = tracos_ordenados(dados)
    principais = personalidade[:3]

    print(f"\n--- Perfil do {nome} ---")
    print(f"Nome: {nome}")
    print(f"Modo atual: {modo}")

    if usuario:
        print(f"Pessoa vinculada: {usuario}")
    else:
        print("Pessoa vinculada: ainda não fui adotado")

    print("Traços principais:")

    for traco, valor in principais:
        print(f"- {traco}: {valor}/100")

    print(f"Descrição: {gerar_descricao_personalidade(dados)}")
    print("-----------------------\n")