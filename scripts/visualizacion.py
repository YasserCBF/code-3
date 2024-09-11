import pandas as pd
import matplotlib.pyplot as plt

def graficar_ventas(ventas):
    # Graficar total de ventas por mes
    ventas['fecha'] = pd.to_datetime(ventas['fecha'])
    ventas['mes'] = ventas['fecha'].dt.to_period('M')
    ventas_mensuales = ventas.groupby('mes')['precio_total'].sum()

    plt.figure(figsize=(10, 5))
    ventas_mensuales.plot(kind='bar')
    plt.title('Total de Ventas por Mes')
    plt.xlabel('Mes')
    plt.ylabel('Total Ventas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Cargar datos
    ventas = pd.read_csv('../data/ventas.csv')
    
    # Graficar ventas
    graficar_ventas(ventas)