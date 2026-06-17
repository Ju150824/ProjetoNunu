import tkinter as tk
from tkinter import ttk, scrolledtext
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
        self.janela.geometry("1000x680")
        self.janela.minsize(900, 620)
        self.janela.configure(bg="#f7edf8")

        self.app_ativo = True

        self.dados = carregar_dados()
        self.dados["pet"]["versao"] = "1.0"
        self.nome = self.dados["pet"]["nome"]

        self.configurar_estilos()
        self.criar_interface()

        self.adicionar_sistema(f"{self.nome} v1.0 iniciado.")
        self.adicionar_sistema("Clique no Nunu para fazer carinho ou converse com ele pelo chat.")

        self.executar_com_saida(aplicar_ausencia, self.dados)

        self.atualizar_tudo()

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_app)

        self.agendar_pensamento_espontaneo()

    def configurar_estilos(self):
        self.estilo = ttk.Style()

        try:
            self.estilo.theme_use("clam")
        except tk.TclError:
            pass

        self.estilo.configure(
            "Nunu.Horizontal.TProgressbar",
            troughcolor="#f1d8f2",
            background="#b76ab5",
            bordercolor="#f1d8f2",
            lightcolor="#b76ab5",
            darkcolor="#b76ab5"
        )

    def criar_interface(self):
        self.container = tk.Frame(self.janela, bg="#f7edf8")
        self.container.pack(fill=tk.BOTH, expand=True, padx=18, pady=18)

        self.criar_lado_esquerdo()
        self.criar_lado_direito()

    def criar_lado_esquerdo(self):
        self.frame_esquerdo = tk.Frame(self.container, bg="#f7edf8", width=330)
        self.frame_esquerdo.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 18))
        self.frame_esquerdo.pack_propagate(False)

        self.canvas_lateral = tk.Canvas(
            self.frame_esquerdo,
            bg="#f7edf8",
            highlightthickness=0
        )

        self.scroll_lateral = tk.Scrollbar(
            self.frame_esquerdo,
            orient="vertical",
            command=self.canvas_lateral.yview
        )

        self.canvas_lateral.configure(yscrollcommand=self.scroll_lateral.set)

        self.scroll_lateral.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas_lateral.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.frame_esquerdo_conteudo = tk.Frame(self.canvas_lateral, bg="#f7edf8")

        self.janela_lateral = self.canvas_lateral.create_window(
            (0, 0),
            window=self.frame_esquerdo_conteudo,
            anchor="nw"
        )

        def atualizar_scroll(event):
            self.canvas_lateral.configure(
                scrollregion=self.canvas_lateral.bbox("all")
            )

        def ajustar_largura(event):
            self.canvas_lateral.itemconfig(
                self.janela_lateral,
                width=event.width
            )

        def rolar_mouse(event):
            self.canvas_lateral.yview_scroll(
                int(-1 * (event.delta / 120)),
                "units"
            )

        self.frame_esquerdo_conteudo.bind("<Configure>", atualizar_scroll)
        self.canvas_lateral.bind("<Configure>", ajustar_largura)

        self.canvas_lateral.bind(
            "<Enter>",
            lambda event: self.canvas_lateral.bind_all("<MouseWheel>", rolar_mouse)
        )

        self.canvas_lateral.bind(
            "<Leave>",
            lambda event: self.canvas_lateral.unbind_all("<MouseWheel>")
        )

        self.card_pet = tk.Frame(
            self.frame_esquerdo_conteudo,
            bg="#ffffff",
            bd=0,
            highlightthickness=1,
            highlightbackground="#ead4ec"
        )
        self.card_pet.pack(fill=tk.X, pady=(0, 14))

        self.label_nome = tk.Label(
            self.card_pet,
            text=self.nome,
            font=("Arial", 26, "bold"),
            bg="#ffffff",
            fg="#7b3b7a"
        )
        self.label_nome.pack(pady=(18, 2))

        self.label_modo = tk.Label(
            self.card_pet,
            text="",
            font=("Arial", 11),
            bg="#ffffff",
            fg="#8b6a8d"
        )
        self.label_modo.pack(pady=(0, 8))

        self.label_rosto = tk.Label(
            self.card_pet,
            text="(•ᴗ•)",
            font=("Arial", 58),
            bg="#ffffff",
            fg="#7b3b7a",
            cursor="hand2"
        )
        self.label_rosto.pack(pady=8)
        self.label_rosto.bind("<Button-1>", self.tocar_no_nunu)

        self.label_toque = tk.Label(
            self.card_pet,
            text="clique em mim para carinho",
            font=("Arial", 10, "italic"),
            bg="#ffffff",
            fg="#9c7b9e"
        )
        self.label_toque.pack(pady=(0, 16))

        self.label_humor = tk.Label(
            self.card_pet,
            text="Humor: tranquilo",
            font=("Arial", 12, "bold"),
            bg="#ffffff",
            fg="#4b2b4b"
        )
        self.label_humor.pack(pady=(0, 16))

        self.card_status = tk.Frame(
            self.frame_esquerdo_conteudo,
            bg="#ffffff",
            bd=0,
            highlightthickness=1,
            highlightbackground="#ead4ec"
        )
        self.card_status.pack(fill=tk.BOTH, pady=(0, 14))

        titulo_status = tk.Label(
            self.card_status,
            text="Status do Nunu",
            font=("Arial", 14, "bold"),
            bg="#ffffff",
            fg="#7b3b7a"
        )
        titulo_status.pack(anchor="w", padx=16, pady=(14, 8))

        self.barras_status = {}

        self.criar_barra_status("humor", "Humor")
        self.criar_barra_status("energia", "Energia")
        self.criar_barra_status("fome", "Fome")
        self.criar_barra_status("apego", "Apego")
        self.criar_barra_status("curiosidade", "Curiosidade")
        self.criar_barra_status("sono", "Sono")

        self.card_acoes = tk.Frame(
            self.frame_esquerdo_conteudo,
            bg="#ffffff",
            bd=0,
            highlightthickness=1,
            highlightbackground="#ead4ec"
        )
        self.card_acoes.pack(fill=tk.X)

        titulo_acoes = tk.Label(
            self.card_acoes,
            text="Ações rápidas",
            font=("Arial", 14, "bold"),
            bg="#ffffff",
            fg="#7b3b7a"
        )
        titulo_acoes.pack(anchor="w", padx=16, pady=(14, 8))

        self.frame_botoes = tk.Frame(self.card_acoes, bg="#ffffff")
        self.frame_botoes.pack(padx=12, pady=(0, 14))

        botoes = [
            ("Carinho", "carinho"),
            ("Comer", "comer"),
            ("Brincar", "brincar"),
            ("Dormir", "dormir"),
            ("Acordar", "acordar"),
            ("Observar", "observar"),
            ("Humor", "humor"),
            ("Perfil", "perfil"),
            ("Personalidade", "personalidade"),
            ("Memórias", "memorias")
        ]

        for indice, (texto, comando) in enumerate(botoes):
            linha = indice // 2
            coluna = indice % 2
            self.criar_botao_acao(texto, comando, linha, coluna)

    def criar_barra_status(self, chave, titulo):
        frame = tk.Frame(self.card_status, bg="#ffffff")
        frame.pack(fill=tk.X, padx=16, pady=5)

        linha_superior = tk.Frame(frame, bg="#ffffff")
        linha_superior.pack(fill=tk.X)

        label_titulo = tk.Label(
            linha_superior,
            text=titulo,
            font=("Arial", 10, "bold"),
            bg="#ffffff",
            fg="#4b2b4b"
        )
        label_titulo.pack(side=tk.LEFT)

        label_valor = tk.Label(
            linha_superior,
            text="0/100",
            font=("Arial", 10),
            bg="#ffffff",
            fg="#6f5c70"
        )
        label_valor.pack(side=tk.RIGHT)

        barra = ttk.Progressbar(
            frame,
            style="Nunu.Horizontal.TProgressbar",
            maximum=100,
            value=0
        )
        barra.pack(fill=tk.X, pady=(3, 0))

        self.barras_status[chave] = {
            "valor": label_valor,
            "barra": barra
        }

    def criar_botao_acao(self, texto, comando, linha, coluna):
        botao = tk.Button(
            self.frame_botoes,
            text=texto,
            width=14,
            font=("Arial", 10, "bold"),
            bg="#e9c7e8",
            fg="#4b2b4b",
            activebackground="#d9a7d8",
            activeforeground="#4b2b4b",
            relief=tk.FLAT,
            cursor="hand2",
            command=lambda: self.processar_comando(comando, mostrar_usuario=False)
        )
        botao.grid(row=linha, column=coluna, padx=5, pady=5, ipady=5)

    def criar_lado_direito(self):
        self.frame_direito = tk.Frame(
            self.container,
            bg="#ffffff",
            bd=0,
            highlightthickness=1,
            highlightbackground="#ead4ec"
        )
        self.frame_direito.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.header_chat = tk.Frame(self.frame_direito, bg="#ffffff")
        self.header_chat.pack(fill=tk.X, padx=18, pady=(16, 8))

        self.titulo_chat = tk.Label(
            self.header_chat,
            text="Conversa com o Nunu",
            font=("Arial", 18, "bold"),
            bg="#ffffff",
            fg="#7b3b7a"
        )
        self.titulo_chat.pack(side=tk.LEFT)

        self.botao_limpar = tk.Button(
            self.header_chat,
            text="Limpar chat",
            font=("Arial", 10),
            bg="#f2def3",
            fg="#7b3b7a",
            activebackground="#e9c7e8",
            relief=tk.FLAT,
            cursor="hand2",
            command=self.limpar_chat
        )
        self.botao_limpar.pack(side=tk.RIGHT)

        self.area_chat = scrolledtext.ScrolledText(
            self.frame_direito,
            wrap=tk.WORD,
            font=("Arial", 11),
            bg="#fffaff",
            fg="#222222",
            bd=0,
            highlightthickness=1,
            highlightbackground="#f1d8f2",
            padx=12,
            pady=12
        )
        self.area_chat.pack(fill=tk.BOTH, expand=True, padx=18, pady=(0, 12))
        self.area_chat.configure(state="disabled")

        self.area_chat.tag_configure("usuario", foreground="#6f3a86", font=("Arial", 11, "bold"))
        self.area_chat.tag_configure("nunu", foreground="#333333", font=("Arial", 11))
        self.area_chat.tag_configure("sistema", foreground="#8a7b8a", font=("Arial", 10, "italic"))

        self.frame_entrada = tk.Frame(self.frame_direito, bg="#ffffff")
        self.frame_entrada.pack(fill=tk.X, padx=18, pady=(0, 18))

        self.entrada = tk.Entry(
            self.frame_entrada,
            font=("Arial", 12),
            bg="#fffaff",
            fg="#222222",
            bd=0,
            highlightthickness=1,
            highlightbackground="#f1d8f2",
            highlightcolor="#d9a7d8"
        )
        self.entrada.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=11)
        self.entrada.bind("<Return>", self.enviar_mensagem)

        self.botao_enviar = tk.Button(
            self.frame_entrada,
            text="Enviar",
            font=("Arial", 11, "bold"),
            bg="#b76ab5",
            fg="#ffffff",
            activebackground="#9f519d",
            activeforeground="#ffffff",
            relief=tk.FLAT,
            cursor="hand2",
            command=self.enviar_mensagem
        )
        self.botao_enviar.pack(side=tk.RIGHT, padx=(10, 0), ipadx=18, ipady=9)

    def tocar_no_nunu(self, event=None):
        self.processar_comando("carinho", mostrar_usuario=False)

    def adicionar_texto_chat(self, texto, tag):
        self.area_chat.configure(state="normal")
        self.area_chat.insert(tk.END, texto + "\n\n", tag)
        self.area_chat.see(tk.END)
        self.area_chat.configure(state="disabled")

    def adicionar_usuario(self, texto):
        self.adicionar_texto_chat(f"Você: {texto}", "usuario")

    def adicionar_sistema(self, texto):
        self.adicionar_texto_chat(f"Sistema: {texto}", "sistema")

    def adicionar_nunu(self, texto):
        texto = texto.strip()

        if texto:
            self.adicionar_texto_chat(texto, "nunu")

    def limpar_chat(self):
        self.area_chat.configure(state="normal")
        self.area_chat.delete("1.0", tk.END)
        self.area_chat.configure(state="disabled")
        self.adicionar_sistema("Chat limpo. O Nunu ainda lembra dos dados salvos.")

    def capturar_saida(self, funcao, *args):
        buffer = io.StringIO()

        with redirect_stdout(buffer):
            funcao(*args)

        return buffer.getvalue()

    def executar_com_saida(self, funcao, *args):
        saida = self.capturar_saida(funcao, *args)

        if saida.strip():
            self.adicionar_nunu(saida)

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
            "perfil",
            "memorias"
        ]

    def enviar_mensagem(self, event=None):
        comando = self.entrada.get().strip()

        if comando == "":
            return

        self.entrada.delete(0, tk.END)
        self.processar_comando(comando, mostrar_usuario=True)

    def processar_comando(self, comando, mostrar_usuario=True):
        if mostrar_usuario:
            self.adicionar_usuario(comando)

        intencao, conteudo = interpretar(comando)
        modo_atual = self.dados["pet"].get("modo", "acordado")

        if modo_atual == "dormindo" and not self.pode_interagir_dormindo(intencao):
            self.adicionar_nunu(
                f"{self.nome}: zzz... estou dormindo agora. Se precisar de mim, tente me acordar."
            )
            passar_tempo(self.dados)
            registrar_interacao(self.dados)
            salvar_dados(self.dados)
            self.atualizar_tudo()
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
            self.adicionar_nunu(saida_tempo)

        registrar_interacao(self.dados)
        salvar_dados(self.dados)

        self.atualizar_tudo()

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

