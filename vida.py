from datetime import datetime


FORMATO_DATA = "%Y-%m-%d %H:%M:%S"


def agora_formatado():
    return datetime.now().strftime(FORMATO_DATA)


def limitar_estado(dados):
    for chave in dados["estado"]:
        if dados["estado"][chave] < 0:
            dados["estado"][chave] = 0
        elif dados["estado"][chave] > 100:
            dados["estado"][chave] = 100


def registrar_evento(dados, evento):
    if "historico" not in dados:
        dados["historico"] = []

    dados["historico"].append({
        "data": agora_formatado(),
        "evento": evento
    })

    dados["historico"] = dados["historico"][-20:]


def registrar_interacao(dados):
    if "sistema" not in dados:
        dados["sistema"] = {}

    dados["sistema"]["ultimo_acesso"] = agora_formatado()
    dados["sistema"]["total_interacoes"] = dados["sistema"].get("total_interacoes", 0) + 1


def calcular_minutos_ausente(dados):
    ultimo_acesso = dados.get("sistema", {}).get("ultimo_acesso", "")

    if not ultimo_acesso:
        return 0

    try:
        data_ultimo_acesso = datetime.strptime(ultimo_acesso, FORMATO_DATA)
    except ValueError:
        return 0

    diferenca = datetime.now() - data_ultimo_acesso
    minutos = int(diferenca.total_seconds() // 60)

    if minutos < 0:
        return 0

    return minutos


def texto_tempo(minutos):
    if minutos < 60:
        return f"{minutos} minuto(s)"

    horas = minutos // 60

    if horas < 24:
        return f"{horas} hora(s)"

    dias = horas // 24
    return f"{dias} dia(s)"


def aplicar_ausencia(dados):
    nome = dados["pet"]["nome"]
    estado = dados["estado"]
    modo = dados["pet"].get("modo", "acordado")

    minutos = calcular_minutos_ausente(dados)

    if minutos < 5:
        return

    ciclos = minutos // 10

    if ciclos < 1:
        ciclos = 1

    if ciclos > 72:
        ciclos = 72

    if modo == "dormindo":
        estado["energia"] += ciclos * 3
        estado["sono"] -= ciclos * 3
        estado["fome"] += ciclos

        if estado["energia"] >= 90 or estado["sono"] <= 10:
            dados["pet"]["modo"] = "acordado"
            estado["humor"] += 5
            registrar_evento(dados, "Nunu acordou sozinho depois de descansar.")

            limitar_estado(dados)

            print(f"{nome}: Eu acordei enquanto você estava fora. Acho que descansei bastante.")
            print(f"{nome}: Você ficou longe por {texto_tempo(minutos)}.")
            return

        limitar_estado(dados)

        print(f"{nome}: zzz... eu continuei dormindo enquanto você estava fora.")
        print(f"{nome}: Passaram {texto_tempo(minutos)} desde a última vez.")
        return

    estado["fome"] += ciclos * 2
    estado["sono"] += ciclos
    estado["energia"] -= ciclos

    if minutos >= 60:
        estado["humor"] -= 4

    if minutos >= 360:
        estado["humor"] -= 8
        estado["apego"] += 3

    if minutos >= 1440:
        estado["humor"] -= 12
        estado["apego"] += 5

    limitar_estado(dados)

    registrar_evento(dados, f"Nunu percebeu uma ausência de {texto_tempo(minutos)}.")

    if minutos < 60:
        print(f"{nome}: Você ficou fora por {texto_tempo(minutos)}. Eu percebi.")
    elif minutos < 360:
        print(f"{nome}: Você demorou {texto_tempo(minutos)} para voltar. Eu fiquei esperando.")
    elif minutos < 1440:
        print(f"{nome}: Você sumiu por {texto_tempo(minutos)}... tentei não ficar dramático.")
    else:
        print(f"{nome}: Faz {texto_tempo(minutos)} que você não aparece. Eu senti sua falta.")