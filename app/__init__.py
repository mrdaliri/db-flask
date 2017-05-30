from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config.from_object('config')

mysql = MySQL()
mysql.init_app(app)
db = mysql.connect()

from app import views
