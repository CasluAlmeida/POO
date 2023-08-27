from datetime import datetime

faturamento = 1000
print(f'O faturamento é RS{faturamento:,.2f}')

cpf = 7573454503
print(f"CPF: {cpf:011}")

margem_lucro = 0.27
print(f"Sua margem de lucro foi de {margem_lucro:.2%}")

hoje = datetime.now()
print(f"Hoje: {hoje:%d/%m/%Y}, Horário: {hoje:%H:%M - %A}\n")

texto = f"""Bom dia, diretoria

Faturamento: RS{faturamento:,.2f}
Margem de Lucro: {margem_lucro:.2%}
Data de hoje: {hoje:%d/%m/%Y}
"""
print(texto)