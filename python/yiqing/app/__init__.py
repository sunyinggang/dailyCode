import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://yiqing:yiqing@39.98.49.111:3306/yiqing"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = '8906ced739ec4d3a80c0bcecfb15fb8c'
app.debug = True

db = SQLAlchemy(app)

from app.home import home as home_blueprint


app.register_blueprint(home_blueprint, url_prefix="/model")
