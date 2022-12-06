from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap

admin_email = "admin@gmail.com"
admin_password = "123456789"

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "some secret string"


class LoginForm(FlaskForm):
    email = StringField("Enter Your Email", validators=[DataRequired(), Email()])
    password = PasswordField("Enter Your Password",  validators=[DataRequired(), Length(min=8)])
    log_in = SubmitField("Log In")


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["POST", "GET"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == admin_email and login_form.password.data == admin_password:
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)

if __name__ == '__main__':
    app.run(debug=True)