# Aula 13 | Validar e-mail e CPF fictício pelo formato.
# Entradas de teste sugeridas: marina@email.com | 12345678901

email = input("E-mail: ").strip().lower()
if "@" in email and "." in email:
    print("E-mail com formato aceitável.")
else:
    print("E-mail inválido.")

cpf = input("CPF fictício (só números): ")
if len(cpf) == 11 and cpf.isdigit():
    print("CPF com formato válido.")
else:
    print("CPF deve ter 11 dígitos numéricos.")
