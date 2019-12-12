import datetime

import flask
import random
import model
import string
import hashlib
import time
import uuid

from flask import request
from flask import url_for

N_USERS = 10
N_RECIPES = 10
N_BOOKS = 10

app = flask.Flask(__name__)
db = model.db
db.create_all()


def hash_password(password):
    hasher = hashlib.sha512()
    password = password.encode('utf-8')
    hasher.update(password)
    return hasher.hexdigest()


def create_dummy_users():
    users = []
    for x in range(N_USERS):
        name = "".join(random.choices(string.ascii_lowercase, k=10))
        user = model.User(username=name, email=f"{name}@home.com", password=hash_password(name))
        users.append(user)

    my_user = model.User(username="admin", email="admin@home.com", password=hash_password("admin"))
    users.append(my_user)
    test_user = model.User(username="test", email="test@home.com", password=hash_password("test"))
    users.append(test_user)

    for user in users:
        if not db.query(model.User).filter_by(username=user.username).first():
            db.add(user)
        # geht auf die DB und gibt den User, der den gleichen Usernamen hat und gitb den ersten Eintrag zurück.
        #wenn er nichts findet, kommt none zurück (daher if not)
        db.commit()

def create_dummy_recipes():
    recipes = []
    for x in range(N_RECIPES):
        name = "".join(random.choices(string.ascii_lowercase, k=10))
        name = name.capitalize() #macht den ersten buchstaben groß
        description = "".join(random.choices(string.ascii_lowercase + "   ", k=80)) # alle buchstaben des alphabets plus ein leerzeichen
        taste = "".join(random.choices(string.ascii_lowercase, k=5))
        new_recipe = model.Recipe(name=name, description=description, taste=taste)
        recipes.append(new_recipe)


    recipe_1 = model.Recipe(name="Apfelstrudel", description="Cut Apple Bake Sweet", taste="sweet dish")
    recipes.append(recipe_1)
    recipe_2 = model.Recipe(name="Hamburger", description="Fry Meat and Eat", taste="salty dish")
    recipes.append(recipe_2)
    recipe_3 = model.Recipe(name="Soup", description="Cut Carrots, Add Water", taste="salty dish")
    recipes.append(recipe_3)

    for recipe in recipes:
        if not db.query(model.Recipe).filter_by(name=recipe.name).first():
            db.add(recipe)
    db.commit()


def create_dummy_books():
    books = []
    for x in range(N_BOOKS):
        booktitle = "".join(random.choices(string.ascii_lowercase + " ", k=20))
        booktitle = booktitle.capitalize() #macht den ersten buchstaben groß
        bookauthor = "".join(random.choices(string.ascii_lowercase + " ", k=15)) # alle buchstaben des alphabets plus ein leerzeichen
        bookauthor = bookauthor.capitalize()
        new_book = model.Books(booktitle=booktitle, bookauthor=bookauthor)
        books.append(new_book)


    book_1 = model.Books(booktitle="1984", bookauthor="George Orwell")
    books.append(book_1)
    book_2 = model.Books(booktitle="Farm der Tiere", bookauthor="George Owell")
    books.append(book_2)
    book_3 = model.Books(booktitle="Tod am Zentralfriedhof", bookauthor="Beate Maxian")
    books.append(book_3)


    for book in books:
        if not db.query(model.Books).filter_by(booktitle=book.booktitle).first():
            db.add(book)
    db.commit()


def add_dummy_data():
    create_dummy_users()
    create_dummy_recipes()
    create_dummy_books()
    # ruft die Funktion von oben, diese rufen wir ganz unten im Main als erstes


def require_session_token(func):
    """Decorator to require authentication to access routes"""
    def wrapper(*args, **kwargs):
        session_token = flask.request.cookies.get("session_token")
        redirect_url = flask.request.path or '/'
        if not session_token:
            app.logger.error('no token in request')
            return flask.redirect(flask.url_for('login', redirectTo=redirect_url))
        user = db.query(model.User).filter_by(session_token=session_token).filter(model.User.session_expiry_datetime>=datetime.datetime.now()).first()
        if not user:
            app.logger.error(f'token {session_token} not valid')
            return flask.redirect(flask.url_for('login', redirectTo=redirect_url))
        app.logger.info(f'authenticated user {user.username} with token {user.session_token} valid until {user.session_expiry_datetime.isoformat()}')
        flask.request.user = user
        return func(*args, **kwargs)

    # Renaming the function name:
    wrapper.__name__ = func.__name__
    return wrapper


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
    db_recipes = db.query(model.Recipe).filter_by(taste="salty dish").all()
