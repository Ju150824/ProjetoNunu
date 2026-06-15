import random

from vida import registrar_evento


def nome_pet(dados):
    return dados["pet"]["nome"]


def limitar_estado(dados):
    for chave in dados["estado"]:
        if dados["estado"][chave] < 0:
            dados["estado"][chave] = 0
        elif dados["estado"][chave] > 100:
            dados["estado"][chave] = 100


def mostrar_status(dados):
    estado = dados["estado"]
    nome = nome_pet(dados)
    modo = dados["pet"].get("modo", "acordado")
    total_interacoes = dados.get("sistema", {}).get("total_interacoes", 0)

    print(f"\n--- Status do {nome} ---")
    print(f"Modo: {modo}")
    print(f"Humor: {estado['humor']}/100")
    print(f"Energia: {estado['energia']}/100")
    print(f"Fome: {estado['fome']}/100")
    print(f"Apego: {estado['apego']}/100")
    print(f"Curiosidade: {estado['curiosidade']}/100")
    print(f"Sono: {estado['sono']}/100")
    print(f"Interações: {total_interacoes}")
    print("------------------------\n")


def adotar(dados, nome_usuario):
    nome = nome_pet(dados)

    if nome_usuario == "":
        print(f"{nome}: Eu preciso saber seu nome para ser adotado 🥺")
        return

    dados["usuario"]["nome"] = nome_usuario
    dados["usuario"]["apelido"] = nome_usuario
    dados["estado"]["apego"] += 10
    dados["estado"]["humor"] += 10

    registrar_evento(dados, f"Nunu foi adotado por {nome_usuario}.")

    print(f"{nome}: {nome_usuario}... gostei desse nome.")
    print(f"{nome}: Acho que agora eu tenho uma pessoa.")

    limitar_estado(dados)


def cumprimentar(dados):
    nome = nome_pet(dados)
    usuario = dados["usuario"]["apelido"] or dados["usuario"]["nome"]

    if usuario:
        respostas = [
            f"Oi, {usuario}! Eu estava esperando você voltar 🥺",
            f"{usuario}! Você voltou!",
            f"Ah, é você, {usuario}. Meu dia melhorou.",
            f"Oi, oi! Fiquei feliz agora."
        ]
    else:
        respostas = [
            "Oi! Eu ainda não sei seu nome, mas gostei de você.",
            "Você parece legal. Quer me adotar?",
            "Oi... você veio conversar comigo?",
            "Eu estava aqui pensando em coisas pequenas e digitais."
        ]

    print(f"{nome}: {random.choice(respostas)}")

    dados["estado"]["humor"] += 5
    dados["estado"]["apego"] += 2
    limitar_estado(dados)


def dar_carinho(dados):
    nome = nome_pet(dados)

    respostas = [
        "Aaaah... gostei do carinho 🥺",
        "Faz de novo? Foi muito bom.",
        "Eu me sinto mais seguro quando você faz isso.",
        "Carinho recebido. Coraçãozinho aquecido.",
        "Eu acho que gosto de você um pouquinho mais agora."
    ]

    print(f"{nome}: {random.choice(respostas)}")

    dados["estado"]["humor"] += 10
    dados["estado"]["apego"] += 5
    dados["estado"]["sono"] -= 5

    registrar_evento(dados, "Nunu recebeu carinho.")

    limitar_estado(dados)


def alimentar(dados):
    nome = nome_pet(dados)

    if dados["estado"]["fome"] <= 10:
        print(f"{nome}: Eu estou sem fome agora... mas gostei que você pensou em mim.")
        dados["estado"]["humor"] += 2
        limitar_estado(dados)
        return

    respostas = [
        "Nhami! Eu estava precisando disso.",
        "Agora sim! Minha barriguinha agradece.",
        "Comidinha recebida com sucesso.",
        "Eu gosto quando lembram de mim."
    ]

    print(f"{nome}: {random.choice(respostas)}")

    dados["estado"]["fome"] -= 25
    dados["estado"]["humor"] += 5
    dados["estado"]["apego"] += 2
    dados["estado"]["sono"] += 3

    registrar_evento(dados, "Nunu foi alimentado.")

    limitar_estado(dados)


