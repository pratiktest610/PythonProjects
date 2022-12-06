from flask import Flask, render_template
import requests
import data

# blogs_url = "https://api.npoint.io/c790b4d5cab58020d391"
# response = requests.get(url=blogs_url)
# blogs = response.json()
blogs = data.data

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html", blogs=blogs)

@app.route("/blog/<id>")
def get_blog(id):
    index =(int(id) - 1)
    return render_template("blog.html", blog=blogs[index])

if __name__ == "__main__":
    app.run(debug=True)

