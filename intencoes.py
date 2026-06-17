import re
import unicodedata
from difflib import get_close_matches


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


def palavra_parecida(palavra, opcoes):
    resultado = get_close_matches(palavra, opcoes, n=1, cutoff=0.82)
    return len(resultado) > 0


def contem_palavra_parecida(texto, opcoes):
    palavras = texto.split()

    for palavra in palavras:
        if palavra in opcoes:
            return True

        if palavra_parecida(palavra, opcoes):
            return True

    return False


def interpretar(comando_original):
    comando_original = comando_original.strip()
    comando = normalizar(comando_original)

    if comando == "":
        return "ajuda", ""

    if comando in ["sair", "fechar", "tchau", "ate logo"]:
        return "sair", ""

    if comando in ["ajuda", "help", "comandos", "o que posso fazer"]:
        return "ajuda", ""

    if comando in ["historico", "acontecimentos", "eventos"]:
        return "historico", ""

    if comando in ["personalidade", "sua personalidade", "como e sua personalidade"]:
        return "personalidade", ""

    if comando in ["perfil", "perfil do nunu", "quem e o nunu"]:
        return "perfil", ""
    
    if comando in ["evolucao", "evolução", "nivel", "nível", "xp"]:
        return "evolucao", ""

    if comando in ["diario", "diário", "meu diario", "meu diário", "registros emocionais"]:
        return "listar_diario", ""

    if comando in ["resumo emocional", "resumo do diario", "resumo do diário", "como estou emocionalmente"]:
        return "resumo_diario", ""

    gatilhos_diario = [
        "registrar diario ",
        "registrar diário ",
        "diario ",
        "diário ",
        "hoje eu ",
        "hoje foi ",
        "estou me sentindo ",
        "me sinto "
    ]

    for gatilho in gatilhos_diario:
        gatilho_normalizado = normalizar(gatilho)

        if comando.startswith(gatilho_normalizado):
            return "registrar_diario", comando_original

    if comando in ["lembretes", "meus lembretes", "alarmes", "meus alarmes"]:
        return "listar_lembretes", ""

    gatilhos_criar_lembrete = [
        "me lembre de ",
        "criar lembrete ",
        "novo lembrete ",
        "lembrete "
    ]

    for gatilho in gatilhos_criar_lembrete:
        if comando.startswith(gatilho):
            conteudo = comando_original[len(gatilho):].strip()
            return "criar_lembrete", conteudo

    gatilhos_concluir_lembrete = [
        "concluir lembrete ",
        "marcar lembrete ",
        "finalizar lembrete "
    ]

    for gatilho in gatilhos_concluir_lembrete:
        if comando.startswith(gatilho):
            conteudo = comando_original[len(gatilho):].strip()
            return "concluir_lembrete", conteudo

    gatilhos_remover_lembrete = [
        "apagar lembrete ",
        "remover lembrete ",
        "deletar lembrete ",
        "excluir lembrete "
    ]

    for gatilho in gatilhos_remover_lembrete:
        if comando.startswith(gatilho):
            conteudo = comando_original[len(gatilho):].strip()
            return "remover_lembrete", conteudo

    gatilhos_nome = [
        "adotar ",
        "meu nome e ",
        "me chama de ",
        "pode me chamar de ",
        "eu sou "
    ]

    for gatilho in gatilhos_nome:
        if comando.startswith(gatilho):
            nome = comando_original[len(gatilho):].strip()
            return "adotar", nome

    if comando in ["memorias", "lembrancas"]:
        return "memorias", ""

    if comando.startswith("lembrar "):
        return "lembrar", comando_original[8:].strip()

    if comando.startswith("lembra que "):
        return "lembrar", comando_original[11:].strip()

    if comando.startswith("guarde que "):
        return "lembrar", comando_original[11:].strip()

    if comando.startswith("guardar "):
        return "lembrar", comando_original[8:].strip()

    if comando in ["status", "estado", "meu status", "status do nunu"]:
        return "status", ""

    perguntas_humor = [
        "humor",
        "como voce esta",
        "como vc esta",
        "como voce ta",
        "como vc ta",
        "como esta",
        "como ta"
    ]

    if comando in perguntas_humor:
        return "humor", ""

    frases_observar = [
        "observar",
        "se observa",
        "o que voce percebe",
        "o que vc percebe",
        "o que esta sentindo",
        "o que voce sente"
    ]

    if comando in frases_observar:
        return "observar", ""

    cumprimentos = [
        "oi",
        "ola",
        "eai",
        "bom dia",
        "boa tarde",
        "boa noite"
    ]

    if comando in cumprimentos:
        return "oi", ""

    palavras_acordar = [
        "acordar",
        "acorda",
        "despertar",
        "desperta",
        "levanta"
    ]

    if contem_palavra_parecida(comando, palavras_acordar):
        return "acordar", ""

    palavras_carinho = [
        "carinho",
        "carinh",
        "cafune",
        "abraco",
        "acariciar",
        "beijinho",
        "colo"
    ]

    if contem_palavra_parecida(comando, palavras_carinho):
        return "carinho", ""

    palavras_comida = [
        "comer",
        "come",
        "comida",
        "alimentar",
        "alimento",
        "lanche",
        "lanchinho",
        "fome"
    ]

    if contem_palavra_parecida(comando, palavras_comida):
        return "comer", ""

    palavras_brincar = [
        "brincar",
        "brinca",
        "jogar",
        "joga",
        "divertir",
        "diversao"
    ]

    if contem_palavra_parecida(comando, palavras_brincar):
        return "brincar", ""

    palavras_dormir = [
        "dormir",
        "dorme",
        "descansar",
        "descansa",
        "sono",
        "cochilo",
        "cochilar"
    ]

    if contem_palavra_parecida(comando, palavras_dormir):
        return "dormir", ""

    if comando.startswith("conversar "):
        return "conversar", comando_original[10:].strip()

    return "conversar", comando_original