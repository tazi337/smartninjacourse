import flask
import random

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("index.html", myname="Tamara")

@app.route("/about")
def about_me():
    return flask.render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return flask.render_template("portfolio.html")

@app.route("/secret-number-game")
def secret_number_game():
    return flask.render_template("secret-number-game.html", secret_number=random.randint)

if __name__ == '__main__':
    app.run()


