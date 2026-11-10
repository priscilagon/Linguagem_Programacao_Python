"""Projeto 4 – Boletim Escolar Digital (regras de negócio).

PARTE LÓGICA: sem print() nem input(). A tela (app.py) já está pronta.
Cada aluno é um dicionário  {"nome": str, "notas": [n1, n2, n3]}.
No arquivo boletim.txt cada linha é:  nome;nota1;nota2;nota3
Regra violada  ->  raise ValueError("mensagem para o usuário").

Teste:  python -m unittest -v testes_logica.py      Tela:  python app.py
"""
import os

ARQUIVO = "boletim.txt"


def calcular_media(notas):
    """RN02: média = soma das notas / quantidade de notas."""
    # >>> SOLUCAO
    return sum(notas) / len(notas)
    # <<< SOLUCAO


def situacao(media):
    """RN02: 'Aprovado' (>= 7), 'Recuperação' (>= 5 e < 7) ou 'Reprovado' (< 5)."""
    # >>> SOLUCAO
    if media >= 7:
        return "Aprovado"
    if media >= 5:
        return "Recuperação"
    return "Reprovado"
    # <<< SOLUCAO


def validar_nota(nota):
    """RN01: a nota deve estar entre 0 e 10 (inclusive). Retorna a nota."""
    # >>> SOLUCAO
    if nota < 0 or nota > 10:
        raise ValueError("Nota inválida! Digite um valor entre 0 e 10.")
    return nota
    # <<< SOLUCAO


def cadastrar_aluno(alunos, nome, notas):
    """RF03, RN01, RN03 e RN04: valida e acrescenta o aluno à lista. Retorna o aluno.

    Erros: nome vazio, nome com ';', nome repetido (ignore maiúsculas/minúsculas
    — o nome é padronizado com strip() e title()) ou nota fora de 0 a 10.
    """
    # >>> SOLUCAO
    nome = nome.strip().title()
    if nome == "":
        raise ValueError("O nome não pode ser vazio.")
    if ";" in nome:
        raise ValueError("O nome não pode conter ponto e vírgula (;).")
    if any(a["nome"] == nome for a in alunos):
        raise ValueError(f"O aluno {nome} já está cadastrado.")
    for nota in notas:
        validar_nota(nota)
    aluno = {"nome": nome, "notas": list(notas)}
    alunos.append(aluno)
    return aluno
    # <<< SOLUCAO


def buscar_aluno(alunos, nome):
    """RF05: retorna o aluno com esse nome (sem diferenciar maiúsculas) ou None."""
    # >>> SOLUCAO
    alvo = nome.strip().title()
    for aluno in alunos:
        if aluno["nome"] == alvo:
            return aluno
    return None
    # <<< SOLUCAO


def estatisticas(alunos):
    """RF06 e RN05: retorna {'media_turma', 'melhor_nome', 'melhor_media', 'situacoes'}.

    'situacoes' é um dicionário contador {'Aprovado': n, 'Recuperação': n, 'Reprovado': n}.
    Lista vazia: ValueError("Nenhum aluno cadastrado.").
    """
    # >>> SOLUCAO
    if not alunos:
        raise ValueError("Nenhum aluno cadastrado.")
    medias = [calcular_media(a["notas"]) for a in alunos]
    melhor = max(range(len(alunos)), key=lambda i: medias[i])
    contagem = {"Aprovado": 0, "Recuperação": 0, "Reprovado": 0}
    for m in medias:
        contagem[situacao(m)] += 1
    return {
        "media_turma": sum(medias) / len(medias),
        "melhor_nome": alunos[melhor]["nome"],
        "melhor_media": medias[melhor],
        "situacoes": contagem,
    }
    # <<< SOLUCAO


def salvar_alunos(alunos, arquivo=ARQUIVO):
    """RF03 e RN06: grava uma linha  nome;n1;n2;n3  por aluno (modo 'w', encoding utf-8)."""
    # >>> SOLUCAO
    with open(arquivo, "w", encoding="utf-8") as f:
        for a in alunos:
            f.write(a["nome"] + ";" + ";".join(str(n) for n in a["notas"]) + "\n")
    # <<< SOLUCAO


def carregar_alunos(arquivo=ARQUIVO):
    """RF01: lê o arquivo e retorna a lista de alunos. Arquivo inexistente -> lista vazia."""
    # >>> SOLUCAO
    alunos = []
    if not os.path.exists(arquivo):
        return alunos
    with open(arquivo, encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if linha:
                partes = linha.split(";")
                alunos.append({"nome": partes[0], "notas": [float(n) for n in partes[1:]]})
    return alunos
    # <<< SOLUCAO


def exportar_relatorio(alunos, arquivo="relatorio.txt"):
    """RF07: grava  nome;média;situação  por aluno (média com 2 casas). Retorna nº de linhas."""
    # >>> SOLUCAO
    with open(arquivo, "w", encoding="utf-8") as f:
        for a in alunos:
            media = calcular_media(a["notas"])
            f.write(f"{a['nome']};{media:.2f};{situacao(media)}\n")
    return len(alunos)
    # <<< SOLUCAO
