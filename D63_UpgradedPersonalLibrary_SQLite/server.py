from hmac import new
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///book_library.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

db.create_all()

@app.route("/")
def homepage():
    books = db.session.query(Book).all()
    return render_template("index.html", books=books)

@app.route("/add", methods=["POST", "GET"])
def add_book():
    if request.method == "POST":
        data = request.form
        new_book = Book(title=data["title"], author=data["author"], rating=data["rating"])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('homepage'))
    return render_template("add.html")

@app.route("/edit/<id>", methods=["POST", "GET"])
def edit(id):
    book_to_edit = Book.query.get(id)
    if request.method == "POST":
        new_rating = request.form["new_rating"]
        book_to_edit.rating = new_rating
        db.session.commit()
        return redirect(url_for('homepage'))
    return render_template("edit.html", book=book_to_edit)
    
@app.route("/delete/<id>")
def delete(id):
    book_to_delete = Book.query.get(id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('homepage'))

if __name__ == "__main__":
    app.run(debug=True)