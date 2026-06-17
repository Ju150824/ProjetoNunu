# Nunu

Nunu é um projeto de pet virtual em desenvolvimento.

A ideia é criar um companheiro digital com personalidade própria, emoções simuladas, memória e interações afetivas. Inicialmente, o Nunu começou pelo terminal, mas agora também possui uma primeira interface visual em desktop.

## Versão atual

Nunu v0.9

## Visão do projeto

O Nunu não é apenas um chatbot. Ele está sendo pensado como um pet virtual semi-inteligente, capaz de criar vínculo com o usuário através de:

- estados emocionais;
- memória persistente;
- personalidade própria;
- respostas variadas;
- interações por comandos e frases naturais;
- comportamento baseado em humor;
- percepção de passagem de tempo;
- modo acordado/dormindo;
- personalidade evolutiva;
- interface visual;
- evolução gradual.

No futuro, a ideia é que o Nunu possa funcionar como um companheiro de mesa, com aparência física, sensores de toque, voz, alarmes, conexão com internet e respostas inteligentes.

## Funcionalidades atuais

- Sistema de adoção
- Sistema de humor
- Sistema de energia
- Sistema de fome
- Sistema de apego
- Sistema de curiosidade
- Sistema de sono
- Modo acordado e modo dormindo
- Percepção de ausência do usuário
- Recuperação de energia durante o sono
- Memória salva em arquivo JSON
- Histórico recente de acontecimentos
- Respostas aleatórias
- Motor emocional básico
- Interpretação de intenção
- Diálogo emocional
- Personalidade evolutiva
- Primeira interface visual em desktop
- Botões de interação
- Campo de conversa
- Status visual
- Expressões faciais simples
- Pensamentos espontâneos ocasionais

## Estrutura do projeto

```txt
Nunu/
├── main.py
├── app.py
├── pet.py
├── memoria.py
├── cerebro.py
├── intencoes.py
├── vida.py
├── personalidade.py
├── dialogo.py
├── dados.json
└── README.md

Arquivos principais
main.py

Versão em terminal do Nunu.

app.py

Primeira interface visual do Nunu em desktop. Possui rosto, chat, botões de interação e status na tela.

pet.py

Contém as ações básicas do Nunu, como comer, brincar, dormir, acordar, receber carinho, conversar e guardar memórias.

memoria.py

Responsável por carregar, atualizar e salvar os dados do Nunu no arquivo dados.json.

cerebro.py

Responsável pelo motor emocional do Nunu. Analisa os estados internos e gera respostas baseadas no humor, fome, sono, energia, apego, curiosidade e personalidade.

intencoes.py

Responsável por interpretar frases do usuário e transformar em intenções. Isso permite que o Nunu entenda comandos escritos de formas diferentes.

vida.py

Responsável pelo ciclo de vida do Nunu. Calcula o tempo longe do usuário, aplica efeitos de ausência, registra interações e mantém um histórico recente.

personalidade.py

Responsável por controlar os traços de personalidade do Nunu e permitir que ele evolua conforme as interações.

dialogo.py

Responsável por respostas mais emocionais e naturais durante conversas livres.

dados.json

Arquivo onde ficam salvos os dados persistentes do Nunu, incluindo estado emocional, informações do usuário, personalidade, memórias, histórico e sistema.

Como executar no terminal
py main.py

ou:

python main.py
Como executar com interface visual
py app.py

ou:

python app.py

adotar SEU_NOME
meu nome é SEU_NOME
oi
status
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
vai descansar
acordar
acorda, Nunu
conversar MENSAGEM
lembrar ALGO
lembra que ALGO
memorias
historico
sair

Objetivo futuro

O objetivo é evoluir o Nunu em fases:

Pet virtual no terminal
Interface gráfica para desktop
Aplicativo mobile
Interação por voz
Integração com IA
Sistema de alarmes e lembretes
Acesso à internet
Versão física com Raspberry Pi, sensores de toque, microfone, alto-falante e corpo impresso em 3D
Status

Projeto em desenvolvimento.