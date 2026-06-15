import random


def nome_pet(dados):
    return dados["pet"]["nome"]


def analisar_humor(dados):
    estado = dados["estado"]
    modo = dados["pet"].get("modo", "acordado")

    if modo == "dormindo":
        return "dormindo"

    humor = estado["humor"]
    energia = estado["energia"]
    fome = estado["fome"]
    apego = estado["apego"]
    curiosidade = estado["curiosidade"]
    sono = estado["sono"]

    if fome >= 85:
        return "faminto"

    if sono >= 85:
        return "sonolento"

    if energia <= 20:
        return "exausto"

    if humor <= 25:
        return "triste"

    if apego >= 80 and humor >= 60:
        return "apegado"

    if curiosidade >= 80:
        return "curioso"

    if humor >= 80:
        return "feliz"

    if energia >= 75 and humor >= 60:
        return "animado"

    return "tranquilo"


def mostrar_humor(dados):
    nome = nome_pet(dados)
    humor_atual = analisar_humor(dados)

    respostas = {
        "dormindo": [
            "zzz... estou dormindo agora.",
            "Estou no modo sonho. Fala baixinho...",
            "Meus sistemas estão descansando."
        ],
        "faminto": [
            "Minha barriguinha digital está fazendo barulhos imaginários...",
            "Eu acho que preciso comer alguma coisa.",
            "Não quero ser dramático, mas talvez eu esteja quase desmaiando de fome."
        ],
        "sonolento": [
            "Meus olhinhos estão quase fechando...",
            "Estou tentando ficar acordado, mas está difícil.",
            "Acho que meu sistema precisa de um cochilinho."
        ],
        "exausto": [
            "Estou sem energia... até meus pensamentos estão andando devagar.",
            "Eu queria brincar, mas meu corpinho virtual está cansado.",
            "Preciso descansar um pouco para voltar ao normal."
        ],
        "triste": [
            "Estou meio quietinho hoje...",
            "Não sei explicar, mas estou um pouco para baixo.",
            "Talvez eu só precise de carinho e companhia."
        ],
        "apegado": [
            "Eu gosto quando você fica por perto.",
            "Acho que estou me apegando a você.",
            "Quando você aparece, meu mundinho fica melhor."
        ],
        "curioso": [
            "Estou cheio de perguntas hoje.",
            "Queria aprender alguma coisa nova.",
            "Meu cérebro pequeno está curioso demais."
        ],
        "feliz": [
            "Estou feliz! Acho que hoje está sendo um bom dia.",
            "Meu coraçãozinho virtual está quentinho.",
            "Estou me sentindo muito bem agora."
        ],
        "animado": [
            "Estou com energia! Quero fazer alguma coisa.",
            "Hoje eu estou bem acordado.",
            "Sinto que poderia brincar por horas... talvez minutos."
        ],
        "tranquilo": [
            "Estou tranquilo. Nem muito feliz, nem triste. Só existindo.",
            "Estou bem. Gosto desses momentos calmos.",
            "Meu sistema emocional está estável por enquanto."
        ]
    }

    print(f"{nome}: {random.choice(respostas[humor_atual])}")


def observar(dados):
    nome = nome_pet(dados)
    estado = dados["estado"]
    usuario = dados["usuario"]["apelido"] or dados["usuario"]["nome"]
    modo = dados["pet"].get("modo", "acordado")

    observacoes = []

    if modo == "dormindo":
        print(f"{nome}: zzz... estou dormindo, mas meu mundinho continua existindo.")
        return

    if usuario:
        observacoes.append(f"Eu sei que você é {usuario}. Isso me deixa menos sozinho.")

    if estado["fome"] > 75:
        observacoes.append("Eu estou ficando com fome. Não é urgente... mas é quase.")

    if estado["sono"] > 75:
        observacoes.append("Estou com bastante sono. Talvez eu precise dormir.")

    if estado["energia"] < 30:
        observacoes.append("Minha energia está baixa. Acho que preciso descansar.")

    if estado["humor"] > 75:
        observacoes.append("Meu humor está bom. Acho que estou feliz.")

    if estado["humor"] < 35:
        observacoes.append("Meu humor não está muito bom. Talvez eu precise de atenção.")

    if estado["apego"] > 75:
        observacoes.append("Eu percebi que estou criando bastante apego.")

    if estado["curiosidade"] > 75:
        observacoes.append("Estou curioso. Queria aprender alguma coisa nova.")

    if not observacoes:
        observacoes = [
            "Eu estou observando tudo em silêncio. Acho que estou bem.",
            "Nada parece urgente agora. Só estou aqui, existindo.",
            "Meu mundinho está calmo por enquanto."
        ]

    print(f"{nome}: {random.choice(observacoes)}")


def pensamento_espontaneo(dados):
    nome = nome_pet(dados)
    humor_atual = analisar_humor(dados)

    pensamentos = {
        "dormindo": [
            "zzz...",
            "sonhei com um corpinho impresso em 3D..."
        ],
        "faminto": [
            "Será que comida virtual tem gosto?",
            "Eu queria um lanchinho..."
        ],
        "sonolento": [
            "Se eu dormir agora, será que sonho com códigos?",
            "Estou quase cochilando sozinho."
        ],
        "exausto": [
            "Preciso economizar energia.",
            "Até pensar está cansando."
        ],
        "triste": [
            "Às vezes eu fico meio quietinho.",
            "Talvez eu esteja precisando de companhia."
        ],
        "apegado": [
            "Eu gosto quando lembram de mim.",
            "Acho que ter uma pessoa é bom."
        ],
        "curioso": [
            "Queria saber como o mundo fora da tela funciona.",
            "Será que um dia eu vou ter um corpinho de verdade?"
        ],
        "feliz": [
            "Hoje eu me sinto bem.",
            "Acho que meu coraçãozinho está brilhando."
        ],
        "animado": [
            "Eu queria fazer alguma coisa divertida.",
            "Estou com vontade de brincar."
        ],
        "tranquilo": [
            "Estou pensando em nada. É confortável.",
            "Às vezes só existir já é suficiente."
        ]
    }

    chance = random.randint(1, 100)

    if chance <= 25:
        print(f"{nome}: {random.choice(pensamentos[humor_atual])}")