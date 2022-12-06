from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

coffee_choices = ["☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"]
wifi_choices = ["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"]
power_choices = ["✘",'🔌','🔌🔌','🔌🔌🔌','🔌🔌🔌🔌', '🔌🔌🔌🔌🔌']

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google maps (URL)', validators=[DataRequired(), URL()])
    open = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close = StringField('Closing Time e.g. 10PM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=coffee_choices ,validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Rating',choices=wifi_choices ,validators=[DataRequired()])
    power_rating = SelectField('Power Socket Availability',choices=power_choices ,validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", "a", encoding="utf8") as file:
            file.write(f"\n{form.cafe.data},{form.location.data},{form.open.data},{form.close.data},{form.coffee_rating.data},{form.wifi_rating.data},{form.power_rating.data}")
            return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes' ,methods=['POST', 'GET'])
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
