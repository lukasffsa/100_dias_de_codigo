numero1 = float(input("digite um numero: "))
numero2 = float(input("digite o segundo numero: "))
operador = str(input("selecione uma opçao de operador: +, -, *, /: "))
if(operador == "+"):
    print(f"A soma de {numero1} + {numero2} é {numero1+numero2}")
elif(operador == "-"):
    print(f"A subtração de {numero1} - {numero2} é {numero1-numero2}")
elif(operador == "*"):
    print(f"A multiplicação de {numero1} * {numero2} é {numero1*numero2}")
elif(operador == "/"):
    print(f"A divisão de {numero1} / {numero2} é {numero1/numero2}")
else:
    print("operador invalido!")