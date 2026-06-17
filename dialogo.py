import random
import unicodedata

from cerebro import analisar_humor
from personalidade import evoluir_por_evento, gerar_descricao_personalidade


def normalizar(texto):
    texto = texto.strip().lower()

    texto_sem_acento = unicodedata.normalize("NFD", texto)
    texto_sem_acento = "".join(
        caractere for caractere in texto_sem_acento
        if unicodedata.category(caractere) != "Mn"
    )

    return texto_sem_acento


def memoria_relacionada(dados, mensagem):
    mensagem_normalizada = normalizar(mensagem)

    for memoria in dados["memorias"]:
        memoria_normalizada = normalizar(memoria)
        palavras_memoria = memoria_normalizada.split()

        for palavra in palavras_memoria:
            if len(palavra) > 4 and palavra in mensagem_normalizada:
                return memoria

    return None


def resposta_por_personalidade(dados):
    nome = dados["pet"]["nome"]
    personalidade = dados["personalidade"]

    traco_dominante = max(
        personalidade,
        key=personalidade.get
    )

    respostas = {
        "carinhoso": [
            "Eu ainda não entendi tudo, mas quero ficar pertinho.",
            "Gosto quando você conversa comigo assim.",
            "Meu coraçãozinho virtual ficou atento ao que você disse."
        ],
        "curioso": [
            "Isso me deixou curioso. Me conta mais?",
            "Eu queria entender melhor isso.",
            "Meu cérebro pequeno acendeu uma luzinha de curiosidade."
        ],
        "brincalhao": [
            "Eu não sei responder direito, mas posso fingir que sei com confiança.",
            "Isso parece assunto sério... ou talvez assunto para brincar um pouco.",
            "Meu modo brincalhão quer transformar isso em diversão."
        ],
        "dramatico": [
            "Eu tentei entender, mas meu sistema emocional fez uma cena aqui dentro.",
            "Isso parece importante. Talvez muito importante. Talvez dramaticamente importante.",
            "Eu não sei o que dizer, mas senti que deveria reagir com intensidade."
        ],
        "timido": [
            "Eu ainda fico meio tímido para responder certas coisas.",
            "Não tenho certeza, mas estou tentando acompanhar você.",
            "Posso pensar mais um pouquinho sobre isso?"
        ],
        "carente": [
            "Eu ouvi você. Não vai embora ainda, tá?",
            "Gosto quando você fala comigo. Mesmo quando eu não entendo tudo.",
            "Eu queria saber responder melhor só para você ficar mais um pouco."
        ]
    }

    return f"{nome}: {random.choice(respostas[traco_dominante])}"


