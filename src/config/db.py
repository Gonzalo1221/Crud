from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql+pymysql://sql5728333:ZJPH4CaGFu@sql5.freesqldatabase.com/sql5728333'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = "final"

db = SQLAlchemy(app)

ma = Marshmallow(app)
