from flask import Flask, render_template

from blueprint_example import example_blueprint

app = Flask(__name__)
app.register_blueprint(example_blueprint, url_prefix="/blue")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/authors')
def authors():
    return render_template('authors.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/stories/')
@app.route('/stories/<story_id>')
def stories(story_id=None):
    return render_template('stories.html', story_id=story_id)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run()
