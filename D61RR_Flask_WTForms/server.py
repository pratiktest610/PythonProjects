from urllib import request
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired, Length
from flask_bootstrap import Bootstrap

admin_email = "admin@gmail.com"
admin_password = "123456789"

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    login = SubmitField("login")

app = Flask(__name__)
app.secret_key = "guter goo guter goo"
Bootstrap(app)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    login_form = LoginForm()
    
    if login_form.validate_on_submit():
        if login_form.email.data == admin_email and login_form.password.data == admin_password:
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)
    
if __name__ == "__main__":
    app.run(debug=True)