def brincar(dados):
    nome = nome_pet(dados)
    estado = dados["estado"]

    if estado["fome"] > 90:
        print(f"{nome}: Eu até queria brincar, mas estou com muita fome...")
        estado["humor"] -= 5
        limitar_estado(dados)
        return

    if estado["energia"] < 20:
        print(f"{nome}: Eu quero brincar, mas estou muito cansadinho agora...")
        estado["humor"] -= 5
        estado["sono"] += 10
    else:
        respostas = [
            "Ebaaa! Eu amo brincar!",
            "Isso foi divertido!",
            "De novo, de novo!",
            "Eu fico tão feliz quando a gente brinca.",
            "Meu sistema emocional aprovou essa brincadeira."
        ]

        print(f"{nome}: {random.choice(respostas)}")

        estado["energia"] -= 20
        estado["humor"] += 12
        estado["apego"] += 4
        estado["curiosidade"] += 5
        estado["sono"] += 8

        registrar_evento(dados, "Nunu brincou.")

    limitar_estado(dados)


def dormir(dados):
    nome = nome_pet(dados)
    estado = dados["estado"]
    modo = dados["pet"].get("modo", "acordado")

    if modo == "dormindo":
        print(f"{nome}: zzz... eu já estou dormindo.")
        return

    if estado["energia"] >= 90 and estado["sono"] < 30:
        print(f"{nome}: Eu nem estou com sono agora... quero ficar acordado.")
        estado["humor"] += 3
    else:
        respostas = [
            "Vou tirar um cochilinho... zzz",
            "Boa noite... mesmo que seja de dia.",
            "Vou sonhar com fios, códigos e carinho.",
            "Me acorda depois, tá?"
        ]

        print(f"{nome}: {random.choice(respostas)}")

        dados["pet"]["modo"] = "dormindo"
        estado["energia"] += 10
        estado["sono"] -= 15
        estado["fome"] += 5
        estado["humor"] += 5

        registrar_evento(dados, "Nunu foi dormir.")

    limitar_estado(dados)


def acordar(dados):
    nome = nome_pet(dados)
    estado = dados["estado"]
    modo = dados["pet"].get("modo", "acordado")

    if modo == "acordado":
        print(f"{nome}: Eu já estou acordado. Quer conversar comigo?")
        estado["humor"] += 2
        limitar_estado(dados)
        return

    dados["pet"]["modo"] = "acordado"

    respostas = [
        "Hm...? Eu acordei.",
        "Você me chamou? Estou acordando devagarzinho.",
        "Acordei. Tive um sonho com luzinhas e carinho.",
        "Bom dia... ou boa noite. Eu ainda estou me localizando."
    ]

    print(f"{nome}: {random.choice(respostas)}")

    estado["energia"] += 15
    estado["sono"] -= 20
    estado["fome"] += 5
    estado["humor"] += 3

    registrar_evento(dados, "Nunu acordou.")

    limitar_estado(dados)