Dica: você também pode clicar no rostinho do Nunu para fazer carinho.
"""
        self.adicionar_nunu(texto)

    def atualizar_tudo(self):
        self.atualizar_status_visual()
        self.atualizar_rosto()

    def atualizar_status_visual(self):
        estado = self.dados["estado"]

        for chave, widgets in self.barras_status.items():
            valor = estado.get(chave, 0)
            widgets["valor"].config(text=f"{valor}/100")
            widgets["barra"]["value"] = valor

        modo = self.dados["pet"].get("modo", "acordado")
        humor_atual = analisar_humor(self.dados)

        self.label_modo.config(text=f"modo: {modo}")
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

    def agendar_pensamento_espontaneo(self):
        if not self.app_ativo:
            return

        self.janela.after(35000, self.executar_pensamento_espontaneo)

    def executar_pensamento_espontaneo(self):
        if not self.app_ativo:
            return

        saida = self.capturar_saida(pensamento_espontaneo, self.dados)

        if saida.strip():
            self.adicionar_nunu(saida)
            salvar_dados(self.dados)
            self.atualizar_tudo()

        self.agendar_pensamento_espontaneo()

    def fechar_app(self):
        self.app_ativo = False
        registrar_interacao(self.dados)
        salvar_dados(self.dados)
        self.janela.destroy()


if __name__ == "__main__":
    janela = tk.Tk()
    app = NunuApp(janela)
    janela.mainloop()