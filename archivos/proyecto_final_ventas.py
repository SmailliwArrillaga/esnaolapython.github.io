#%%
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

path = "ventas.xlsx"

ventas=pd.read_excel(path, nrows=100)

print(ventas)


#Promedio de Ventas basado en la columna "Importe venta total"
promedioVentas= sum(ventas["Importe venta total"])/len(ventas["Importe venta total"])
print(f'El promedio de las ventas es {promedioVentas}')


#%%
#Pedidos con importe mayor a 1.000.000, tomando las columnas de Fecha Pedido, ID Pedido, Importe Venta Total

ventas=pd.read_excel(path, usecols=["ID Pedido","Fecha pedido", "Importe venta total"], nrows=20)
pedidos_un_millon = ventas[ventas["Importe venta total"] > 1000000]
print(pedidos_un_millon)

#Pedidos con importe entre 200000 y 500000, tomando las columnas de Fecha Pedido, ID Pedido, Importe Venta Total
ventas=pd.read_excel(path, usecols=["ID Cliente","Fecha pedido", "Importe venta total"], nrows=20)
pedidos_rango = ventas[ventas["Importe venta total"].between(200000,500000) ]

print(f"\n{pedidos_rango}")

plt.bar(pedidos_rango["ID Cliente"], pedidos_rango["Importe venta total"])
plt.xlabel("ID Pedido")
plt.ylabel("Importe venta total")
plt.title("Pedidos con importe entre 200,000 y 500,000")

plt.xticks(rotation=20, ha="right")

plt.show()


# %%

#Agrupamos y contamos los pedidos por Zona
ventas = pd.read_excel(path, nrows=100)
zona = ventas.groupby(["Zona"]).agg(Conteo_pedidos=('Zona', 'count')).reset_index()
print(zona)

colores = ['red', 'blue', 'orange', 'purple', 'black', 'skyblue']

plt.bar(zona["Zona"], zona["Conteo_pedidos"], color=colores)
plt.xlabel("Zona")
plt.ylabel("Conteo de productos")
plt.title("Conteo de productos por Zona")
plt.xticks(rotation=20, ha="right")
plt.show()


# Gráfico de barras interactivas para conteo de productos por zona
fig = go.Figure(data=go.Bar(x=zona['Zona'], y=zona['Conteo_pedidos'], marker=dict(color=colores)))
fig.update_layout(title='Conteo de productos por Zona', xaxis_title='Zona', yaxis_title='Conteo de productos')

fig.show()




# %%

#Agrupamos los pedidos por el país que sea igual "Australia"
ventas=pd.read_excel(path, usecols=["ID Cliente", "Zona", "País"] ,nrows=100)
pais= ventas[ventas["País"] == "Australia"]
print(pais)
# %%
#Mostramos las ventas que sean menor a 500.000
ventas=pd.read_excel(path, usecols=["ID Cliente", "Zona", "País", "Importe venta total"] ,nrows=100)
ventas_menor= ventas[ventas["Importe venta total"] < 500000]
print(ventas_menor)
# %%
#Agrupamos las ventas por Tipo de productos y lo visualizamos en un gráfico de torta
ventas = pd.read_excel(path, usecols=[ "Tipo de producto"], nrows=100)
tipo_productos = ventas.groupby("Tipo de producto").agg(Conteo_Productos=('Tipo de producto', 'count')).reset_index()
print(tipo_productos)

plt.pie(tipo_productos['Conteo_Productos'], labels=tipo_productos['Tipo de producto'], autopct='%1.1f%%')
plt.title('Ventas por Tipo de Producto')

plt.show()

# Gráfico de torta interactiva para ventas por tipo de producto
fig = go.Figure(data=go.Pie(labels=tipo_productos['Tipo de producto'], values=tipo_productos['Conteo_Productos']))
fig.update_layout(title='Ventas por Tipo de Producto')

fig.show()

# %%
#Agregar y graficar los productos por "Cereales y Cuidado Personal"
ventas = pd.read_excel(path, usecols=["ID Cliente", "Tipo de producto", "País", "Zona"], nrows=100)
tipo_productos = ventas[ventas["Tipo de producto"].isin(["Cereales", "Cuidado personal"])]
tipo_productos = tipo_productos.groupby("Tipo de producto").agg(Conteo_Productos=('Tipo de producto', 'count')).reset_index()
print(tipo_productos)

plt.bar(tipo_productos["Tipo de producto"], tipo_productos["Conteo_Productos"])
plt.xlabel("Tipo de producto")
plt.ylabel("Conteo de productos")
plt.title("Conteo de productos por tipo")
plt.show()




# Gráfico de barras interactivas para conteo de productos por zona
colores = ['red', 'blue', 'orange', 'purple', 'black', 'skyblue']
fig = go.Figure(data=go.Bar(x=tipo_productos['Tipo de producto'], y=tipo_productos['Conteo_Productos'], marker=dict(color=colores)))
fig.update_layout(title='Conteo de productos por Zona', xaxis_title='Zona', yaxis_title='Conteo de productos')

fig.show()

# Gráfico de torta interactiva para ventas por tipo de producto
fig = go.Figure(data=go.Pie(labels=tipo_productos['Tipo de producto'], values=tipo_productos['Conteo_Productos']))
fig.update_layout(title='Ventas por Tipo de Producto')

fig.show()
# %%
