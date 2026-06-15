from memoria import carregar_pet, salvar_pet
from pet import (
    mostrar_status,
    cumprimentar,
    dar_carinho,
    alimentar,
    brincar,
    dormir,
    passar_tempo
)

pet = carregar_pet()

print(f"{pet['nome']} v0.2 iniciado!")
print("Comandos disponíveis:")
print("oi | status | carinho | comer | brincar | dormir | sair\n")

while True:
    comando = input("Você: ").strip().lower()

    if comando == "sair":
        salvar_pet(pet)
        print(f"{pet['nome']}: Tá bom... vou sentir sua falta 🥺")
        print("Dados salvos. Até depois!")
        break

    elif comando == "oi":
        cumprimentar(pet)

    elif comando == "status":
        mostrar_status(pet)

    elif comando == "carinho":
        dar_carinho(pet)

    elif comando == "comer":
        alimentar(pet)

    elif comando == "brincar":
        brincar(pet)

    elif comando == "dormir":
        dormir(pet)

    else:
        print(f"{pet['nome']}: Eu ainda não entendi esse comando, mas estou aprendendo.")

    passar_tempo(pet)
    salvar_pet(pet)