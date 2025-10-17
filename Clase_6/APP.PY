from flask import Flask
from login import login #importamos el blueprint desde login.py
from logout import logout

app = Flask(__name__)
app.register_blueprint(login) #registramos el blueprint
app.register_blueprint(logout)
@app.route("/")
def home():
    return "¡Hola, mundo desde Clase_6!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5005)#favor codocar la ip de su macina local
