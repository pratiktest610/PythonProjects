from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

api_key = '3967504e58bbb9509f1808196609ea77'

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-list.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)

class EditForm(FlaskForm):
    new_rating = StringField("You rating out of 10 e.g. 7.5", validators=[DataRequired()])
    new_review = StringField("Your review", validators=[DataRequired()])
    done = SubmitField("DONE")

class AddForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    ADD = SubmitField("ADD MOVIE")


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(1000), nullable=True)
    img_url = db.Column(db.String(1000), unique=True, nullable=False)

db.create_all()

@app.route("/")
def home():
    movies = db.session.query(Movie).order_by(Movie.rating).all()
    i = 0
    movies.reverse()
    for movie in movies:
        i += 1
        movie.ranking = i 
    movies.reverse()
    return render_template("index.html", movies=movies)

@app.route("/edit/<id>", methods=["POST", "GET"])
def edit(id):
    form = EditForm()
    movie_to_update = Movie.query.get(id)
    if form.validate_on_submit():
        movie_to_update.rating = form.new_rating.data
        movie_to_update.review = form.new_review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form, title=movie_to_update.title)

@app.route("/delete/<id>")
def delete(id):
    movie_to_delete = Movie.query.get(id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/add", methods=["POST", "GET"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        api_url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}'
        title = form.title.data
        response = requests.get(api_url, params={"query": title})
        movies = response.json()["results"]
        return render_template("select.html", movies=movies)
    return render_template("add.html", form=form)

@app.route("/fetch-data/<movie_id>")
def fetch_data(movie_id):
    api_url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    response = requests.get(api_url)
    data = response.json()
    new_movie = Movie(title=data["title"], year=data["release_date"].split("-")[0], description=data["overview"], rating=data["vote_average"], img_url=data["poster_path"])
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("edit", id=new_movie.id, title=new_movie.title))

if __name__ == '__main__':
    app.run(debug=True)
