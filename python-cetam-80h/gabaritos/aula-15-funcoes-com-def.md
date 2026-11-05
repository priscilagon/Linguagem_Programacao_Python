# Gabarito – Aula 15: Funções com def

> **Uso exclusivo do professor.** Há mais de uma solução correta: compare o comportamento, não a forma exata. As saídas abaixo foram obtidas ao executar cada código.

## Atividade 1

> Crie a função `saudacao_cliente(nome)` que mostre “Olá, [nome]! Boa viagem!”.

```python
def saudacao_cliente(nome):
    print(f"Olá, {nome}! Boa viagem!")

saudacao_cliente("Marina")
```

**Saída esperada:**

```text
Olá, Marina! Boa viagem!
```

## Atividade 2

> Transforme o cálculo do total (dias × gasto por dia) em uma função e chame-a duas vezes com valores diferentes.

```python
def calcular_total(dias, gasto_dia):
    return dias * gasto_dia

print(calcular_total(3, 330))
print(calcular_total(5, 200))
```

**Saída esperada:**

```text
990
1000
```

> 📝 **Nota ao professor:** Verifique o uso de `return` (e não só `print`) dentro da função.

