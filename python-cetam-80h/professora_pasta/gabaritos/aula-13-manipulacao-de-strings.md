# Gabarito – Aula 13: Manipulação de strings

> **Uso exclusivo do professor.** Há mais de uma solução correta: compare o comportamento, não a forma exata. As saídas abaixo foram obtidas ao executar cada código.

## Atividade 1

> Padronize o texto `"  joão PEDRO  "` para `"João Pedro"`.

```python
texto = "  joão PEDRO  "
print(texto.strip().title())
```

**Saída esperada:**

```text
João Pedro
```

> 📝 **Nota ao professor:** `strip()` remove os espaços das pontas e `title()` coloca a inicial de cada palavra em maiúscula.

## Atividade 2

> Valide um e-mail digitado (deve conter `@` e `.`).

```python
email = input("E-mail: ").strip().lower()
if "@" in email and "." in email:
    print("E-mail com formato aceitável.")
else:
    print("E-mail inválido.")
```

**Saída esperada – e-mail válido:**

```text
E-mail: marina@email.com
E-mail com formato aceitável.
```

**Saída esperada – sem @:**

```text
E-mail: marina.email.com
E-mail inválido.
```

## Atividade 3

> Gere o código de reserva no formato `PAR-03-MA` a partir do destino, dos dias e do nome do cliente.

```python
nome = "marina costa"
destino = "Parintins"
dias = 3

codigo = f"{destino[:3].upper()}-{dias:02d}-{nome[:2].upper()}"
print(codigo)
```

**Saída esperada:**

```text
PAR-03-MA
```

## Desafio do projeto – Cadastro padronizado e recibo

> Padronizar o nome do cliente e montar o recibo da viagem com f-strings.

```python
nome = input("Nome do cliente: ").strip().title()
destino = input("Destino: ").strip().title()
dias = int(input("Dias: "))
total = float(input("Total (R$): "))

codigo = f"{destino[:3].upper()}-{dias:02d}-{nome[:2].upper()}"

print("=" * 34)
print("     RECIBO - AMAZÔNIA TUR DIGITAL")
print("=" * 34)
print(f"Cliente: {nome}")
print(f"Destino: {destino}")
print(f"Duração: {dias} dias")
print(f"Total:   R$ {total:.2f}")
print(f"Reserva: {codigo}")
```

**Saída esperada:**

```text
Nome do cliente:   marina COSTA 
Destino: parintins
Dias: 3
Total (R$): 990
==================================
     RECIBO - AMAZÔNIA TUR DIGITAL
==================================
Cliente: Marina Costa
Destino: Parintins
Duração: 3 dias
Total:   R$ 990.00
Reserva: PAR-03-MA
```

