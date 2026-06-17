from memoria import carregar_dados, salvar_dados

from pet import (
    mostrar_status,
    adotar,
    cumprimentar,
    dar_carinho,
    alimentar,
    brincar,
    dormir,
    acordar,
    conversar,
    lembrar,
    mostrar_memorias,
    mostrar_historico,
    passar_tempo
)

from cerebro import (
    mostrar_humor,
    observar,
    pensamento_espontaneo
)

from intencoes import interpretar

from vida import (
    aplicar_ausencia,
    registrar_interacao
)

from personalidade import (
    mostrar_personalidade,
    mostrar_perfil
)

from lembretes import (
    criar_lembrete,
    listar_lembretes,
    verificar_lembretes,
    concluir_lembrete,
    remover_lembrete
)

from diario import (
    registrar_diario,
    listar_diario,
    resumo_diario
)


def mostrar_ajuda():
    print("\n--- Comandos e frases que o Nunu entende ---")
    print("adotar SEU_NOME")
    print("meu nome é SEU_NOME")
    print("oi")
    print("status")
    print("como você está?")
    print("observar")
    print("personalidade")
    print("perfil")
    print("carinho")
    print("comer")
    print("brincar")
    print("dormir")
    print("acordar")
    print("conversar MENSAGEM")
    print("lembrar ALGO")
    print("memorias")
    print("me lembre de estudar às 19:00")
    print("lembretes")
    print("diario hoje foi um dia difícil")
    print("hoje foi um dia bom")
    print("diario")
    print("resumo emocional")
    print("historico")
    print("sair")
    print("--------------------------------------------\n")


def pode_interagir_dormindo(intencao):
    return intencao in [
        "sair",
        "ajuda",
        "status",
        "humor",
        "observar",
        "acordar",
        "historico",
        "personalidade",
        "perfil",
        "memorias",
        "listar_lembretes",
        "listar_diario",
        "resumo_diario"
    ]


dados = carregar_dados()

nome = dados["pet"]["nome"]
versao = dados["pet"]["versao"]

print(f"{nome} v{versao} iniciado!")
print("Digite 'ajuda' para ver o que o Nunu entende.\n")

aplicar_ausencia(dados)
verificar_lembretes(dados)

while True:
    comando = input("Você: ").strip()

    intencao, conteudo = interpretar(comando)

    modo_atual = dados["pet"].get("modo", "acordado")

    if modo_atual == "dormindo" and not pode_interagir_dormindo(intencao):
        print(f"{dados['pet']['nome']}: zzz... estou dormindo agora. Se precisar de mim, tente me acordar.")
        passar_tempo(dados)
        registrar_interacao(dados)
        salvar_dados(dados)
        continue

    if intencao == "sair":
        registrar_interacao(dados)
        verificar_lembretes(dados)
        salvar_dados(dados)
        print(f"{dados['pet']['nome']}: Tá bom... vou sentir sua falta 🥺")
        print("Dados salvos. Até depois!")
        break

    elif intencao == "ajuda":
        mostrar_ajuda()

    elif intencao == "adotar":
        adotar(dados, conteudo)

    elif intencao == "oi":
        cumprimentar(dados)

    elif intencao == "status":
        mostrar_status(dados)

    elif intencao == "humor":
        mostrar_humor(dados)

    elif intencao == "observar":
        observar(dados)

    elif intencao == "personalidade":
        mostrar_personalidade(dados)

    elif intencao == "perfil":
        mostrar_perfil(dados)

    elif intencao == "carinho":
        dar_carinho(dados)

    elif intencao == "comer":
        alimentar(dados)

    elif intencao == "brincar":
        brincar(dados)

    elif intencao == "dormir":
        dormir(dados)

    elif intencao == "acordar":
        acordar(dados)

    elif intencao == "lembrar":
        lembrar(dados, conteudo)

    elif intencao == "memorias":
        mostrar_memorias(dados)

    elif intencao == "criar_lembrete":
        criar_lembrete(dados, conteudo)

    elif intencao == "listar_lembretes":
        listar_lembretes(dados)

    elif intencao == "concluir_lembrete":
        concluir_lembrete(dados, conteudo)

    elif intencao == "remover_lembrete":
        remover_lembrete(dados, conteudo)

    elif intencao == "registrar_diario":
        registrar_diario(dados, conteudo)

    elif intencao == "listar_diario":
        listar_diario(dados)

    elif intencao == "resumo_diario":
        resumo_diario(dados)

    elif intencao == "historico":
        mostrar_historico(dados)

    elif intencao == "conversar":
        conversar(dados, conteudo)

    passar_tempo(dados)
    registrar_interacao(dados)
    verificar_lembretes(dados)
    salvar_dados(dados)
    pensamento_espontaneo(dados)