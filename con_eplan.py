from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)

# MySQL Eplan
eplan = MySQL(app)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'adl_eplan'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
eplan.init_app(app)