## brauchen wir nicht mehr mit der Datenbank
   # recipe_1 = model.Recipe("Apfelstrudel", "Cut Apple Bake Sweet", "sweet dish")
    #recipe_2 = model.Recipe("Hamburger", "Fry Meat and Eat", "salty dish")
    #recipe_3 = model.Recipe("Soup", "Cut Carrots, Add Water", "salty dish")
    return flask.render_template("blog.html", recipes=db_recipes)

@app.route("/books")
def booklistold():
    all_books = db.query(model.Books).all()
    return flask.render_template('books.html', books=all_books)
    #db_books = db.query(model.Books).all()
    # book_1 = model.Books("1984", "George Orwell")
    # book_2 = model.Books("Farm der Tiere", "George Orwell")

@app.route("/homepage-hans")
def homepage_hans():
    return flask.render_template("homepage-hans.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    current_request = flask.request

    if current_request.method == "GET":
        return flask.render_template("register.html")

    elif current_request.method == "POST":
        # TODO: register valid user
        email=current_request.form.get('email')
        username=current_request.form.get('username')
        password=current_request.form.get('password')
        user_exists = db.query(model.User).filter_by(username=username).first()
        email_exists = db.query(model.User).filter_by(email=email).first()
        if user_exists:
            print("User already exists")
        elif email_exists:
            print("Email already exists")
        else:
            new_user = model.User(username=username, email=email, password=hash_password(password))
            db.add(new_user)
            db.commit()
            return flask.redirect(flask.url_for('register'))
        #wenn post, muss es einen redirect geben. hier redirecten wir auf die gleiche Seite


@app.route("/accounts")
@require_session_token
def accounts():

    # get session token
   # current_request = flask.request
    #session_token = current_request.cookies.get('session_token') # cookies ist hier eine directory, suche nach dem cookie namens session_token
    #if not session_token:
        # TODO: use redirect url to get back to this page after login
     #   return flask.redirect(flask.url_for('login', redirectTo='accounts'))
    #user = db.query(model.User).filter_by(session_token=session_token).first()
    #if not user:
     #   return flask.redirect(flask.url_for('login', redirectTo='accounts'))
   # if user and not user.session_expiry_datetime>datetime.datetime.now():
    #    return flask.redirect(flask.url_for('login', redirectTo='accounts'))

    # user is authenticated, refresh token expiry
    #user.session_expiry_datetime = datetime.datetime.now() + datetime.timedelta(seconds=3600)
    #db.add(user)
    #db.commit()

    all_user = db.query(model.User).all()
    return flask.render_template('accouts.html', accounts=all_user)

@app.route("/accounts/<account_id>/delete", methods=["GET", "POST"])
def account_delete(account_id):
    user_to_delete = db.query(model.User).get(account_id)
    if user_to_delete is None:
        return flask.redirect(flask.url_for('accounts'))

    current_request = flask.request
    if current_request.method=="GET":
        return flask.render_template("account_delete_html.html", account=user_to_delete)
    elif current_request.method=="POST":
        db.delete(user_to_delete)
        db.commit()
        return flask.redirect(flask.url_for('accounts'))
    else:
        return flask.redirect(flask.url_for('accounts'))


@app.route("/booksaddone", methods=["GET", "POST"])
def booksaddone():
    current_request = flask.request

    if current_request.method == "GET":
        return flask.render_template("books-add-one.html")
    elif current_request.method == "POST":
        # TODO: register book
        booktitle=current_request.form.get('booktitle')
        bookauthor=current_request.form.get('bookauthor')
        title_exists = db.query(model.Books).filter_by(booktitle=booktitle).first()
        author_exists = db.query(model.Books).filter_by(bookauthor=bookauthor).first()
        if title_exists:
            print("Title already exists")
        elif author_exists:
            print("Author already exists")
        else:
            new_book = model.Books(booktitle=booktitle, bookauthor=bookauthor)
            db.add(new_book)
            db.commit()
            return flask.redirect(flask.url_for('booksaddone'))


@app.route("/booklist")
def booklist():
    all_books = db.query(model.Books).all()
    return flask.render_template('booklist.html', books=all_books)


@app.route("/booklist/<book_id>/delete", methods=["GET", "POST"])
def book_delete(book_id):
    book_to_delete = db.query(model.Books).get(book_id)
    if book_to_delete is None:
        return flask.redirect(flask.url_for('booklist'))

    current_request = flask.request
    if current_request.method=="GET":
        return flask.render_template("book-delete.html", book=book_to_delete)
    elif current_request.method=="POST":
        db.delete(book_to_delete)
        db.commit()
        return flask.redirect(flask.url_for('booklist'))
    else:
        return flask.redirect(flask.url_for('booklist'))


@app.route("/accounts/<account_id>/edit", methods=["GET", "POST"])
def account_edit(account_id):
    user_to_edit = db.query(model.User).get(account_id)
    if user_to_edit is None:
        return flask.redirect(flaks.url_for('accounts'))

    current_request = flask.request
    if current_request.method=="GET":
        return flask.render_template("account_edit.html", account=user_to_edit)
    elif current_request.method=="POST":
        email=current_request.form.get('email')
        username=current_request.form.get('username')
        user_to_edit.email = email
        user_to_edit.username = username

        db.add(user_to_edit)
        db.commit()
        return flask.redirect(flask.url_for('accounts'))


@app.route("/booklist/<book_id>/edit", methods=["GET", "POST"])
def book_edit(book_id):
    book_to_edit = db.query(model.Books).get(book_id)
    if book_to_edit is None:
        return flask.redirect(flaks.url_for('booklist'))

    current_request = flask.request
    if current_request.method=="GET":
        return flask.render_template("book-edit.html", book=book_to_edit)
    elif current_request.method=="POST":
        booktitle=current_request.form.get('booktitle')
        bookauthor=current_request.form.get('bookauthor')
        book_to_edit.booktitle = booktitle
        book_to_edit.bookauthor = bookauthor

        db.add(book_to_edit)
        db.commit()
        return flask.redirect(flask.url_for('booklist'))


@app.route("/login", methods=['GET', 'POST'])
def login():
    current_request = flask.request
    if current_request.method=='GET':
        return flask.render_template('login.html')
    elif current_request.method == 'POST':
        email = current_request.form.get('email')
        password = current_request.form.get('password')
        user = db.query(model.User).filter_by(email=email).first()
        if user is None:
            print("User does not exist")
            return flask.redirect(flask.url_for('login'))
        else:
            if hash_password(password) == user.password:
                # find redirect method from request argument
                redirect_url = current_request.args.get('redirectTo', '/')

                # generate token and expiry time in 1 hour from now
                session_token = str(uuid.uuid4())
                session_expiry_datetime = datetime.datetime.now() + datetime.timedelta(seconds=3600)
                # update user with new session token and expiry
                user.session_token = session_token
                user.session_expiry_datetime = session_expiry_datetime
                # save in DB
                db.add(user)
                db.commit()

                # make response and add cookie with session token
                response = flask.make_response(flask.redirect(redirect_url))
                response.set_cookie('session_token', session_token)
                return response
            else:
                return flask.redirect(flask.url_for('forbidden'))


@app.route("/forbidden")
def forbidden():
    return flask.render_template("forbidden.html")

@app.route('/logout')
def logout():
    # get session token
    current_request = flask.request
    session_token = current_request.cookies.get(
        'session_token')  # cookies ist hier eine directory, suche nach dem cookie namens session_token
    if not session_token:
        # TODO: use redirect url to get back to this page after login
        return flask.redirect(flask.url_for('login'))
    user = db.query(model.User).filter_by(session_token=session_token).first()
    if not user:
        return flask.redirect(flask.url_for('login'))
    if user and not user.session_expiry_datetime > datetime.datetime.now():
        return flask.redirect(flask.url_for('login'))

    # remove token from db and browser cookie
    user.session_token = None
    user.session_expiry_datetime = None
    db.add(user)
    db.commit()


    return flask.redirect(flask.url_for('login'))


if __name__ == '__main__':
    add_dummy_data()
    app.run()


