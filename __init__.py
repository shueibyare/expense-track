from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenseDB.db'
app.config['SECRET_KEY'] = 'WEERT789)(*Er'
db = SQLAlchemy(app)


from application import routes