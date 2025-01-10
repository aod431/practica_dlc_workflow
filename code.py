import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
meteo_data = pd.read_csv("meteo.csv")

# Visualizar los datos de precipitación de los primeros 1000 días
plt.plot(range(1, 1001), meteo_data['y'][:1000], color='steelblue')
plt.xlabel("Day")
plt.ylabel("Precipitation")
plt.title("Precipitation Over First 1000 Days")
plt.show()
