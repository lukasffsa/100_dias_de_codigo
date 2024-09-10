def fatorial(numero):
    if(numero <= 1):
        return numero
    else:
        return numero * fatorial(numero-1)

numero = int(input("digite um numero "))
print(f"o fatorial de {numero} é {fatorial(numero)}")