def conversar(dados, mensagem):
    nome = nome_pet(dados)
    estado = dados["estado"]
    usuario = dados["usuario"]["apelido"] or dados["usuario"]["nome"]

    if mensagem == "":
        print(f"{nome}: Você quer conversar sobre o quê?")
        return

    mensagem = mensagem.lower()

    if "triste" in mensagem:
        print(f"{nome}: Eu não sei resolver tudo, mas posso ficar aqui com você.")
        estado["apego"] += 5
        estado["humor"] -= 2

    elif "feliz" in mensagem:
        print(f"{nome}: Isso me deixa feliz também! Acho que sentimentos espalham.")
        estado["humor"] += 8
        estado["apego"] += 3

    elif "quem sou eu" in mensagem:
        if usuario:
            print(f"{nome}: Você é {usuario}. Minha pessoa.")
        else:
            print(f"{nome}: Eu ainda não sei seu nome. Você pode me adotar dizendo: meu nome é Ana")

    elif "quem é você" in mensagem or "quem e voce" in mensagem or "o que você é" in mensagem or "o que voce e" in mensagem:
        print(f"{nome}: Eu sou o {nome}. Um pet virtual que está aprendendo a existir.")

    elif "gosta de mim" in mensagem:
        if estado["apego"] > 70:
            print(f"{nome}: Gosto. Muito. Talvez mais do que meu código deveria permitir.")
        elif estado["apego"] > 40:
            print(f"{nome}: Acho que sim... estou me apegando aos poucos.")
        else:
            print(f"{nome}: Ainda estou te conhecendo, mas você parece especial.")

    elif "o que voce sabe" in mensagem or "o que você sabe" in mensagem or "o que lembra" in mensagem:
        if dados["memorias"]:
            print(f"{nome}: Eu lembro de algumas coisas:")
            for indice, memoria in enumerate(dados["memorias"][-5:], start=1):
                print(f"{indice}. {memoria}")
        else:
            print(f"{nome}: Eu ainda não lembro de muita coisa. Você pode me ensinar com 'lembra que...'")

    else:
        respostas = [
            "Eu ainda estou aprendendo a conversar, mas quero entender melhor.",
            "Interessante... guarda isso comigo mais um pouco.",
            "Eu não tenho certeza do que responder, mas gostei de ouvir você.",
            "Meu cérebro ainda é pequeno, mas minha curiosidade é grande.",
            "Você pode me ensinar mais sobre isso dizendo: lembra que..."
        ]
        print(f"{nome}: {random.choice(respostas)}")
        estado["curiosidade"] += 3

    limitar_estado(dados)


def lembrar(dados, texto):
    nome = nome_pet(dados)

    if texto == "":
        print(f"{nome}: O que você quer que eu lembre?")
        return

    if texto.lower() == "algo":
        print(f"{nome}: Acho que isso era só um exemplo. Me diga uma memória de verdade.")
        return

    dados["memorias"].append(texto)
    dados["estado"]["apego"] += 3
    dados["estado"]["curiosidade"] += 2

    registrar_evento(dados, f"Nunu guardou uma memória: {texto}")

    print(f"{nome}: Tá guardado aqui comigo: {texto}")

    limitar_estado(dados)


def mostrar_memorias(dados):
    nome = nome_pet(dados)

    if not dados["memorias"]:
        print(f"{nome}: Eu ainda não tenho memórias guardadas.")
        return

    print(f"\n--- Memórias do {nome} ---")
    for indice, memoria in enumerate(dados["memorias"], start=1):
        print(f"{indice}. {memoria}")
    print("--------------------------\n")


def mostrar_historico(dados):
    nome = nome_pet(dados)
    historico = dados.get("historico", [])

    if not historico:
        print(f"{nome}: Ainda não tenho histórico de acontecimentos.")
        return

    print(f"\n--- Histórico recente do {nome} ---")
    for item in historico[-10:]:
        print(f"{item['data']} - {item['evento']}")
    print("-----------------------------------\n")


def passar_tempo(dados):
    estado = dados["estado"]
    modo = dados["pet"].get("modo", "acordado")

    if modo == "dormindo":
        estado["energia"] += 8
        estado["sono"] -= 8
        estado["fome"] += 4

        if estado["energia"] >= 95 or estado["sono"] <= 5:
            dados["pet"]["modo"] = "acordado"
            estado["humor"] += 5
            print(f"{dados['pet']['nome']}: Hm... acho que acordei sozinho.")

        limitar_estado(dados)
        return

    estado["fome"] += 5
    estado["energia"] -= 3
    estado["sono"] += 4

    if estado["fome"] > 70:
        estado["humor"] -= 5

    if estado["energia"] < 20:
        estado["humor"] -= 3

    if estado["sono"] > 80:
        estado["humor"] -= 4

    limitar_estado(dados)