import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Practicas/co2.csv')
filtered_data = data[data['Year'] >= 2020]
# Se crea una nueva columna de tipo datetime que contiene Year-Month-Day -> que se asigna valor 1 a todos los meses
filtered_data['Date'] = pd.to_datetime(filtered_data[['Year', 'Month']].assign(Day=1))
""" 
# Basico sin seaborn
plt.plot(filtered_data['Date'], filtered_data['CO2_Level'])
plt.show()
"""
# Opcion avanzada con seaborn
plt.figure(figsize=(12, 6))
sns.lineplot(data=filtered_data, x='Date', y='CO2_Level', marker='o', label='CO2 Level (ppm)')
plt.title('Nivel de CO2 en los ultimos 4 años') # Titulo del grafico
plt.xlabel('Fecha', fontsize=11) # Texto en el eje X
plt.ylabel('Nivel de CO2(ppm)', fontsize=11) # Texto en el eje Y
#plt.xticks(rotation=45) #: Mejora la legibilidad de las etiquetas en el eje X al girarlas 45 grados.
plt.legend() #: Añade una leyenda al gráfico para explicar qué representan las diferentes líneas o categorías.
plt.tight_layout() #: Ajusta los márgenes del gráfico automáticamente para evitar superposiciones o elementos fuera de los bordes.
plt.show()
