import re
import unicodedata
from datetime import datetime, timedelta

from vida import registrar_evento


FORMATO_DATA = "%Y-%m-%d %H:%M:%S"


def normalizar(texto):
    texto = texto.strip().lower()

    texto_sem_acento = unicodedata.normalize("NFD", texto)
    texto_sem_acento = "".join(
        caractere for caractere in texto_sem_acento
        if unicodedata.category(caractere) != "Mn"
    )

    texto_sem_acento = re.sub(r"[^a-z0-9\s:]", " ", texto_sem_acento)
    texto_sem_acento = re.sub(r"\s+", " ", texto_sem_acento)

    return texto_sem_acento.strip()


def formatar_data(data_hora):
    return data_hora.strftime("%d/%m/%Y às %H:%M")


def proximo_id(dados):
    lembretes = dados.get("lembretes", [])

    if not lembretes:
        return 1

    return max(lembrete["id"] for lembrete in lembretes) + 1


def limpar_descricao(texto):
    texto = normalizar(texto)

    texto = re.sub(r"\bem\s+\d+\s*(minuto|minutos|min|hora|horas)\b", "", texto)
    texto = re.sub(r"\b(as|a)\s+\d{1,2}([:h]\d{2})?\b", "", texto)
    texto = texto.replace("depois de amanha", "")
    texto = texto.replace("amanha", "")
    texto = texto.replace("hoje", "")

    texto = re.sub(r"\s+", " ", texto)
    texto = texto.strip()

    return texto


def interpretar_data_hora(texto):
    texto_normalizado = normalizar(texto)
    agora = datetime.now()

    relativo = re.search(
        r"\bem\s+(\d+)\s*(minuto|minutos|min|hora|horas)\b",
        texto_normalizado
    )

    if relativo:
        quantidade = int(relativo.group(1))
        unidade = relativo.group(2)

        if unidade in ["hora", "horas"]:
            data_hora = agora + timedelta(hours=quantidade)
        else:
            data_hora = agora + timedelta(minutes=quantidade)

        descricao = limpar_descricao(texto)

        return data_hora, descricao

    horario = re.search(
        r"\b(as|a)\s+(\d{1,2})(?:[:h](\d{2}))?\b",
        texto_normalizado
    )

    if not horario:
        return None, ""

    hora = int(horario.group(2))
    minuto = int(horario.group(3)) if horario.group(3) else 0

    if hora < 0 or hora > 23 or minuto < 0 or minuto > 59:
        return None, ""

    dias = 0

    if "depois de amanha" in texto_normalizado:
        dias = 2
    elif "amanha" in texto_normalizado:
        dias = 1

    data_hora = datetime(
        agora.year,
        agora.month,
        agora.day,
        hora,
        minuto,
        0
    ) + timedelta(days=dias)

    if dias == 0 and data_hora <= agora:
        data_hora += timedelta(days=1)

    descricao = limpar_descricao(texto)

    return data_hora, descricao


def criar_lembrete(dados, texto):
    nome = dados["pet"]["nome"]

    if "lembretes" not in dados:
        dados["lembretes"] = []

    if texto.strip() == "":
        print(f"{nome}: Me diga o que eu devo lembrar e o horário.")
        print(f"{nome}: Exemplo: me lembre de estudar às 19:00")
        return

    data_hora, descricao = interpretar_data_hora(texto)

    if data_hora is None:
        print(f"{nome}: Eu ainda preciso de um horário para esse lembrete.")
        print(f"{nome}: Tente assim: me lembre de estudar às 19:00")
        print(f"{nome}: Ou assim: me lembre de beber água em 10 minutos")
        return

    if descricao == "":
        descricao = "lembrete sem descrição"

    lembrete = {
        "id": proximo_id(dados),
        "texto": descricao,
        "data_hora": data_hora.strftime(FORMATO_DATA),
        "concluido": False,
        "notificado": False
    }

    dados["lembretes"].append(lembrete)

    dados["estado"]["apego"] += 2
    dados["estado"]["curiosidade"] += 1

    registrar_evento(
        dados,
        f"Nunu criou um lembrete: {descricao} em {formatar_data(data_hora)}."
    )

    print(f"{nome}: Tá combinado. Vou tentar lembrar você de '{descricao}' em {formatar_data(data_hora)}.")


def listar_lembretes(dados):
    nome = dados["pet"]["nome"]
    lembretes = dados.get("lembretes", [])

    if not lembretes:
        print(f"{nome}: Você ainda não tem lembretes comigo.")
        return

    ativos = [lembrete for lembrete in lembretes if not lembrete.get("concluido", False)]

    if not ativos:
        print(f"{nome}: Todos os lembretes estão concluídos.")
        return

    print(f"\n--- Lembretes do {nome} ---")

    agora = datetime.now()

    for lembrete in ativos:
        try:
            data_hora = datetime.strptime(lembrete["data_hora"], FORMATO_DATA)
            data_formatada = formatar_data(data_hora)
        except ValueError:
            data_hora = agora
            data_formatada = lembrete["data_hora"]

        status = "pendente"

        if data_hora <= agora:
            status = "na hora"

        print(f"{lembrete['id']}. {lembrete['texto']} — {data_formatada} [{status}]")

    print("--------------------------\n")


def verificar_lembretes(dados):
    nome = dados["pet"]["nome"]
    lembretes = dados.get("lembretes", [])

    if not lembretes:
        return

    agora = datetime.now()

    for lembrete in lembretes:
        if lembrete.get("concluido", False):
            continue

        if lembrete.get("notificado", False):
            continue

        try:
            data_hora = datetime.strptime(lembrete["data_hora"], FORMATO_DATA)
        except ValueError:
            continue

        if data_hora <= agora:
            lembrete["notificado"] = True

            dados["estado"]["apego"] += 1

            registrar_evento(
                dados,
                f"Nunu avisou um lembrete: {lembrete['texto']}."
            )

            print(f"{nome}: Ei! Você me pediu para lembrar: {lembrete['texto']}")


def concluir_lembrete(dados, conteudo):
    nome = dados["pet"]["nome"]
    lembretes = dados.get("lembretes", [])

    try:
        id_lembrete = int(conteudo.strip())
    except ValueError:
        print(f"{nome}: Me diga o número do lembrete que você quer concluir.")
        print(f"{nome}: Exemplo: concluir lembrete 1")
        return

    for lembrete in lembretes:
        if lembrete["id"] == id_lembrete:
            lembrete["concluido"] = True

            registrar_evento(
                dados,
                f"Nunu concluiu o lembrete: {lembrete['texto']}."
            )

            print(f"{nome}: Pronto. Marquei esse lembrete como concluído.")
            return

    print(f"{nome}: Não encontrei esse lembrete.")


def remover_lembrete(dados, conteudo):
    nome = dados["pet"]["nome"]
    lembretes = dados.get("lembretes", [])

    try:
        id_lembrete = int(conteudo.strip())
    except ValueError:
        print(f"{nome}: Me diga o número do lembrete que você quer apagar.")
        print(f"{nome}: Exemplo: apagar lembrete 1")
        return

    for lembrete in lembretes:
        if lembrete["id"] == id_lembrete:
            dados["lembretes"].remove(lembrete)

            registrar_evento(
                dados,
                f"Nunu apagou um lembrete: {lembrete['texto']}."
            )

            print(f"{nome}: Apaguei esse lembrete.")
            return

    print(f"{nome}: Não encontrei esse lembrete.")