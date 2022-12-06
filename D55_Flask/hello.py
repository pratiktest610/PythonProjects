from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def mod_function():
        return f'<b>{function()}</b>'
    return mod_function


def make_italic(function):
    def mod_function():
        return f'<i>{function()}</i>'
    return mod_function


def make_emphasis(function):
    def mod_function():
        return f'<em>{function()}</em>'
    return mod_function


def make_underline(function):
    def mod_function():
        return f'<u>{function()}</u>'
    return mod_function


@app.route('/')
@make_bold
@make_emphasis
@make_italic
@make_underline
def hello_world():
    return '<h1>Hello, World!</h1>' \
           '<p>Well come back.</p>'


@app.route("/<name>")
def greet(name):
    return f"Hello, {name}!!"

if __name__ == "__main__":
    app.run(debug=True)
