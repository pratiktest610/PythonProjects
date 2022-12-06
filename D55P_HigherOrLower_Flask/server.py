from flask import Flask
import random

number = random.randint(0, 9)
app = Flask(__name__)


@app.route("/")
def homepage():
    return '<h1 style="text-align: center; color: #6FEDD6;">Guess a number between 0 & 9</h1>' \
           '<div style="text-align: center;"><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></div>'


@app.route("/<int:guess>")
def check_guess(guess):
    if guess < number:
        return '<h1 style="text-align: center; color: #6FEDD6;">Too Low</h1>' \
               '<div style="text-align: center;"><img src=" https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif></div>'
    elif guess > number:
        return '<h1 style="text-align: center; color: #6FEDD6;">Too High</h1>' \
               '<div style="text-align: center;"><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"></div>'
    else:
        return '<h1 style="text-align: center; color: #6FEDD6;">You Got It !!!</h1>' \
               '<div style="text-align: center;"><img src=" https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"></div>'


if __name__ == "__main__":
    app.run(debug=True)
