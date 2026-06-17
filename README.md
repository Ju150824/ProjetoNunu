# Nunu

Nunu é um projeto de pet virtual em desenvolvimento.

A ideia é criar um companheiro digital com personalidade própria, emoções simuladas, memória e interações afetivas. Inicialmente, o Nunu funciona pelo terminal, mas o objetivo futuro é evoluir para uma interface gráfica, aplicativo mobile e, posteriormente, um corpo físico com sensores, voz e impressão 3D.

## Versão atual

Nunu v0.7

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
- Comando para observar o próprio estado
- Comando para expressar humor atual
- Pensamentos espontâneos ocasionais

## Estrutura do projeto

```txt
Nunu/
├── main.py
├── pet.py
├── memoria.py
├── cerebro.py
├── intencoes.py
├── vida.py
├── dados.json
└── README.md

Arquivos principais
main.py

Arquivo principal do projeto. Controla o loop de interação com o usuário e chama as funções dos outros módulos.

pet.py

Contém as ações básicas do Nunu, como comer, brincar, dormir, acordar, receber carinho, conversar e guardar memórias.

memoria.py

Responsável por carregar, atualizar e salvar os dados do Nunu no arquivo dados.json.

cerebro.py

Responsável pelo motor emocional do Nunu. Analisa os estados internos e gera respostas baseadas no humor, fome, sono, energia, apego e curiosidade.

intencoes.py

Responsável por interpretar frases do usuário e transformar em intenções. Isso permite que o Nunu entenda comandos escritos de formas diferentes.

vida.py

Responsável pelo ciclo de vida do Nunu. Calcula o tempo longe do usuário, aplica efeitos de ausência, registra interações e mantém um histórico recente.

dados.json

Arquivo onde ficam salvos os dados persistentes do Nunu, incluindo estado emocional, informações do usuário, personalidade, memórias, histórico e sistema.

Comandos disponiveis
adotar SEU_NOME
meu nome é SEU_NOME
oi
status
como você está?
observar
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

Como executar
No terminal, dentro da pasta do projeto:
python main.py
py main.py


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