import pandas as pd

def cargar_datos():
    # Cargar datos de ventas
    ventas = pd.read_csv('../data/ventas.csv')
    
    # Cargar datos de usuarios
    usuarios = pd.read_csv('../data/usuarios.csv')
    
    # Cargar datos de productos
    productos = pd.read_csv('../data/productos.csv')
    
    return ventas, usuarios, productos

if __name__ == "__main__":
    ventas, usuarios, productos = cargar_datos()
    print("Datos cargados correctamente.")
    print("Ventas:", ventas.head())
    print("Usuarios:", usuarios.head())
    print("Productos:", productos.head())