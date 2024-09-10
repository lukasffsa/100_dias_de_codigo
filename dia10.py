import numpy as np
import pandas as pd

data = {
    'nome' : ['Joao', 'Maria','Paulo', 'Ana'],
    'departamento' : ['TI', "Saude", 'TI', 'RH'],
    'salario' : [3000.00, 4500.00, 7000.00, 2800.00]
}

df = pd.DataFrame(data)

ti = df[df['departamento'] == 'TI']
media = np.mean(ti['salario'])

print(f"A media salarial do departamento de TI é {media}")