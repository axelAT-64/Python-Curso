from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Datos de ejemplo para el card
    data = {
        "usuario": "Juan Pérez",
        "ventas": 45,
        "visitas": 120
    }
    return render_template('home.html', data=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/acerca')
def acerca():
    return render_template('acerca.html')

if __name__ == '__main__':
    app.run(debug=True)
