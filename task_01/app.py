from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = {'title': 'My store'}
    return render_template('index.html', **context)


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
