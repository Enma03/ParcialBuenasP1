from flask import Flask, render_template
import pyodbc

# Creación de una instancia de la aplicación Flask
app = Flask(__name__)

# Configuración de la conexión a la base de datos Access
# Asegúrate de reemplazar la ruta con la ubicación correcta de tu archivo .accdb
conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                      r'DBQ=C:\Users\ASUS\Documents\GitHub\buenas practicas\Parcial1\TallerDB.accdb;')

# Ruta principal de la aplicación
@app.route('/')
def index():
    """
    Ruta principal que da la bienvenida y muestra las rutas disponibles.
    """
    return "¡Bienvenido a la aplicación de TallerDB!<br>Lista Estudiantes: /estudiantes<br>Lista Cursos: /cursos"

# Ruta para mostrar la lista de estudiantes
@app.route('/estudiantes')
def listar_estudiantes():
    """
    Ruta que obtiene y muestra la lista de estudiantes desde la tabla 'Estudiantes' en la base de datos.
    """
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Estudiantes')
    estudiantes = cursor.fetchall()
    return render_template('estudiantes.html', estudiantes=estudiantes)

# Ruta para mostrar la lista de cursos
@app.route('/cursos')
def listar_cursos():
    """
    Ruta que obtiene y muestra la lista de cursos desde la tabla 'Cursos' en la base de datos.
    """
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Cursos')
    cursos = cursor.fetchall()
    return render_template('cursos.html', cursos=cursos)

# Verifica si el script se está ejecutando como el programa principal
if __name__ == '__main__':
    # Inicia la aplicación Flask en modo de depuración (debug)
    app.run(debug=True)
