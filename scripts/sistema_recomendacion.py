import pandas as pd

def recomendar_productos(ventas, productos, n=5):
    # Calcular la popularidad de los productos
    popularidad = ventas.groupby('id_producto').size().reset_index(name='cantidad_vendida')
    productos_populares = popularidad.sort_values(by='cantidad_vendida', ascending=False)
    
    # Unir con los detalles de los productos
    recomendaciones = productos.merge(productos_populares, on='id_producto', how='left')
    return recomendaciones[['id_producto', 'nombre_producto', 'cantidad_vendida']].head(n)

if __name__ == "__main__":
    # Cargar datos
    ventas = pd.read_csv('../data/ventas.csv')
    productos = pd.read_csv('../data/productos.csv')
    
    # Obtener recomendaciones
    recomendaciones = recomendar_productos(ventas, productos)
    print("Productos recomendados:")
    print(recomendaciones)