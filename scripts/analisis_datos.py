import pandas as pd

def analisis_ventas(ventas):
    # Análisis básico de ventas
    total_ventas = ventas['precio_total'].sum()
    total_transacciones = ventas['id_venta'].nunique()
    return total_ventas, total_transacciones

if __name__ == "__main__":
    # Cargar datos
    ventas = pd.read_csv('../data/ventas.csv')
    
    # Realizar análisis
    total_ventas, total_transacciones = analisis_ventas(ventas)
    print(f'Total Ventas: {total_ventas}')
    print(f'Total Transacciones: {total_transacciones}')