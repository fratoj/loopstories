from flask import Flask, render_template

from authors import authors_blueprint
from blueprint_example import example_blueprint
from stories import stories_blueprint

app = Flask(__name__)
app.register_blueprint(example_blueprint, url_prefix="/blue")
app.register_blueprint(stories_blueprint, name="stories", url_prefix="/stories")
app.register_blueprint(authors_blueprint, name="authors", url_prefix="/authors")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/hello/")
@app.route("/hello/<name>")
def hello_world(name=None):
    return render_template("hello.html", name=name)


if __name__ == "__main__":
    app.run()
