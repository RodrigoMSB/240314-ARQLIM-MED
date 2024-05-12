from flask import Flask, request, jsonify
from repositorio_usuario import RepositorioUsuario

app = Flask(__name__)
usuario_repo = RepositorioUsuario()

@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.json
    nombre = data.get('nombre')
    correo = data.get('correo')
    contraseña = data.get('contraseña')

    if not nombre or not correo or not contraseña:
        return jsonify({'mensaje': 'Todos los campos son obligatorios'}), 400

    usuario_nuevo = usuario_repo.crear(nombre, correo, contraseña)

    if usuario_nuevo:
        return jsonify({'mensaje': 'Usuario creado exitosamente'}), 201
    else:
        return jsonify({'mensaje': 'No se pudo crear el usuario'}), 500

if __name__ == '__main__':
    app.run(debug=True)