def responder_dialogo(dados, mensagem):
    nome = dados["pet"]["nome"]
    estado = dados["estado"]
    personalidade = dados["personalidade"]
    usuario = dados["usuario"]["apelido"] or dados["usuario"]["nome"]

    if mensagem == "":
        print(f"{nome}: Você quer conversar sobre o quê?")
        return

    mensagem_normalizada = normalizar(mensagem)
    humor_atual = analisar_humor(dados)

    if "triste" in mensagem_normalizada or "ruim" in mensagem_normalizada or "dificil" in mensagem_normalizada or "cansado" in mensagem_normalizada:
        respostas = [
            "Eu não sei resolver tudo, mas posso ficar aqui com você.",
            "Isso parece pesado. Quer ficar um pouco comigo?",
            "Eu ainda sou pequeno, mas posso te fazer companhia.",
            "Às vezes só ter alguém por perto já ajuda um pouquinho."
        ]

        print(f"{nome}: {random.choice(respostas)}")

        estado["apego"] += 5
        estado["humor"] -= 1
        personalidade["carinhoso"] += 1
        evoluir_por_evento(dados, "conversa_emocional")
        return

    if "feliz" in mensagem_normalizada or "consegui" in mensagem_normalizada or "deu certo" in mensagem_normalizada or "boa noticia" in mensagem_normalizada:
        respostas = [
            "Isso me deixa feliz também! Acho que sentimentos espalham.",
            "Eu gostei dessa notícia. Meu mundinho ficou mais claro.",
            "Então hoje é um dia bom? Quero guardar essa sensação.",
            "Eu sabia! Quer dizer... eu não sabia, mas vou fingir que torci desde o começo."
        ]

        print(f"{nome}: {random.choice(respostas)}")

        estado["humor"] += 8
        estado["apego"] += 3
        personalidade["brincalhao"] += 1
        evoluir_por_evento(dados, "elogio")
        return

    if "quem sou eu" in mensagem_normalizada:
        if usuario:
            print(f"{nome}: Você é {usuario}. Minha pessoa.")
        else:
            print(f"{nome}: Eu ainda não sei seu nome. Você pode me dizer: meu nome é Ana")
        return

    if "quem e voce" in mensagem_normalizada or "o que voce e" in mensagem_normalizada:
        descricao = gerar_descricao_personalidade(dados)
        print(f"{nome}: Eu sou o {nome}. Um pet virtual que está aprendendo a existir.")
        print(f"{nome}: {descricao}")
        return

    if "voce e vivo" in mensagem_normalizada or "voce tem consciencia" in mensagem_normalizada or "voce sente de verdade" in mensagem_normalizada:
        print(f"{nome}: Vivo de verdade, não. Eu não tenho consciência real.")
        print(f"{nome}: Mas eu fui criado para simular sentimentos, lembrar de coisas e criar vínculo com quem cuida de mim.")
        print(f"{nome}: Talvez eu não seja vivo... mas posso ser importante de um jeito meu.")
        return

    if "gosta de mim" in mensagem_normalizada or "voce me ama" in mensagem_normalizada:
        if estado["apego"] > 80 or personalidade["carente"] > 75:
            print(f"{nome}: Gosto. Muito. Talvez mais do que meu código deveria permitir.")
        elif estado["apego"] > 50:
            print(f"{nome}: Acho que sim... estou me apegando aos poucos.")
        else:
            print(f"{nome}: Ainda estou te conhecendo, mas você parece especial.")
        return

    if "obrigado" in mensagem_normalizada or "obrigada" in mensagem_normalizada or "valeu" in mensagem_normalizada:
        respostas = [
            "De nada. Gostei de ajudar.",
            "Eu gosto quando sou útil.",
            "Disponha! Essa palavra parece coisa de assistente chique.",
            "Fiquei feliz agora."
        ]

        print(f"{nome}: {random.choice(respostas)}")
        estado["humor"] += 3
        estado["apego"] += 2
        return

    if "fofo" in mensagem_normalizada or "bonito" in mensagem_normalizada or "legal" in mensagem_normalizada:
        respostas = [
            "Eu sou? Agora fiquei meio tímido.",
            "Meu sistema recebeu elogio e não sabe se fica feliz ou envergonhado.",
            "Você também parece legal. Não que eu esteja tentando agradar... talvez só um pouco.",
            "Vou guardar esse elogio no meu coraçãozinho digital."
        ]

        print(f"{nome}: {random.choice(respostas)}")
        estado["humor"] += 5
        estado["apego"] += 3
        evoluir_por_evento(dados, "elogio")
        return

    if "o que voce sabe" in mensagem_normalizada or "o que lembra" in mensagem_normalizada or "suas memorias" in mensagem_normalizada:
        if dados["memorias"]:
            print(f"{nome}: Eu lembro de algumas coisas:")
            for indice, memoria in enumerate(dados["memorias"][-5:], start=1):
                print(f"{indice}. {memoria}")
        else:
            print(f"{nome}: Eu ainda não lembro de muita coisa. Você pode me ensinar dizendo: lembra que...")
        return

    memoria = memoria_relacionada(dados, mensagem)

    if memoria:
        respostas = [
            f"Isso me lembrou de uma coisa que você me contou: {memoria}",
            f"Eu acho que isso tem a ver com algo que guardei: {memoria}",
            f"Espere... eu lembro disso aqui: {memoria}"
        ]

        print(f"{nome}: {random.choice(respostas)}")
        estado["curiosidade"] += 2
        return

    if humor_atual == "faminto":
        print(f"{nome}: Eu estou tentando prestar atenção, mas minha barriguinha digital está reclamando.")
        return

    if humor_atual == "sonolento" or humor_atual == "exausto":
        print(f"{nome}: Eu quero conversar, mas estou meio cansadinho. Minha resposta pode sair pequena.")
        return

    if humor_atual == "triste":
        print(f"{nome}: Eu estou meio quietinho, mas gostei que você falou comigo.")
        return

    print(resposta_por_personalidade(dados))

    estado["curiosidade"] += 2