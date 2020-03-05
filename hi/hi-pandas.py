# Python
import pandas as pd
import numpy as np

print("--------------------------------------")
print("Hi Pandas! Version: " + pd.__version__)
print("--------------------------------------")

raw_data = {'titulo': ['Clean Code', 'Head First Design Patterns', 'Artificial Intelligence with Python', 'Electrónica para Makers'], 
        'autor': ['Robert C. Martin', 'Eric Freeman', 'Prateek Joshi', 'Paolo Aliverti'], 
        'paginas': [464, 694, 446, 376],
        'precio': [35.40, 41.00, 45.74, 23.70],
        'puntuacion': [4.6, 4.5, 3.5, 4.4]
}
df = pd.DataFrame(raw_data, columns = ['titulo', 'autor', 'paginas', 'precio', 'puntuacion'])
print(df)

print("Precio medio:", df["precio"].mean())
print("Puntuación media:", df["puntuacion"].mean())
print("Número de páginas (máximo):", df["paginas"].max())
print("Número de páginas (mínimo):", df["paginas"].min())