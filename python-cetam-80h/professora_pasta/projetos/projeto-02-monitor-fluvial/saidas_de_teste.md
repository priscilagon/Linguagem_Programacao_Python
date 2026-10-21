# Saídas de teste – Projeto 2

## com um valor inválido em janeiro e três consultas

**Entradas:** `45` → `26.1` → `27.4` → `28.3` → `29` → `29.6` → `29.8` → `29.2` → `27.9` → `25.7` → `23.8` → `23.1` → `24` → `  jun ` → `xyz` → `FIM`

```text
=== MONITOR FLUVIAL - RIO NEGRO ===
Nível em Jan (m): 45
Valor inválido! Digite entre 0 e 40 metros.
Nível em Jan (m): 26.1
Nível em Fev (m): 27.4
Nível em Mar (m): 28.3
Nível em Abr (m): 29
Nível em Mai (m): 29.6
Nível em Jun (m): 29.8
Nível em Jul (m): 29.2
Nível em Ago (m): 27.9
Nível em Set (m): 25.7
Nível em Out (m): 23.8
Nível em Nov (m): 23.1
Nível em Dez (m): 24

--- ESTATÍSTICAS DO ANO ---
Média anual: 26.99 m
Maior nível: 29.8 m em Jun
Menor nível: 23.1 m em Nov

--- RELATÓRIO MENSAL ---
Jan | 26.1 m | Enchente/Vazante | ##########################
Fev | 27.4 m | Enchente/Vazante | ###########################
Mar | 28.3 m | Enchente/Vazante | ############################
Abr | 29.0 m | Cheia | #############################
Mai | 29.6 m | Cheia | #############################
Jun | 29.8 m | Cheia | #############################
Jul | 29.2 m | Cheia | #############################
Ago | 27.9 m | Enchente/Vazante | ###########################
Set | 25.7 m | Seca | #########################
Out | 23.8 m | Seca | #######################
Nov | 23.1 m | Seca | #######################
Dez | 24.0 m | Seca | ########################

--- MESES POR CLASSIFICAÇÃO ---
Cheia: 4
Enchente/Vazante: 4
Seca: 4

Maior subida: +1.3 m em Fev

Consultar mês (ou 'fim'):   jun 
Jun: 29.8 m - Cheia

Consultar mês (ou 'fim'): xyz
Mês não encontrado.

Consultar mês (ou 'fim'): FIM
Monitoramento encerrado.
```
