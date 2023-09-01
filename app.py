from flask import Flask, render_template
import pyodbc

app = Flask(__name__)

# Configura la conexión a la base de datos Access
conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                      r'DBQ=C:\Users\ASUS\Documents\GitHub\buenas practicas\Parcial1\TallerDB.accdb;')

@app.route('/')
def index():
    return "¡Bienvenido a la aplicación de TallerDB!"

@app.route('/estudiantes')
def listar_estudiantes():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Estudiantes')
    estudiantes = cursor.fetchall()
    return render_template('estudiantes.html', estudiantes=estudiantes)

@app.route('/cursos')
def listar_cursos():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Cursos')
    cursos = cursor.fetchall()
    return render_template('cursos.html', cursos=cursos)

if __name__ == '__main__':
    app.run(debug=True)
