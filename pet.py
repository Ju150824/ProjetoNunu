import random


def limitar_status(pet):
    for chave in ["humor", "energia", "fome", "apego"]:
        if pet[chave] < 0:
            pet[chave] = 0
        elif pet[chave] > 100:
            pet[chave] = 100


def mostrar_status(pet):
    print("\n--- Status do Nunu ---")
    print(f"Humor: {pet['humor']}/100")
    print(f"Energia: {pet['energia']}/100")
    print(f"Fome: {pet['fome']}/100")
    print(f"Apego: {pet['apego']}/100")
    print("----------------------\n")


def cumprimentar(pet):
    respostas = [
        "Oi! Eu estava esperando você voltar 🥺",
        "Você voltou! Eu senti sua falta.",
        "Oi, oi! Fiquei feliz agora.",
        "Ah, é você! Meu dia melhorou."
    ]
    print(f"{pet['nome']}: {random.choice(respostas)}")
    pet["humor"] += 5
    pet["apego"] += 2
    limitar_status(pet)


def dar_carinho(pet):
    respostas = [
        "Aaaah... gostei do carinho 🥺",
        "Faz de novo? Foi muito bom.",
        "Eu me sinto mais seguro quando você faz isso.",
        "Carinho recebido. Coraçãozinho aquecido."
    ]
    print(f"{pet['nome']}: {random.choice(respostas)}")
    pet["humor"] += 10
    pet["apego"] += 5
    limitar_status(pet)


def alimentar(pet):
    respostas = [
        "Nhami! Eu estava precisando disso.",
        "Agora sim! Minha barriguinha agradece.",
        "Comidinha recebida com sucesso.",
        "Eu gosto quando você lembra de mim."
    ]
    print(f"{pet['nome']}: {random.choice(respostas)}")
    pet["fome"] -= 25
    pet["humor"] += 5
    pet["apego"] += 2
    limitar_status(pet)


def brincar(pet):
    if pet["energia"] < 20:
        print(f"{pet['nome']}: Eu quero brincar, mas estou muito cansadinho agora...")
        pet["humor"] -= 5
    else:
        respostas = [
            "Ebaaa! Eu amo brincar com você!",
            "Isso foi divertido!",
            "De novo, de novo!",
            "Eu fico tão feliz quando a gente brinca."
        ]
        print(f"{pet['nome']}: {random.choice(respostas)}")
        pet["energia"] -= 20
        pet["humor"] += 12
        pet["apego"] += 4

    limitar_status(pet)


def dormir(pet):
    if pet["energia"] >= 90:
        print(f"{pet['nome']}: Eu nem estou com sono agora... quero ficar acordado com você.")
        pet["humor"] += 3
    else:
        respostas = [
            "Vou tirar um cochilinho... zzz",
            "Boa noite... mesmo que seja de dia.",
            "Vou sonhar com fios, códigos e carinho.",
            "Me acorda depois, tá?"
        ]
        print(f"{pet['nome']}: {random.choice(respostas)}")
        pet["energia"] += 35
        pet["fome"] += 10
        pet["humor"] += 5

    limitar_status(pet)


def passar_tempo(pet):
    pet["fome"] += 5
    pet["energia"] -= 3

    if pet["fome"] > 70:
        pet["humor"] -= 5

    if pet["energia"] < 20:
        pet["humor"] -= 3

    limitar_status(pet)

def lembrar(pet, texto):
    if texto == "":
        print(f"{pet['nome']}: O que você quer que eu lembre?")
        return

    pet["memorias"].append(texto)
    pet["apego"] += 3
    print(f"{pet['nome']}: Tá guardado aqui comigo: {texto}")
    limitar_status(pet)


def mostrar_memorias(pet):
    if not pet["memorias"]:
        print(f"{pet['nome']}: Eu ainda não tenho memórias guardadas.")
        return

    print("\n--- Memórias do Nunu ---")
    for indice, memoria in enumerate(pet["memorias"], start=1):
        print(f"{indice}. {memoria}")
    print("------------------------\n")