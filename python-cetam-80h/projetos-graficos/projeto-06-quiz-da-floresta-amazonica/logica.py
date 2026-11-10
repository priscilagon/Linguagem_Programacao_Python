"""Projeto 6 – Quiz da Floresta Amazônica (regras de negócio).

PARTE LÓGICA: sem print() nem input(). A tela (app.py) já está pronta.
Regra violada  ->  raise ValueError("mensagem para o usuário").

Teste:  python -m unittest -v testes_logica.py      Tela:  python app.py
"""

PERGUNTAS = [
    {"texto": "Quais rios formam o Encontro das Águas, em Manaus?",
     "alternativas": ["A) Madeira e Purus", "B) Negro e Solimões", "C) Tapajós e Xingu", "D) Juruá e Japurá"],
     "correta": "B"},
    {"texto": "Qual peixe amazônico pode ultrapassar 2 metros de comprimento?",
     "alternativas": ["A) Tambaqui", "B) Pirarucu", "C) Jaraqui", "D) Matrinxã"],
     "correta": "B"},
    {"texto": "O Festival Folclórico de Parintins reúne quais bois-bumbás?",
     "alternativas": ["A) Garantido e Caprichoso", "B) Mimoso e Caprichoso", "C) Garantido e Mimoso", "D) Faceiro e Caprichoso"],
     "correta": "A"},
    {"texto": "Em qual cidade fica o Teatro Amazonas?",
     "alternativas": ["A) Belém", "B) Manaus", "C) Parintins", "D) Santarém"],
     "correta": "B"},
    {"texto": "Qual é o rio de maior volume de água do mundo?",
     "alternativas": ["A) Nilo", "B) Mississippi", "C) Amazonas", "D) Yangtzé"],
     "correta": "C"},
]

PONTOS_ACERTO = 10
BONUS = 5
SEGUIDOS_BONUS = 3


def validar_resposta(texto):
    """RN01: aceita a, B, ' c ' ... e retorna a letra MAIÚSCULA. Fora de A–D: ValueError."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def conferir(pergunta, resposta):
    """RF03: True se a resposta (já validada) for a alternativa correta da pergunta."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def calcular_pontos(acertos):
    """RN02 e RN03: recebe a lista de resultados [True, False, ...] na ordem das perguntas.

    Cada acerto vale 10. A cada 3 acertos SEGUIDOS ganha +5 de bônus e a contagem de
    seguidos recomeça do zero. Qualquer erro também zera a contagem. Retorna os pontos.
    """
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def titulo(pontos):
    """RN04: 'Guardião da Floresta' (>= 50), 'Explorador' (30 a 49) ou 'Aprendiz' (< 30)."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def novo_recorde(pontos, melhor):
    """RN05: True quando os pontos da partida são MAIORES que a melhor pontuação."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")
