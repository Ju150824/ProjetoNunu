import tkinter as tk
from tkinter import scrolledtext
import io
from contextlib import redirect_stdout

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
    pensamento_espontaneo,
    analisar_humor
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


class NunuApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Nunu - Pet Virtual")
        self.janela.geometry("850x600")
        self.janela.configure(bg="#f6eef7")

        self.dados = carregar_dados()
        self.dados["pet"]["versao"] = "0.9"

        self.nome = self.dados["pet"]["nome"]

        self.criar_interface()

        self.adicionar_mensagem_sistema(f"{self.nome} v0.9 iniciado.")
        self.adicionar_mensagem_sistema("Digite algo ou use os botões para interagir.")

        self.executar_com_saida(aplicar_ausencia, self.dados)
        self.atualizar_status_visual()
        self.atualizar_rosto()

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_app)

    def criar_interface(self):
        self.container_principal = tk.Frame(self.janela, bg="#f6eef7")
        self.container_principal.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        self.frame_esquerdo = tk.Frame(self.container_principal, bg="#f6eef7")
        self.frame_esquerdo.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 15))

        self.frame_direito = tk.Frame(self.container_principal, bg="#ffffff")
        self.frame_direito.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.label_nome = tk.Label(
            self.frame_esquerdo,
            text="Nunu",
            font=("Arial", 24, "bold"),
            bg="#f6eef7",
            fg="#7b3b7a"
        )
        self.label_nome.pack(pady=(10, 5))

        self.label_rosto = tk.Label(
            self.frame_esquerdo,
            text="(•ᴗ•)",
            font=("Arial", 48),
            bg="#f6eef7",
            fg="#7b3b7a"
        )
        self.label_rosto.pack(pady=10)

        self.label_humor = tk.Label(
            self.frame_esquerdo,
            text="Humor: tranquilo",
            font=("Arial", 12),
            bg="#f6eef7",
            fg="#4b2b4b"
        )
        self.label_humor.pack(pady=(0, 15))

        self.frame_status = tk.Frame(self.frame_esquerdo, bg="#ffffff", padx=10, pady=10)
        self.frame_status.pack(fill=tk.X, pady=10)

        self.label_status = tk.Label(
            self.frame_status,
            text="",
            font=("Arial", 10),
            bg="#ffffff",
            fg="#333333",
            justify=tk.LEFT
        )
        self.label_status.pack()

        self.frame_botoes = tk.Frame(self.frame_esquerdo, bg="#f6eef7")
        self.frame_botoes.pack(pady=10)

        self.criar_botao("Carinho", "carinho", 0, 0)
        self.criar_botao("Comer", "comer", 0, 1)
        self.criar_botao("Brincar", "brincar", 1, 0)
        self.criar_botao("Dormir", "dormir", 1, 1)
        self.criar_botao("Acordar", "acordar", 2, 0)
        self.criar_botao("Status", "status", 2, 1)
        self.criar_botao("Humor", "humor", 3, 0)
        self.criar_botao("Perfil", "perfil", 3, 1)

        self.area_chat = scrolledtext.ScrolledText(
            self.frame_direito,
            wrap=tk.WORD,
            font=("Arial", 11),
            bg="#ffffff",
            fg="#222222",
            height=25
        )
        self.area_chat.pack(fill=tk.BOTH, expand=True, padx=15, pady=(15, 10))
        self.area_chat.configure(state="disabled")

        self.frame_entrada = tk.Frame(self.frame_direito, bg="#ffffff")
        self.frame_entrada.pack(fill=tk.X, padx=15, pady=(0, 15))

        self.entrada = tk.Entry(
            self.frame_entrada,
            font=("Arial", 12),
            bg="#f7f7f7",
            fg="#222222"
        )
        self.entrada.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8)
        self.entrada.bind("<Return>", self.enviar_mensagem)

        self.botao_enviar = tk.Button(
            self.frame_entrada,
            text="Enviar",
            font=("Arial", 11, "bold"),
            bg="#d9a7d8",
            fg="#ffffff",
            activebackground="#c589c4",
            activeforeground="#ffffff",
            relief=tk.FLAT,
            command=self.enviar_mensagem
        )
        self.botao_enviar.pack(side=tk.RIGHT, padx=(10, 0), ipadx=15, ipady=7)

    def criar_botao(self, texto, comando, linha, coluna):
        botao = tk.Button(
            self.frame_botoes,
            text=texto,
            width=11,
            font=("Arial", 10, "bold"),
            bg="#e9c7e8",
            fg="#4b2b4b",
            activebackground="#d9a7d8",
            relief=tk.FLAT,
            command=lambda: self.processar_comando(comando, mostrar_usuario=False)
        )
        botao.grid(row=linha, column=coluna, padx=5, pady=5)

    def adicionar_texto_chat(self, texto):
        self.area_chat.configure(state="normal")
        self.area_chat.insert(tk.END, texto + "\n")
        self.area_chat.see(tk.END)
        self.area_chat.configure(state="disabled")

    def adicionar_mensagem_usuario(self, texto):
        self.adicionar_texto_chat(f"Você: {texto}")

    def adicionar_mensagem_sistema(self, texto):
        self.adicionar_texto_chat(f"Sistema: {texto}")

    def adicionar_resposta_nunu(self, texto):
        if texto.strip():
            self.adicionar_texto_chat(texto.strip())

    def capturar_saida(self, funcao, *args):
        buffer = io.StringIO()

        with redirect_stdout(buffer):
            funcao(*args)

        return buffer.getvalue()

    def executar_com_saida(self, funcao, *args):
        saida = self.capturar_saida(funcao, *args)

        if saida.strip():
            self.adicionar_resposta_nunu(saida)

    def pode_interagir_dormindo(self, intencao):
        return intencao in [
            "sair",
            "ajuda",
            "status",
            "humor",
            "observar",
            "acordar",
            "historico",
            "personalidade",
            "perfil"
        ]

    def enviar_mensagem(self, event=None):
        comando = self.entrada.get().strip()

        if comando == "":
            return

        self.entrada.delete(0, tk.END)
        self.processar_comando(comando, mostrar_usuario=True)

    def processar_comando(self, comando, mostrar_usuario=True):
        if mostrar_usuario:
            self.adicionar_mensagem_usuario(comando)

        intencao, conteudo = interpretar(comando)

        modo_atual = self.dados["pet"].get("modo", "acordado")

        if modo_atual == "dormindo" and not self.pode_interagir_dormindo(intencao):
            self.adicionar_resposta_nunu(
                f"{self.nome}: zzz... estou dormindo agora. Se precisar de mim, tente me acordar."
            )
            passar_tempo(self.dados)
            registrar_interacao(self.dados)
            salvar_dados(self.dados)
            self.atualizar_status_visual()
            self.atualizar_rosto()
            return

        if intencao == "sair":
            self.fechar_app()
            return

        elif intencao == "ajuda":
            self.mostrar_ajuda()

        elif intencao == "adotar":
            self.executar_com_saida(adotar, self.dados, conteudo)

        elif intencao == "oi":
            self.executar_com_saida(cumprimentar, self.dados)

        elif intencao == "status":
            self.executar_com_saida(mostrar_status, self.dados)

        elif intencao == "humor":
            self.executar_com_saida(mostrar_humor, self.dados)

        elif intencao == "observar":
            self.executar_com_saida(observar, self.dados)

        elif intencao == "personalidade":
            self.executar_com_saida(mostrar_personalidade, self.dados)

        elif intencao == "perfil":
            self.executar_com_saida(mostrar_perfil, self.dados)

        elif intencao == "carinho":
            self.executar_com_saida(dar_carinho, self.dados)

        elif intencao == "comer":
            self.executar_com_saida(alimentar, self.dados)

        elif intencao == "brincar":
            self.executar_com_saida(brincar, self.dados)

        elif intencao == "dormir":
            self.executar_com_saida(dormir, self.dados)

        elif intencao == "acordar":
            self.executar_com_saida(acordar, self.dados)

        elif intencao == "lembrar":
            self.executar_com_saida(lembrar, self.dados, conteudo)

        elif intencao == "memorias":
            self.executar_com_saida(mostrar_memorias, self.dados)

        elif intencao == "historico":
            self.executar_com_saida(mostrar_historico, self.dados)

        elif intencao == "conversar":
            self.executar_com_saida(conversar, self.dados, conteudo)

        self.executar_ciclo_final()

    def executar_ciclo_final(self):
        saida_tempo = self.capturar_saida(passar_tempo, self.dados)

        if saida_tempo.strip():
            self.adicionar_resposta_nunu(saida_tempo)

        registrar_interacao(self.dados)
        salvar_dados(self.dados)

        saida_pensamento = self.capturar_saida(pensamento_espontaneo, self.dados)

        if saida_pensamento.strip():
            self.adicionar_resposta_nunu(saida_pensamento)

        self.atualizar_status_visual()
        self.atualizar_rosto()

    def mostrar_ajuda(self):
        texto = """
--- O que o Nunu entende ---
meu nome é Ana
oi
como você está?
observar
personalidade
perfil
carinho
quero fazer carinho em você
comer
come alguma coisa
brincar
vamos brincar
dormir
acordar
conversar hoje foi um dia difícil
lembra que eu gosto de tecnologia
memorias
historico
sair
----------------------------
"""
        self.adicionar_resposta_nunu(texto)

    def atualizar_status_visual(self):
        estado = self.dados["estado"]
        modo = self.dados["pet"].get("modo", "acordado")
        humor_atual = analisar_humor(self.dados)

        texto_status = (
            f"Modo: {modo}\n"
            f"Humor: {estado['humor']}/100\n"
            f"Energia: {estado['energia']}/100\n"
            f"Fome: {estado['fome']}/100\n"
            f"Apego: {estado['apego']}/100\n"
            f"Curiosidade: {estado['curiosidade']}/100\n"
            f"Sono: {estado['sono']}/100"
        )

        self.label_status.config(text=texto_status)
        self.label_humor.config(text=f"Humor: {humor_atual}")

    def atualizar_rosto(self):
        humor_atual = analisar_humor(self.dados)

        rostos = {
            "dormindo": "(-_-) zZ",
            "faminto": "(ó﹏ò)",
            "sonolento": "(－.－) zz",
            "exausto": "(×_×)",
            "triste": "(｡•́︿•̀｡)",
            "carente": "(つ﹏<。)",
            "apegado": "(づ｡◕‿‿◕｡)づ",
            "curioso": "(•ิ_•ิ)?",
            "feliz": "(＾▽＾)",
            "animado": "ヽ(＾▽＾)ﾉ",
            "tranquilo": "(•ᴗ•)"
        }

        self.label_rosto.config(text=rostos.get(humor_atual, "(•ᴗ•)"))

    def fechar_app(self):
        registrar_interacao(self.dados)
        salvar_dados(self.dados)
        self.janela.destroy()


if __name__ == "__main__":
    janela = tk.Tk()
    app = NunuApp(janela)
    janela.mainloop()