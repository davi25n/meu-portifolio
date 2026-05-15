valor1 = 0
valor2 = 0
operacao = ""
def calcular(operacao, valor1, valor2):
    valor1 = int(input("qual deve ser o primeiro valor? "))
    operacao = input("qual operação deseja realizar? ")
    valor2 = int(input("qual deve ser o segundo valor? "))
    if operacao == "+":
        return valor1 + valor2
    elif operacao == "-":
        return valor1 - valor2
    elif operacao == "*":
        return valor1 * valor2
    elif operacao == "/":
        return valor1 / valor2
    else:
        return "Operação inválida"

resultado = calcular(operacao, valor1, valor2)
if resultado%1 == 0:
    print(f"o resultado é: {int(resultado)}")
else:
    print(f"o resultado é: {resultado:.5f}")        