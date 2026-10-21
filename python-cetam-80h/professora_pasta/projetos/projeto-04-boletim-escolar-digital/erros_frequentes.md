# Erros frequentes – Projeto 4

- **Abrir o arquivo em modo `"w"` ao cadastrar sem regravar a lista inteira**, apagando os alunos anteriores.
- **Esquecer a conversão `float()`** ao ler as notas do arquivo (a média vira concatenação de textos ou gera TypeError).
- **Esquecer o `.strip()`** ao ler as linhas: o `\n` fica grudado na última nota.
- **Executar o programa em uma pasta diferente** da do arquivo (VS Code sem abrir a pasta; Colab sem montar o Drive).
- **Não tratar o arquivo inexistente** na primeira execução (FileNotFoundError).
- **Dividir a média por 3 fixo em vez de `len(notas)`** — funciona, mas dificulta alterações.
