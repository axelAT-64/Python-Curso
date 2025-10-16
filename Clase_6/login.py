from flask import Blueprint, request, jsonify

login = Blueprint('login', __name__)

@login.route('/login', methods=['POST'])
def login_user():
    user = request.json.get('user')
    password = request.json.get('password')
    print("headers:", request.headers)
    print(f"Usuario: {user}, Password: {password}")

    codRes, menRes, accion = login_func(user, password)  # llamada a la funcion login

    salida = {
        "codRes": codRes,
        "menRes": menRes,
        "user": user,
        "accion": accion
    }
    return jsonify(salida)


def login_func(user, password):
    userLocal = "AxelAma"
    passLocal = "unida123"
    codRes = "SIN_ERROR"
    menRes = "OK"
    accion = ""

    try:
        print("Verificar login")
        if user == userLocal and password == passLocal:
            print("Login exitoso")
            accion = "Success"
        else:
            print("Usuario o contraseña incorrectos")
            codRes = "ERROR"
            menRes = "Usuario o contraseña incorrecto"
            print("Login fallido")

    except Exception as e:
        print("ERROR", str(e))
        codRes = "ERROR"
        menRes = 'Msg: ' + str(e)
        accion = "Error interno"

    return codRes, menRes, accion
