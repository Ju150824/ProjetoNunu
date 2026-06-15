from memoria import carregar_dados, salvar_dados

from pet import (
    mostrar_status,
    adotar,
    cumprimentar,
    dar_carinho,
    alimentar,
    brincar,
    dormir,
    conversar,
    lembrar,
    mostrar_memorias,
    passar_tempo
)

from cerebro import (
    mostrar_humor,
    observar,
    pensamento_espontaneo
)

from intencoes import interpretar


def mostrar_ajuda():
    print("\n--- Comandos e frases que o Nunu entende ---")
    print("adotar SEU_NOME")
    print("meu nome é SEU_NOME")
    print("oi")
    print("status")
    print("como você está?")
    print("observar")
    print("carinho")
    print("quero fazer carinho em você")
    print("comer")
    print("come alguma coisa")
    print("brincar")
    print("vamos brincar")
    print("dormir")
    print("vai descansar")
    print("conversar MENSAGEM")
    print("lembrar ALGO")
    print("lembra que ALGO")
    print("memorias")
    print("sair")
    print("--------------------------------------------\n")


dados = carregar_dados()

nome = dados["pet"]["nome"]
versao = dados["pet"]["versao"]

print(f"{nome} v{versao} iniciado!")
print("Digite 'ajuda' para ver o que o Nunu entende.\n")

while True:
    comando = input("Você: ").strip()

    intencao, conteudo = interpretar(comando)

    if intencao == "sair":
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

    elif intencao == "carinho":
        dar_carinho(dados)

    elif intencao == "comer":
        alimentar(dados)

    elif intencao == "brincar":
        brincar(dados)

    elif intencao == "dormir":
        dormir(dados)

    elif intencao == "lembrar":
        lembrar(dados, conteudo)

    elif intencao == "memorias":
        mostrar_memorias(dados)

    elif intencao == "conversar":
        conversar(dados, conteudo)

    passar_tempo(dados)
    salvar_dados(dados)
    pensamento_espontaneo(dados)