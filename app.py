from flask import Flask, render_template, redirect, url_for, request, session
import pandas as pd

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

# Cargar datos de productos
def cargar_productos():
    return pd.read_csv('data/productos.csv')

# Ruta para la página de inicio
@app.route('/')
def index():
    productos = cargar_productos()
    return render_template('index.html', productos=productos)

# Ruta para mostrar el formulario de login
@app.route('/login', methods=['GET'])
def login_form():
    return render_template('login.html')

# Ruta para procesar el login
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    if email == 'usuario@ejemplo.com' and password == 'contraseña':
        session['email'] = email
        return redirect(url_for('preferencias_form'))
    else:
        return render_template('login.html', error='Email o contraseña incorrectos')

# Ruta para mostrar el formulario de preferencias
@app.route('/preferencias', methods=['GET'])
def preferencias_form():
    if 'email' in session:
        return render_template('preferencias.html')
    else:
        return redirect(url_for('login_form'))

# Ruta para procesar las preferencias
@app.route('/preferencias', methods=['POST'])
def preferencias():
    if 'email' in session:
        categoria = request.form['categoria']
        
        # Cargar productos y filtrar por categoría
        productos = cargar_productos()
        productos_filtrados = productos[productos['categoria'] == categoria]
        
        return render_template('index.html', productos=productos_filtrados.to_dict(orient='records'))
    else:
        return redirect(url_for('login_form'))

# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)