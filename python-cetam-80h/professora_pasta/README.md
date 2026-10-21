# Pasta do professor (NÃO é publicada)

Esta pasta está listada no `.gitignore`: **o Git ignora tudo o que está aqui**, então ela **não vai para o GitHub** com `git add .` e `git push`. Mantenha-a apenas no seu computador (ou em um repositório **privado** à parte).

## Conteúdo

- `gabaritos/` – gabarito de todas as atividades, aula por aula, com saídas executadas.
- `projeto-integrador/` – soluções de referência de cada versão (v1 a v6) da Agência Amazônia Tur Digital.
- `projetos/` – solução, casos de teste, matriz de correção e erros frequentes dos 10 projetos integradores (1 a 10).
- `material/` – gabarito oficial da apostila e cadernos de projetos com gabarito, Volume 1 e Volume 2 (`.docx`).

## Antes de publicar, confira

```bash
git status          # a pasta _professor/ NÃO deve aparecer
git check-ignore -v _professor/README.md
```

> ⚠️ Os arquivos `material/Projetos_Integradores_com_Gabarito.docx` e `material/Projetos_Integradores_Vol2_com_Gabarito.docx` contêm o **gabarito**. Para entregar o caderno aos alunos, use uma cópia sem a seção “Exclusivo do professor”.
