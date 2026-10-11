# Aula 17 – Arquivos .txt

> **Fase 5 – Modularização e Persistência** • 4 horas

[![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/priscilagon/python-cetam-80h/blob/main/aulas/fase-5-modularizacao-e-persistencia/aula-17-arquivos-txt/aula-17.ipynb)

## O que você vai estudar

- **Objeto do conhecimento:** uso de arquivos `.txt`: leitura e escrita, modos de arquivos e formatos
- **Habilidade a desenvolver:** abranger a escrita de dados em arquivos, com satisfação
- **Avaliação:** formativa

## Resumo da aula

- Modos: `"r"` leitura, `"w"` escrita (**apaga o anterior**), `"a"` acréscimo.
- Use `with open(..., encoding="utf-8") as arquivo:` — o arquivo é fechado automaticamente.
- Para guardar vários dados por linha, use um separador (`;`).
- **Colab:** os arquivos somem ao fim da sessão (monte o Google Drive). **VS Code:** abra a **pasta** do projeto.

## Exemplos

| Arquivo | O que mostra |
| --- | --- |
| [`01_escrever_e_ler.py`](exemplos/01_escrever_e_ler.py) | Gravar uma lista e ler de volta. |
| [`02_salvar_e_carregar_clientes.py`](exemplos/02_salvar_e_carregar_clientes.py) | Persistência de registros com separador ;. |
| [`03_google_drive_no_colab.py`](exemplos/03_google_drive_no_colab.py) | Somente no Colab: montar o Google Drive (não executa fora do Colab). |

Para rodar um exemplo no terminal: `python exemplos/01_escrever_e_ler.py`.

## Exercícios

👉 [exercicios/enunciados.md](exercicios/enunciados.md)

## Notebook

👉 [aula-17.ipynb](aula-17.ipynb)

---
⬅️ [Aula 16](../aula-16-parametros-retorno-e-escopo/) • [Aula 18](../../fase-6-poo-e-integracao/aula-18-fundamentos-de-poo/) ➡️
