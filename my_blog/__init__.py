from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# This is where I set secret key
app.config['SECRET_KEY'] = '2feea2720d48bd16f90deb7fc68199e4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# db.init_app(app)
db = SQLAlchemy(app)

from my_blog import routes