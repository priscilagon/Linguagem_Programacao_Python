# Projeto 5 – Amazônia Bank: Mini-Banco Digital

| Ficha do projeto |  |
| --- | --- |
| **Tema** | Sistema bancário com POO, arquivos e login |
| **Nível** | ★★★★★ |
| **Conteúdos** | Aulas 1 a 19: classes e objetos, métodos, atributos, dicionário de objetos, arquivos, funções, menus aninhados e validações |
| **Tempo sugerido** | 12 a 16 horas |
| **Organização** | dupla |

## Cenário

Uma cooperativa de crédito de Manaus quer lançar o **Amazônia Bank**, um mini-banco digital de terminal. Cada cliente cria uma conta com **senha de 4 dígitos**, faz login e realiza **depósitos, saques, transferências** e consulta **saldo e extrato**. Os dados das contas devem **permanecer salvos em arquivo**.

Este é o **projeto final do curso**: ele integra todos os conteúdos, incluindo a **Programação Orientada a Objetos**. Os valores são **fictícios**.

## Objetivos de aprendizagem

- Modelar o domínio com **classes**, atributos e métodos.
- Manter um **dicionário de objetos** (`titular → Conta`).
- Persistir e recarregar os dados com **arquivos**.
- Construir **menus aninhados** com autenticação.
- Aplicar validações e regras de negócio bancárias.

## Requisitos funcionais

| Código | O sistema deve... |
| --- | --- |
| RF01 | Criar a classe **`Conta`** com os atributos `titular`, `senha`, `saldo` (inicial 0) e `historico` (lista de movimentações). |
| RF02 | Implementar os métodos **`depositar(valor)`**, **`sacar(valor)`** e **`transferir(destino, valor)`**, que devolvem `True` (operação realizada) ou `False`, e atualizam o `historico`. |
| RF03 | Implementar **`extrato()`**, que mostra as movimentações da sessão e o saldo atual, e **`autenticar(senha)`**. |
| RF04 | **Menu principal**: 1 – Criar conta, 2 – Entrar, 0 – Sair. |
| RF05 | **Menu da conta** (após o login): 1 – Saldo, 2 – Depositar, 3 – Sacar, 4 – Transferir, 5 – Extrato, 0 – Sair da conta. |
| RF06 | **Persistir** as contas em `contas.txt` (`titular;senha;saldo`) após cada criação e cada operação financeira, e **carregá-las** ao iniciar. |
| RF07 | Organizar o código com a classe `Conta` e **funções** para carregar, salvar, criar conta e menus. |

## Regras de negócio

| Código | Regra |
| --- | --- |
| RN01 | Titular padronizado com `strip()` e `title()`; **não pode ser vazio, conter `;` nem repetir** um titular existente. |
| RN02 | A senha deve ter **exatamente 4 dígitos numéricos**. |
| RN03 | Login só é aceito com **titular existente e senha correta**; caso contrário, “Titular ou senha inválidos.” |
| RN04 | Depósito, saque e transferência exigem **valor maior que zero**. |
| RN05 | Não é permitido **sacar ou transferir mais do que o saldo**. |
| RN06 | A transferência exige **conta de destino existente** e **diferente da conta de origem**; registra movimentação nas duas contas. |
| RN07 | O saldo deve ser exibido sempre com **duas casas decimais**. |

## Exemplo de execução

Trecho de uma execução (o que o usuário digita aparece após os dois pontos):

```text

=== AMAZÔNIA BANK - MINI-BANCO DIGITAL ===
1 - Criar conta
2 - Entrar
0 - Sair
Escolha: 1
Nome do titular: marina silva
Senha (4 dígitos): 1234
Conta criada com sucesso para Marina Silva!

=== AMAZÔNIA BANK - MINI-BANCO DIGITAL ===
1 - Criar conta
2 - Entrar
0 - Sair
Escolha: 1
Nome do titular: joão pedro
Senha (4 dígitos): 12ab
A senha deve ter exatamente 4 dígitos numéricos.

=== AMAZÔNIA BANK - MINI-BANCO DIGITAL ===
1 - Criar conta
2 - Entrar
0 - Sair
Escolha: 1
Nome do titular: JOÃO PEDRO
Senha (4 dígitos): 4321
Conta criada com sucesso para João Pedro!

```

## O que entregar

- Arquivo `projeto5_amazonia_bank.py` (VS Code) **ou** notebook `Projeto5_AmazoniaBank.ipynb` (Colab, com o Drive montado).
- Quadro de **testes** com, no mínimo, 8 casos (incluindo persistência) e **registro de colaboração** da dupla.
- **Apresentação oral** de 5 a 7 minutos: demonstração, explicação da classe `Conta` e das decisões de projeto.

## Critérios de avaliação

| Critério | O que será observado |
| --- | --- |
| Funcionamento | Criação de conta, login e todas as operações financeiras funcionando. |
| POO | Classe `Conta` com atributos e métodos coerentes; objetos usados corretamente. |
| Persistência | Contas salvas e recarregadas; saldos corretos após reiniciar. |
| Regras de negócio | RN01 a RN07 implementadas. |
| Organização, testes e apresentação | Código legível, testes completos e boa comunicação oral. |

## Dicas

- Guarde as contas em um dicionário: `contas = {"Marina Silva": Conta(...)}`; assim, `titular in contas` é a verificação de existência.
- Faça `depositar`, `sacar` e `transferir` **devolverem `True` ou `False`**: o menu decide a mensagem e quando salvar.
- Na transferência, o objeto de destino é passado como argumento: `conta.transferir(contas[nome_destino], valor)`.
- Use `senha.isdigit()` e `len(senha) == 4` para validar a senha.
- Guardar senha em texto puro serve **apenas para estudo**: em sistemas reais, ela é protegida por *hash*.

## Desafios extras (opcionais)

- **Histórico em arquivo:** persista as movimentações para que o extrato sobreviva ao fechamento.
- **Tentativas:** bloqueie o login após 3 senhas incorretas seguidas.
- **Tarifa:** cobre R$ 2,00 por saque (se houver saldo suficiente).
- **Classe `Banco`:** encapsule o dicionário de contas e as operações de carregar/salvar.

## Por onde começar

1. Leia o enunciado inteiro e planeje em pseudocódigo.
2. Abra o arquivo inicial em [`starter/projeto05_amazonia_bank.py`](starter/projeto05_amazonia_bank.py).
3. Implemente um requisito por vez e teste.
4. Preencha o [quadro de testes](testes/quadro_de_testes.md).
