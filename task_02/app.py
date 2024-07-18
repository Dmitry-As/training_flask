from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = '0c2ae4784b520f17912ae00c2ae4784b520f17912ae0f214cac'


@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('greeting'))
    else:
        return redirect(url_for('login'))
    
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username', 'email') 
        return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/greeting/')
def greeting():
    return render_template('greeting.html')


@app.route('/acou_guitars/')
def aguitars():
    context = {'title': 'Акустические гитары'}
    return render_template('acou_guitars.html', **context)


@app.route('/elec_guitars/')
def eguitars():
    context = {'title': 'Гитары электрические'}
    guitar_list = [
        {
            "description": "Электрогитара, цвет санберст, корпус - тополь, гриф - окуоме, накладка грифа - палисандр",
            "img": "electro_g.jpeg"
        },
        {
            "description": "Электрогитара, корпус из агатиса в черном цвете, кленовый гриф",
            "img": "electro_g2.jpg"
        },
        {
            "description": "Электрогитара, цвет санберст, глянцевое покрытие, хромированная фурнитура, корпус из тополя, гриф из клена",
            "img": "electro_g3.jpg"
        },
        ]
    return render_template('elec_guitars.html', **context, eleguitars=guitar_list)


@app.route('/amplifiers/')
def amplifiers():
    context = {'title': 'Усилители'}
    amplifiers_list = [
        {
            "description": "Усилитель гитарный ламповый 40Вт",
            "img": "amplif.jpg"
        },
        {
            "description": "Усилитель гитарный транзисторный 10Вт",
            "img": "amplif2.jpg"
        },
        ]
    return render_template('amplifiers.html', **context, ampli=amplifiers_list)


if __name__ == '__main__':
    app.run(debug=True)