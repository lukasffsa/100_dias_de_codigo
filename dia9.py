import numpy as np
import pandas as pd

data = {
    'vendas' : [10.00, 100.00, 250.00, 38.00, 900.70] 
}

df = pd.DataFrame(data)

media = df['vendas'].mean()
mediana = df['vendas'].median()
desvio_padrao = df['vendas'].std()
maximo =  df['vendas'].max()
minimmo = df['vendas'].min()

print(f"A media das vendas é {media}")
print(f"A mediana das vendas é {mediana}")
print(f"O desvio padrão das vendas é {desvio_padrao}")
print(f"A minimo das vendas é {minimmo}")
print(f"O maximo das vendas é {maximo}")

