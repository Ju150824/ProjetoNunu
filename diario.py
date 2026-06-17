import re
import unicodedata
from datetime import datetime

from vida import registrar_evento
from personalidade import evoluir_por_evento


FORMATO_DATA = "%Y-%m-%d %H:%M:%S"


def agora_formatado():
    return datetime.now().strftime(FORMATO_DATA)


def normalizar(texto):
    texto = texto.strip().lower()

    texto_sem_acento = unicodedata.normalize("NFD", texto)
    texto_sem_acento = "".join(
        caractere for caractere in texto_sem_acento
        if unicodedata.category(caractere) != "Mn"
    )

    texto_sem_acento = re.sub(r"[^a-z0-9\s]", " ", texto_sem_acento)
    texto_sem_acento = re.sub(r"\s+", " ", texto_sem_acento)

    return texto_sem_acento.strip()


def analisar_sentimento(texto):
    texto_normalizado = normalizar(texto)

    palavras_positivas = [
        "feliz",
        "bem",
        "otimo",
        "otima",
        "bom",
        "boa",
        "consegui",
        "alegre",
        "animado",
        "animada",
        "orgulhoso",
        "orgulhosa",
        "calmo",
        "calma",
        "tranquilo",
        "tranquila",
        "esperancoso",
        "esperancosa"
    ]

    palavras_negativas = [
        "triste",
        "ruim",
        "dificil",
        "cansado",
        "cansada",
        "exausto",
        "exausta",
        "ansioso",
        "ansiosa",
        "medo",
        "raiva",
        "chorei",
        "chorar",
        "desanimei",
        "sobrecarregado",
        "sobrecarregada",
        "estresse",
        "estressado",
        "estressada"
    ]

    pontos_positivos = 0
    pontos_negativos = 0

    for palavra in palavras_positivas:
        if palavra in texto_normalizado:
            pontos_positivos += 1

    for palavra in palavras_negativas:
        if palavra in texto_normalizado:
            pontos_negativos += 1

    if pontos_positivos > pontos_negativos:
        return "positivo"

    if pontos_negativos > pontos_positivos:
        return "negativo"

    return "neutro"


def limpar_texto_diario(texto):
    texto = texto.strip()

    gatilhos = [
        "diario ",
        "diário ",
        "registrar diario ",
        "registrar diário ",
        "hoje eu ",
        "hoje foi ",
        "estou me sentindo ",
        "me sinto "
    ]

    texto_normalizado = normalizar(texto)

    for gatilho in gatilhos:
        gatilho_normalizado = normalizar(gatilho)

        if texto_normalizado.startswith(gatilho_normalizado):
            tamanho = len(gatilho)
            return texto[tamanho:].strip()

    return texto


def registrar_diario(dados, texto):
    nome = dados["pet"]["nome"]

    if "diario" not in dados:
        dados["diario"] = []

    texto_limpo = limpar_texto_diario(texto)

    if texto_limpo == "":
        print(f"{nome}: Me conta como você está se sentindo ou como foi seu dia.")
        print(f"{nome}: Exemplo: hoje foi um dia difícil")
        return

    sentimento = analisar_sentimento(texto_limpo)

    entrada = {
        "id": len(dados["diario"]) + 1,
        "data": agora_formatado(),
        "texto": texto_limpo,
        "sentimento": sentimento
    }

    dados["diario"].append(entrada)
    dados["diario"] = dados["diario"][-50:]

    if sentimento == "positivo":
        dados["estado"]["humor"] += 5
        dados["estado"]["apego"] += 2

        print(f"{nome}: Gostei de guardar isso. Parece que teve algo bom aí.")
        print(f"{nome}: Vou lembrar desse pedacinho feliz com você.")

    elif sentimento == "negativo":
        dados["estado"]["apego"] += 4
        dados["estado"]["humor"] -= 1

        print(f"{nome}: Eu guardei isso com cuidado.")
        print(f"{nome}: Não sei resolver tudo, mas posso ficar aqui com você um pouquinho.")

    else:
        dados["estado"]["curiosidade"] += 2
        dados["estado"]["apego"] += 1

        print(f"{nome}: Tá guardado no nosso diário.")
        print(f"{nome}: Obrigado por me contar.")

    evoluir_por_evento(dados, "conversa_emocional")
    registrar_evento(dados, f"Nunu registrou uma entrada no diário emocional: {sentimento}.")


def listar_diario(dados):
    nome = dados["pet"]["nome"]
    diario = dados.get("diario", [])

    if not diario:
        print(f"{nome}: Nosso diário ainda está vazio.")
        print(f"{nome}: Você pode começar dizendo: hoje foi um dia difícil")
        return

    print(f"\n--- Diário emocional do {nome} ---")

    for entrada in diario[-10:]:
        print(f"{entrada['id']}. [{entrada['sentimento']}] {entrada['data']}")
        print(f"   {entrada['texto']}")

    print("---------------------------------\n")


def resumo_diario(dados):
    nome = dados["pet"]["nome"]
    diario = dados.get("diario", [])

    if not diario:
        print(f"{nome}: Ainda não tenho registros suficientes para resumir.")
        return

    ultimos = diario[-10:]

    positivos = sum(1 for entrada in ultimos if entrada["sentimento"] == "positivo")
    negativos = sum(1 for entrada in ultimos if entrada["sentimento"] == "negativo")
    neutros = sum(1 for entrada in ultimos if entrada["sentimento"] == "neutro")

    print(f"\n--- Resumo emocional do {nome} ---")
    print(f"Registros analisados: {len(ultimos)}")
    print(f"Positivos: {positivos}")
    print(f"Negativos: {negativos}")
    print(f"Neutros: {neutros}")

    if positivos > negativos and positivos > neutros:
        print(f"{nome}: Pelos últimos registros, parece que você tem vivido momentos bons.")
    elif negativos > positivos and negativos > neutros:
        print(f"{nome}: Percebi que os últimos registros parecem pesados. Vou ficar mais atento a você.")
    elif neutros >= positivos and neutros >= negativos:
        print(f"{nome}: Seus últimos registros parecem misturados ou tranquilos.")
    else:
        print(f"{nome}: Parece que seus últimos dias tiveram um pouco de tudo.")

    print("---------------------------------\n")