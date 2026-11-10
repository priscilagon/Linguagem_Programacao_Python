# 🖥️ Projetos com interface gráfica (1 a 10)

Os dez projetos integradores, agora com **janelas** (botões, tabelas e gráficos) feitas com o **`tkinter`**, que já vem com o Python e roda direto no **VS Code**.

## Como funciona

Cada projeto tem **três partes separadas**, como em um sistema de verdade:

| Parte | Arquivo | Quem faz |
| --- | --- | --- |
| **Tela** (o que o usuário vê) | `app.py` | Já vem pronta |
| **Lógica** (regras de negócio) | `logica.py` | **Você** |
| **Testes** (conferem a lógica) | `testes_logica.py` | Já vêm prontos |

A tela chama as funções do `logica.py`. Enquanto uma função não estiver pronta, a janela abre e avisa **“Falta implementar”**, então dá para evoluir **uma função por vez** e ver o resultado na tela.

## Passo a passo (em qualquer projeto)

```bash
cd projetos-graficos/projeto-01-caixa-da-feira
python -m unittest -v testes_logica.py   # mostra o que falta
python app.py                            # abre a janela
```

1. Implemente uma função de `logica.py`.
2. Rode os testes até ficarem todos **OK**.
3. Abra `python app.py` e experimente.

> **Requisitos:** Python 3.8 ou superior com `tkinter`. No Linux: `sudo apt install python3-tk`. Teste com `python -m tkinter`.

## Os 10 projetos

| Projeto | Nível | Aulas | Tempo |
| --- | --- | --- | --- |
| [1 – Caixa da Feira do Produtor](projeto-01-caixa-da-feira/) | ★☆☆☆☆ | Aulas 1 a 10 | 4 a 6 horas |
| [2 – Monitor Fluvial: Nível do Rio Negro](projeto-02-monitor-fluvial/) | ★★☆☆☆ | Aulas 1 a 14 | 6 a 8 horas |
| [3 – Estoque da Cooperativa Ribeirinha](projeto-03-estoque-da-cooperativa/) | ★★★☆☆ | Aulas 1 a 16 | 8 a 10 horas |
| [4 – Boletim Escolar Digital](projeto-04-boletim-escolar-digital/) | ★★★★☆ | Aulas 1 a 17 | 8 a 12 horas |
| [5 – Amazônia Bank: Mini-Banco Digital](projeto-05-amazonia-bank/) | ★★★★★ | Aulas 1 a 20 | 12 a 16 horas |
| [6 – Quiz da Floresta Amazônica](projeto-06-quiz-da-floresta-amazonica/) | ★☆☆☆☆ | Aulas 1 a 10 | 4 a 6 horas |
| [7 – Meu Orçamento Familiar](projeto-07-meu-orcamento-familiar/) | ★★☆☆☆ | Aulas 1 a 14 | 6 a 8 horas |
| [8 – Forca Amazônica](projeto-08-forca-amazonica/) | ★★★☆☆ | Aulas 1 a 16 | 8 a 10 horas |
| [9 – Agenda de Contatos Comunitária](projeto-09-agenda-de-contatos-comunitaria/) | ★★★★☆ | Aulas 1 a 17 | 10 a 12 horas |
| [10 – Biblioteca Comunitária](projeto-10-biblioteca-comunitaria/) | ★★★★★ | Aulas 1 a 20 | 12 a 16 horas |

Os enunciados em modo texto (com `input()` e `print()`) continuam em [`../projetos-integradores/`](../projetos-integradores/). As regras de negócio são as mesmas.

## Estrutura de cada projeto

```text
projeto-NN-tema/
├── README.md           ← enunciado, funções a implementar e desafios extras
├── app.py              ← tela (pronta)
├── logica.py           ← SEU trabalho
├── testes_logica.py    ← testes automáticos
├── ui_comum.py         ← cores e utilitários de tela
└── capturas/tela.png   ← como a tela deve ficar
```

## Caderno em Word

Todos os enunciados em um único arquivo: [`../material/Projetos_Graficos_Caderno_do_Aluno.docx`](../material/Projetos_Graficos_Caderno_do_Aluno.docx).

## Desafios extras

Quem terminar pode mexer no `app.py`: novos botões, gráficos no `Canvas`, atalhos de teclado e exportação de arquivos. Cada README sugere três desafios.
