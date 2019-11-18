import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/about")
def about_me():
    return flask.render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return flask.render_template("portfolio.html")

if __name__ == '__main__':
    app.run()


