from datetime import datetime

def calcular_juros(valor, vencimento_str):
    vencimento = datetime.strptime(vencimento_str, "%d/%m/%Y")
    hoje = datetime.now()

    dias_atraso = (hoje - vencimento).days

    if dias_atraso <= 0:
        return 0, valor

    multa_dia = 0.025
    juros = valor * multa_dia * dias_atraso
    total = valor + juros

    return juros, total

valor = 1000
vencimento = "10/02/2025"

juros, total = calcular_juros(valor, vencimento)

print(f"Dias de atraso: { (datetime.now() - datetime.strptime(vencimento, '%d/%m/%Y')).days }")
print(f"Juros: R$ {juros:.2f}")
print(f"Total a pagar: R$ {total:.2f}")
