from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random
# import requests

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/random", methods=["GET"]) #by default already on GET, not need write methods=["GET"]
def random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes).to_dict()
    return jsonify(cafe=random_cafe)
    
@app.route("/all") #by default already on GET, not need write methods=["GET"]
def all_cafes():
    cafes = db.session.query(Cafe).all()
    cafes = [cafe.to_dict() for cafe in cafes]
    return jsonify(cafes=cafes)

@app.route("/search")
def search_cafe():
    location = request.args.get("loc")
    cafes = Cafe.query.filter_by(location=location.title()).all()
    cafes = [cafe.to_dict() for cafe in cafes]
    if cafes == []:
        return jsonify(error={"Not Found":"There are no cafe at the queried location."})
    return jsonify(cafe=cafes)

@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
    name=request.form.get("name"),
    map_url=request.form.get("map_url"),
    img_url=request.form.get("img_url"),
    location=request.form.get("location"),
    has_sockets=bool(int(request.form.get("has_sockets"))),
    has_toilet=bool(int(request.form.get("has_toilet"))),
    has_wifi=bool(int(request.form.get("has_wifi"))),
    can_take_calls=bool(int(request.form.get("can_take_calls"))),
    seats=request.form.get("seats"),
    coffee_price=request.form.get("coffee_price"),
)
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe_to_update = Cafe.query.get(cafe_id)
    new_price = request.args.get("new_price")
    if cafe_to_update:
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    cafe_to_delete = Cafe.query.get(cafe_id)
    api_key = request.args.get("api_key")
    if api_key == "TopSecretKey":
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"Success": "Cafe has been successfully removed."}), 200
        return jsonify(response={"Failed": "Cafe with queried id does not exit."}), 404
    return jsonify(error={"KeyError": "API Key does not exit."}), 403
    
        


## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
