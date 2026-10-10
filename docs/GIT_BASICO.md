# Git e GitHub para o seu portfólio

Guardar seus projetos no GitHub cria um **portfólio** que você pode mostrar a empresas e professores.

## Primeiros passos

1. Crie uma conta em **github.com**.
2. Instale o Git (**git-scm.com**).
3. Configure seu nome e e-mail:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@exemplo.com"
```

## Fluxo do dia a dia

```bash
git clone <endereço-do-repositório>   # baixa o projeto
git status                            # mostra o que mudou
git add .                             # prepara as mudanças
git commit -m "Mensagem curta explicando o que mudou"
git push                              # envia para o GitHub
git pull                              # baixa novidades do GitHub
```

## Dicas

- Escreva mensagens de commit **curtas e claras** (“Adiciona validação dos dias”).
- Faça commits **pequenos e frequentes**.
- **Nunca** envie senhas, dados pessoais reais ou documentos. Use sempre dados fictícios.
- Seu repositório de portfólio deve ter um `README.md` explicando o que cada projeto faz.
