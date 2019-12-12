import sqla_wrapper
import os

#SQLITE_FILE = ':memory:'
SQLITE_FILE = 'localhost.sqlite'

db = sqla_wrapper.SQLAlchemy(os.getenv("DATABASE_URL", f"sqlite:///{SQLITE_FILE}"))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False) # nullable = optional (true) oder pflicht (false)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    session_token = db.Column(db.String, nullable=True)
    session_expiry_datetime = db.Column(db.DateTime, nullable=True)


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    description = db.Column(db.String, unique=True)
    taste = db.Column(db.String)

    ## Brauchen wir mit der Datenbank nimma:
  #  def __init__(self, name, description, taste):
   #     self.name = name
    #    self.description = description
     #   self.taste = taste


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    booktitle = db.Column(db.String)
    bookauthor = db.Column(db.String)

  #  def __init__(self, title, author):
   #     self.title = title
    #    self.author = author


