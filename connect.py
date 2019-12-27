from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)

# MySQL Users
mysql = MySQL(app)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'adl_user'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)