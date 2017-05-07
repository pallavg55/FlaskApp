from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return 'This is my homepage'


@app.route("/post")
def post():
    return "<h1>Trying to create a post</h1>"


@app.route("/post/<username>")
def print_username(username):
    return "<h1>Hello {}</h1>".format(username)


@app.route("/post/<int:id>")
def pritn_id(id):
    return "<h1>My id is {}</h1>".format(id)


if __name__ == "__main__":
    app.run(debug=True)
