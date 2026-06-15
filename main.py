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

dados = carregar_dados()

nome = dados["pet"]["nome"]
versao = dados["pet"]["versao"]

print(f"{nome} v{versao} iniciado!")
print("Comandos disponíveis:")
print("adotar SEU_NOME | oi | status | carinho | comer | brincar | dormir")
print("conversar MENSAGEM | lembrar ALGO | memorias | sair\n")

while True:
    comando = input("Você: ").strip()
    comando_minusculo = comando.lower()

    if comando_minusculo == "sair":
        salvar_dados(dados)
        print(f"{dados['pet']['nome']}: Tá bom... vou sentir sua falta 🥺")
        print("Dados salvos. Até depois!")
        break

    elif comando_minusculo.startswith("adotar "):
        nome_usuario = comando[7:].strip()
        adotar(dados, nome_usuario)

    elif comando_minusculo == "oi":
        cumprimentar(dados)

    elif comando_minusculo == "status":
        mostrar_status(dados)

    elif comando_minusculo == "carinho":
        dar_carinho(dados)

    elif comando_minusculo == "comer":
        alimentar(dados)

    elif comando_minusculo == "brincar":
        brincar(dados)

    elif comando_minusculo == "dormir":
        dormir(dados)

    elif comando_minusculo == "conversar":
        conversar(dados, "")

    elif comando_minusculo.startswith("conversar "):
        mensagem = comando[10:].strip()
        conversar(dados, mensagem)

    elif comando_minusculo == "lembrar":
        lembrar(dados, "")

    elif comando_minusculo.startswith("lembrar "):
        texto = comando[8:].strip()
        lembrar(dados, texto)

    elif comando_minusculo == "memorias":
        mostrar_memorias(dados)

    else:
        print(f"{dados['pet']['nome']}: Eu ainda não conheço esse comando, mas estou aprendendo.")

    passar_tempo(dados)
    salvar_dados(dados)