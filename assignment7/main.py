<<<<<<< HEAD
from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
=======
from flask import Flask,render_template , request
from wtforms import StringField,PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, Email


>>>>>>> 05592bb9d8684e9834f41ffcc74e0cf8bacc07b6
app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'

class RegisterForm(FlaskForm):
    name = StringField("name", validators=[InputRequired()])
    last = StringField("last", validators=[InputRequired()])
    email = StringField("Email",  [InputRequired("Please enter your email address."), Email("Please enter your email again.")])
    username = StringField("username", validators=[InputRequired()])
    password = PasswordField("password", validators=[InputRequired(), Length(min=8,max=12, message="Please enter your password 8-12 characters.")])

<<<<<<< HEAD
class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

@app.route("/")
def redirect():
    return render_template('login.html')

@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('submit.html', form=form)

if __name__ == '__main__':
    app.run()
=======
@app.route('/')
def member():
    form = RegisterForm()
    return render_template('login.html', form=form)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return "Register OK"
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 05592bb9d8684e9834f41ffcc74e0cf8bacc07b6
