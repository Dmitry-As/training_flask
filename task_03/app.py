from flask import Flask, render_template, request, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_wtf.csrf import CSRFProtect
from models import db, User


app = Flask(__name__)
app.secret_key = '0c2ae4784b520f17912ae00c2ae4784b520f17912ae0f214cac'
app.config['SECRET_KEY'] = 'cjOINd0xvJgqyr92$44838273c440afe3dfba273181a89a5e41c9e5772d4ca1e0c97deeca413cca3a1a'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db.init_app(app)


class RegistrationForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired(), Length(min=2, max=50)])
    usersurname = StringField('Фамилия', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    passwd = PasswordField('Пароль', validators=[DataRequired(), Length(min=8)])
    confirm_passwd = PasswordField('Подтвердите Пароль', validators=[DataRequired(), EqualTo('passwd')])
    submit = SubmitField('Зарегистрироваться')



@app.before_request
def init_db():
    db.create_all()
  

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


@app.route('/register/', methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        usersurname = form.usersurname.data
        email = form.email.data
        passwd = form.passwd.data
        existing_usr = User.query.filter_by(email = email).first()
        if existing_usr:
            exist_msg = 'Данный email уже создан.'
            form.email.errors.append(exist_msg)
            return render_template('register.html', form=form)
        new_user = User(username=username, usersurname=usersurname, email=email, password=passwd)
        new_user.set_passwd(passwd)
        new_user = User.write_data(new_user)
        return render_template('sucssesreg.html')
    return render_template('register.html', form=form)


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