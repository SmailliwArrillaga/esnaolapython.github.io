#%%
import pandas as pd
import matplotlib.pyplot as plt

path="clientes.xlsx"

clientes = pd.read_excel(path, usecols=['ID', 'Nombre completo', 'Grupo de clientes'], nrows=100)

print(clientes)

# Contar la cantidad de personas en cada grupo
conteo_grupos = clientes['Grupo de clientes'].value_counts().sort_index()

# Crear el gráfico de barras
colores = ['red', 'blue', 'green', 'orange', 'purple']  # Lista de colores para cada grupo

conteo_grupos.plot(kind='bar', color=colores)


# Personalizar el gráfico
plt.xlabel('Grupos de clientes')
plt.ylabel('Cantidad de personas')
plt.title('Cantidad de personas en cada grupo de clientes')

# Mostrar el gráfico
plt.show()


# %%
