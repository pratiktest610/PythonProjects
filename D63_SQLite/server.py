from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, )
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<book {self.title}>"

db.create_all()

# new_book = Book(title="pqr", author="xyz", rating=9.5)
# db.session.add(new_book)
# db.session.commit()

print(db.session.query(Book).all())
print(Book.query.filter_by(title="abc").first())

# book_to_update = Book.query.filter_by(title="abc").first()
# book_to_update.id = "ijk"
# print(db.session.query(Book).all())

book_to_delete = Book.query.filter_by(title="pqr").first()
db.session.delete(book_to_delete)
print(db.session.query(Book).all())