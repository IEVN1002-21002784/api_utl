 
from flask import Flask, jsonify
from flask_mysqldb import MySQL
from config import config
 
app = Flask(__name__)
con = MySQL(app)
 
@app.route('/alumnos', methods=['GET'])
def lista_alumnos():
    try:
        cursor = con.connection.cursor()
        sql = 'SELECT * FROM alumnos'
        cursor.execute(sql)
        datos = cursor.fetchall()  # Corregido
        alumnos = []
        for fila in datos:
            alumno = {'matricula': fila[0], 'nombre': fila[1], 'apaterno': fila[2], 'amaterno': fila[3], 'correo': fila[4]}
            alumnos.append(alumno)
        return jsonify({'alumnos': alumnos, 'mensaje': 'Lista de alumnos', 'exito': True})
    except Exception as ex:
        return jsonify({"message": "Error al conectar a la base de datos: {}".format(ex), 'exito': False})
 
def pagina_no_encontrada(error):
    return "<h1>La página que buscas no existe</h1>", 404
 
if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.config['MYSQL_SSL_DISABLED'] = True
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(host='0.0.0.0', port=5000)
 
 