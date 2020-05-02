from flask import Flask, render_template, redirect, request, url_for
from data import db_session
from data.users import User
from flask_login import LoginManager, login_user, login_required, logout_user
from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, SelectField, IntegerField, \
    FieldList, FormField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(User).get(user_id)


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/')
def qwe():
    return render_template('index.html', style=url_for("static", filename="css/normalize.css"),
                           style2=url_for("static", filename="css/style.css"),
                           js=url_for("static", filename="js/jQuery.js"),
                           js2=url_for("static", filename="js/main.js"))

@app.route('/login')
def qe():
    return render_template('sign-in.html', style=url_for("static", filename="css/normalize.css"),
                           style2=url_for("static", filename="css/style.css"),
                           js=url_for("static", filename="js/jQuery.js"),
                           js2=url_for("static", filename="js/main.js"),
                           style3=url_for("static", filename="css/stylesu.css"),)

@app.route('/login')
def q():
    return render_template('sign-in.html', style=url_for("static", filename="css/normalize.css"),
                           style2=url_for("static", filename="css/style.css"),
                           js=url_for("static", filename="js/jQuery.js"),
                           js2=url_for("static", filename="js/main.js"),
                           style3=url_for("static", filename="css/stylesu.css"),)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')
