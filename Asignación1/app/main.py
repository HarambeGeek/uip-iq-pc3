from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def bienvenida():
    return render_template('index.html')

@app.route('/calculadora', methods = ['POST'])
def calculadora():
    if request.method == 'POST':
        #Así se comuníca con las variables de index.html?
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        ventas = float(request.form['ventas'])
        if ventas < 25000:
            comision = ventas * 0.03
        elif ventas >= 25000 and ventas < 50000:
            comision  = ventas * 0.05
        elif ventas >= 50000 and ventas < 75000:
            comision = ventas * 0.07
        elif ventas >= 75000 and ventas < 100000:
            comision = ventas * 0.1
        elif ventas >= 100000:
            comision = ventas * 0.15
        guardar = "%s, %s, %4.2f, %4.2f" %(nombre, apellido, ventas, comision)
        report = open("report.csv", "a+")
        report.write(guardar + "\n")
        report.close()

    return render_template('calculadora.html', n=nombre, a=apellido , c = comision)

@app.route('/cortex', methods = ['POST'])
def cortex():
    if request.method == 'POST':
        return redirect(url_for("bienvenida"))


if __name__ == "__main__":
    app.run(debug=True)
