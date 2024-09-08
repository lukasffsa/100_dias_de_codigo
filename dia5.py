numero1 = float(input("digite um numero: "))
numero2 = float(input("digite o segundo numero: "))
operador = str(input("selecione uma opçao de operador: +, -, *, /: "))
if(operador == "+"):
    print(f"A soma {numero1} + {numero2} é igual a {numero1+numero2}")
elif(operador == "-"):
    print(f"A subtração {numero1} - {numero2} é igual a {numero1-numero2}")
elif(operador == "*"):
    print(f"A multiplicação {numero1} * {numero2} é igual a {numero1*numero2}")
elif(operador == "/"):
    print(f"A divisão de {numero1} / {numero2} é igual a {numero1/numero2}")
else:
    print("operador invalido!")