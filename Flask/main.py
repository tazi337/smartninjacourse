import flask
import random
import model

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
    return flask.render_template("secret-number-game.html", secret_number=random.randint(0,10))

@app.route("/blog")
def blog():

    recipe_1 = model.Recipe("Apfelstrudel", "Cut Apple Bake Sweet", "sweet dish")
    recipe_2 = model.Recipe("Hamburger", "Fry Meat and Eat", "salty dish")
    recipe_3 = model.Recipe("Soup", "Cut Carrots, Add Water", "salty dish")
    return flask.render_template("blog.html", recipes=[recipe_1, recipe_2, recipe_3])

if __name__ == '__main__':
    app.run()


