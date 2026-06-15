pet = {
    "nome": "Nunu",
    "humor": 70,
    "energia": 80,
    "fome": 30
}

print("Nunu v0.1 iniciado!")
print("Digite 'sair' para encerrar.\n")

while True:
    mensagem = input("Você: ").lower()

    if mensagem == "sair":
        print(f'{pet["nome"]}: Tá bom... vou sentir sua falta 🥺')
        break

    elif "oi" in mensagem or "olá" in mensagem:
        print(f'{pet["nome"]}: Oi! Eu estava esperando você voltar.')

    elif "carinho" in mensagem:
        pet["humor"] += 10
        print(f'{pet["nome"]}: Aaaah... gostei do carinho 🥺')

    elif "comer" in mensagem or "comida" in mensagem:
        pet["fome"] -= 20
        print(f'{pet["nome"]}: Nhami! Agora estou mais feliz.')

    elif "brincar" in mensagem:
        pet["energia"] -= 15
        pet["humor"] += 10
        print(f'{pet["nome"]}: Ebaaa! Eu amo brincar com você!')

    elif "dormir" in mensagem:
        pet["energia"] += 20
        print(f'{pet["nome"]}: Vou tirar um cochilinho... zzz')

    else:
        print(f'{pet["nome"]}: Não entendi muito bem, mas gosto quando você fala comigo.')

    print(f'Status → Humor: {pet["humor"]} | Energia: {pet["energia"]} | Fome: {pet["fome"]}\n')