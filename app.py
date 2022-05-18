from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY DATABASE_URI'] = 'sqlite:///date.db'

db = SQLAlchemy(app)


from routes import *

if __name__ == '__main__':
    app.run(debug=True)