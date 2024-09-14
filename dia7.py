def tabuada(numero):
    for i in range(10):
        print(f"{numero} x {i+1} = {numero*(i+1)}")
        
num = int(input("digite um numero "))
tabuada(num)