# Preparando o ambiente

Você pode programar em Python de duas formas neste curso. O ideal é conhecer as duas.

## Opção 1 – Google Colab (sem instalação)

1. Acesse **colab.research.google.com** e entre com sua conta Google.
2. Para abrir um notebook deste repositório, clique no botão **Abrir no Colab** no `README.md` da aula (ou abra o arquivo `.ipynb` e use o botão do GitHub).
3. Execute uma célula com **Shift + Enter**.
4. Para guardar suas alterações, use **Arquivo → Salvar uma cópia no Drive**.

> ⚠️ As variáveis ficam na memória do ambiente. Se o Colab desconectar, execute as células de cima para baixo. Arquivos `.txt` criados no Colab **desaparecem** ao fim da sessão: monte o Google Drive (veja a Aula 17).

## Opção 2 – Visual Studio Code (no seu computador)

1. Baixe o Python em **python.org**. **No Windows, marque “Add python.exe to PATH”** na instalação.
2. Confirme no terminal: `python --version` (no Linux/macOS, `python3 --version`; no Windows também funciona `py --version`).
3. Instale o VS Code em **code.visualstudio.com**.
4. Em **Extensões** (Ctrl + Shift + X), instale **Python** (Microsoft).
5. Abra a **pasta** do projeto (**Arquivo → Abrir Pasta**), crie ou abra um arquivo `.py` e execute com o botão ▶ ou no terminal com `python arquivo.py`.

## Baixando este repositório

```bash
git clone https://github.com/priscilagon/python-cetam-80h.git
cd python-cetam-80h
```

Ou clique em **Code → Download ZIP** na página do repositório.

## Simulando as entradas do teclado

```bash
python tools/simular_entrada.py caminho/do/programa.py caminho/das/entradas.txt
```

Cada linha do arquivo de entradas responde a um `input()`, na ordem.

## Problemas comuns

| Sintoma | Causa provável | Solução |
| --- | --- | --- |
| “python não é reconhecido como comando” | Python fora do PATH | Reinstale marcando “Add python.exe to PATH” |
| O ▶ não executa o arquivo | Extensão Python não instalada ou interpretador não selecionado | Instale a extensão; use Ctrl + Shift + P → Python: Select Interpreter |
| Arquivo `.txt` não é encontrado (VS Code) | A pasta do projeto não foi aberta | Use Arquivo → Abrir Pasta |
| Variável sumiu (Colab) | Sessão reiniciada | Execute as células de cima para baixo |
| `NameError` | Variável não criada ou escrita diferente | Confira a grafia e a ordem de execução |
